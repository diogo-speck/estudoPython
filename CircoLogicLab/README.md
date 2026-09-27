# CircoLogicLab

Calculadora visual de lógica booleana feita com Python e Streamlit.
https://diogospeck.streamlit.app/

## Funcionalidades iniciais

- Avaliação de expressões booleanas.
- Operadores NOT, AND, OR, XOR, NAND, NOR e XNOR.
- Parênteses e diferentes formas de escrever operadores em português, inglês e símbolos.
- Parser próprio, sem executar a expressão com `eval()`.

## Requisitos

- Python 3.10 ou superior

## Executar localmente

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências e inicie a aplicação:

```bash
pip install -r requirements.txt
streamlit run app.py
```

O Streamlit mostrará no terminal o endereço local da aplicação.

## Operadores aceitos

| Operação | Formas |
|---|---|
| NOT | `not`, `não`, `nao`, `!`, `-` |
| AND | `and`, `e`, `&&`, `*`, `.` |
| OR | `or`, `ou`, `||`, `+` |
| XOR | `xor`, `^` |
| NAND | `nand` |
| NOR | `nor` |
| XNOR | `xnor` |

Valores aceitos: `verdadeiro`, `falso`, `true`, `false`, `v`, `f`, `1` e `0`.

## Próximas ideias

- Tabela-verdade automática.
- Suporte a variáveis como A, B e C.
- Visualização de circuitos lógicos.
- Histórico de expressões calculadas.