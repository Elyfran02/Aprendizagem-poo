"""
Ponto de Entrada Principal da Aplicação (Main Entry Point).

Este script é responsável por inicializar e conectar as camadas da aplicação
e iniciar a interface gráfica.
"""

from src import AlunoDAO, AlunoGUI


def main():
    """Função principal que orquestra a inicialização da aplicação."""
    # 1. Inicializa a camada de acesso a dados (DAO)
    dao = AlunoDAO()
    
    # 2. Inicializa a interface gráfica (GUI) injetando o DAO
    app = AlunoGUI(dao)
    app.mainloop()

if __name__ == "__main__":
    main()