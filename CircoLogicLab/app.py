import streamlit as st

from logic import BooleanExpressionError, evaluate_expression

st.set_page_config(
    page_title="CircoLogicLab",
    page_icon="⚙️",
    layout="centered",
)

st.title("CircoLogicLab")
st.caption("Uma calculadora interativa de lógica booleana")

st.markdown(
    """
    Digite uma expressão lógica, escolha **Calcular** e veja o resultado.
    Você pode usar palavras em português, palavras em inglês ou símbolos.
    """
)

with st.expander("Como escrever as expressões"):
    st.markdown(
        """
        | Operação | Formas aceitas |
        |---|---|
        | NÃO | `not`, `não`, `nao`, `!`, `-` |
        | E | `and`, `e`, `&&`, `*`, `.` |
        | OU | `or`, `ou`, "||", "+" |
        | XOR | `xor`, `^` |
        | NAND | `nand` |
        | NOR | `nor` |
        | XNOR | `xnor` |

        **Valores:** `verdadeiro` / `falso`, `true` / `false`, `v` / `f`, `1` / `0`.

        **Exemplos:**
        - `verdadeiro && !falso`
        - `(1 xor 0) and 1`
        - `falso nand verdadeiro`
        """
    )

with st.form("calculator_form"):
    expression = st.text_input(
        "Expressão booleana",
        placeholder="Ex.: verdadeiro && !falso",
    )
    submitted = st.form_submit_button("Calcular", type="primary", use_container_width=True)

if submitted:
    if not expression.strip():
        st.warning("Digite uma expressão antes de calcular.")
    else:
        try:
            result = evaluate_expression(expression)
            if result:
                st.success("Resultado: VERDADEIRO")
            else:
                st.error("Resultado: FALSO")
            st.code(f"{expression}  →  {str(result).upper()}", language="text")
        except BooleanExpressionError as exc:
            st.error(f"Expressão inválida: {exc}")

st.divider()
st.caption("CircoLogicLab • Projeto de estudos em Python by Diogo Speck")