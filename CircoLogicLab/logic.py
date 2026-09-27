"""Parser e avaliador de expressões booleanas do CircoLogicLab.

Não usa eval(): a expressão é tokenizada e interpretada por um parser pequeno.
Prioridade: parênteses, NOT, XOR/XNOR, AND/NAND, OR/NOR.
"""

import re


class BooleanExpressionError(ValueError):
    """Erro de sintaxe ou de conteúdo em uma expressão booleana."""


_TOKEN_PATTERN = re.compile(
    r"""
    \s*
    (
        \&\&|\|\||\^|[!()+*.\-]
        |[A-Za-zÀ-ÿ]+
        |[01]
    )
    """,
    re.VERBOSE,
)

_TRUE_WORDS = {"verdadeiro", "true", "v"}
_FALSE_WORDS = {"falso", "false", "f"}
_NOT_WORDS = {"not", "não", "nao"}
_AND_WORDS = {"and", "e"}
_OR_WORDS = {"or", "ou"}
_XOR_WORDS = {"xor"}
_NAND_WORDS = {"nand"}
_NOR_WORDS = {"nor"}
_XNOR_WORDS = {"xnor"}


def _tokenize(expression: str) -> list[str]:
    tokens = []
    position = 0

    while position < len(expression):
        if expression[position:].strip() == "":
            break

        match = _TOKEN_PATTERN.match(expression, position)
        if not match:
            raise BooleanExpressionError(
                f"caractere não reconhecido na posição {position + 1}."
            )

        tokens.append(match.group(1).lower())
        position = match.end()

    if not tokens:
        raise BooleanExpressionError("a expressão está vazia.")

    return tokens


class _Parser:
    def __init__(self, tokens: list[str]):
        self.tokens = tokens
        self.position = 0

    def _peek(self):
        if self.position >= len(self.tokens):
            return None
        return self.tokens[self.position]

    def _take(self):
        token = self._peek()
        if token is not None:
            self.position += 1
        return token

    def _is_operator(self, token, words, symbols=()):
        return token in words or token in symbols

    def parse(self) -> bool:
        value = self._parse_or()
        if self._peek() is not None:
            raise BooleanExpressionError(
                f"token inesperado: '{self._peek()}'."
            )
        return value

    def _parse_or(self) -> bool:
        value = self._parse_and()
        while True:
            token = self._peek()
            if token in _OR_WORDS or token == "||" or token == "+":
                self._take()
                right = self._parse_and()
                value = value or right
            elif token in _NOR_WORDS:
                self._take()
                right = self._parse_and()
                value = not (value or right)
            else:
                return value

    def _parse_and(self) -> bool:
        value = self._parse_xor()
        while True:
            token = self._peek()
            if token in _AND_WORDS or token in {"&&", "*", "."}:
                self._take()
                right = self._parse_xor()
                value = value and right
            elif token in _NAND_WORDS:
                self._take()
                right = self._parse_xor()
                value = not (value and right)
            else:
                return value

    def _parse_xor(self) -> bool:
        value = self._parse_unary()
        while True:
            token = self._peek()
            if token in _XOR_WORDS or token == "^":
                self._take()
                value = value != self._parse_unary()
            elif token in _XNOR_WORDS:
                self._take()
                value = value == self._parse_unary()
            else:
                return value

    def _parse_unary(self) -> bool:
        token = self._peek()

        if token in _NOT_WORDS or token in {"!", "-"}:
            self._take()
            return not self._parse_unary()

        if token == "(":
            self._take()
            value = self._parse_or()
            if self._take() != ")":
                raise BooleanExpressionError("faltou fechar um parêntese.")
            return value

        token = self._take()
        if token in _TRUE_WORDS or token == "1":
            return True
        if token in _FALSE_WORDS or token == "0":
            return False
        if token is None:
            raise BooleanExpressionError("a expressão terminou antes de um valor.")
        if token == ")":
            raise BooleanExpressionError("há um parêntese de fechamento sem abertura.")
        raise BooleanExpressionError(f"valor desconhecido: '{token}'.")


def evaluate_expression(expression: str) -> bool:
    """Avalia uma expressão booleana e retorna True ou False."""
    if not isinstance(expression, str):
        raise BooleanExpressionError("a expressão precisa ser um texto.")

    tokens = _tokenize(expression)
    return _Parser(tokens).parse()
