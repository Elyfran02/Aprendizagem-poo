

class Endereco_aluno:
    """
    classe que representa o endereço do aluno
    """
    def __init__(self, rua : str, num : str, cep : str, bairro : str, cidade : str, unidade_federativa : str):
        """_
        diferentes parametros e atributos do construtor
        """
        self.rua : str = rua
        self.num : str = num
        self.cep : str = cep
        self.bairro : str = bairro
        self.cidade : str = cidade
        self.unidade_federativa : str = unidade_federativa
    def __del__(self):
         print(f"[Log] Objeto do Endereço {self.cep} destruído e memória liberada.")
           