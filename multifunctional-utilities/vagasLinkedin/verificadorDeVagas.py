from playwright import *
from beautifulsoup4 import *
from lxml import *
from sqlite3 import *

"""
Ideia Futura:

    Novo e-mail
        │
        ▼
    É do LinkedIn?
        │
        ▼
    Extrai link da vaga
        │
        ▼
    Abre a vaga
        │
        ├── Expirada?
        │      │
        │      └── Sim → apaga e-mail
        │
        ▼
    Tem Candidatura Simplificada?
        │
        ├── Não → apaga ou arquiva
        │
        ▼
    Aplica automaticamente
        │
        ▼
    Sucesso?
        │
        ├── Sim → apaga e-mail
        └── Não → deixa marcado para revisão

"""