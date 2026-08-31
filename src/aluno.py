from datetime import date


class Aluno:
    """
    Classe que representa a entidade Aluno no domínio da aplicação.
    """

    # 1. Construtor
    def __init__(self, matricula: str, nome: str, data_nascimento: date, peso: float, altura: float, sexo: str ):
        """
        O método __init__ é o construtor em Python. 
        Ele inicializa os atributos da instância no momento de sua criação.
        """
        """ "def"cria uma função ou um procedimento"""
        """ "self" é uma referência à instância atual da classe, permitindo acessar atributos e métodos da classe. Ele aponta para o primeiro valor"""

        """diferente entre parametro e atributo do construtor
        parametro: matricula, nome, data_nascimento, peso, altura
        atributo: self.matricula, self.nome, self.data_nascimento, self.peso, self.altura;"""
        self.matricula: str = matricula
        self.nome: str = nome
        self.data_nascimento: date = data_nascimento
        self.peso: float = peso
        self.altura: float = altura
        self.sexo: str = sexo
        
    # 2. Destruidor
    def __del__(self):
        """
        O método __del__ é o destruidor em Python.
        Ele é chamado automaticamente pelo Garbage Collector (Coletor de Lixo) quando
        a contagem de referências de um objeto chega a zero.
        
        Nota: O uso de `del` no código (como em `aluno_dao.py`) apenas decrementa
        a contagem de referências, não garante a chamada imediata deste método.
        """
        print(f"[Log] Objeto do Aluno {self.nome} destruído e memória liberada.")

    # Exemplo de um método de negócio útil usando os novos atributos
    def calcular_imc(self) -> float:
        """
        Calcula o Índice de Massa Corporal (IMC) do aluno.
        """
        if self.altura > 0:
            return round(self.peso / (self.altura ** 2), 2)
        return 0.0