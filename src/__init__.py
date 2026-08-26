"""
Arquivo de inicialização do pacote 'src'.

Este arquivo transforma o diretório 'src' em um pacote Python e expõe
as classes principais do sistema para facilitar a importação em outros
módulos, criando uma API pública para o pacote.
"""

from .aluno import Aluno
from .aluno_dao import AlunoDAO
from .gui import AlunoGUI