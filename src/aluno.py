from datetime import date

from .aluno_endereco import Endereco_aluno


class Aluno:
    """
    Classe que representa a entidade Aluno no domínio da aplicação.
    """

    # 1. Construtor
    def __init__(self, matricula: str, nome: str, data_nascimento: date, peso: float, altura: float, sexo: str, endereco: Endereco_aluno):
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
        self.sexo: str = sexo #adicioando
        self.estado: str = self.tipo_imc() #adicioando
        self.endereco: Endereco_aluno = endereco

    # Exemplo de um método de negócio útil usando os novos atributos
    def calcular_imc(self) -> float:
        """
        Calcula o Índice de Massa Corporal (IMC) do aluno com base no sexo.
        """
        if self.altura > 0 and self.peso > 0:
            return round(self.peso / (self.altura ** 2), 2)
        return 0.0
 
    def tipo_imc(self) -> str:
        """
        Direciona o tipo do IMC baseado no sexo do aluno.(abaixo dopeso,peso noral,sobrepeso...)
        """
        imc = self.calcular_imc()
        if self.sexo.upper() == "M":
                intervalo = [
                   (0,18.5, "Abaixo do peso"),
                   (18.5, 24.9, "peso normal"),
                   (25.0, 29.9, "Sobrepeso"),
                   (30.0, 34.9, "Obesidade grau I"),
                   (35.0, 39.9, "Obesidade grau II"),
                   (40.0, float('inf'), "Obesidade grau III")
                   ]
                for limite_inferior, limite_superior, classificacao in intervalo:
                    if limite_inferior <= imc <= limite_superior:
                        return classificacao
        elif self.sexo.upper() == "F":
                intervalo = [
                   (0,16.99, "Muito abaixo do peso"),
                   (17.0, 18.49, "abaixo do peso"),
                   (18.5, 24.99, "Peso normal"),
                   (25.0, 29.99, "Acima do peso"),
                   (30.0, 34.99, "Obesidade grau I"),
                   (35.0, 39.99, "Obesidade grau II"),
                   (40.0, float('inf'), "Obesidade grau III")
                   ]
                for limite_inferior, limite_superior, classificacao in intervalo:
                    if limite_inferior <= imc <= limite_superior:
                        return classificacao
        
        return "Indefinido"
    def __del__(self):    
        """O método __del__ é o destruidor em Python. Ele é chamado automaticamente pelo Garbage Collector (Coletor de Lixo) quando a contagem de referências de um objeto chega a zero.    
        Nota: O uso de `del` no código (como em `aluno_dao.py`) apenas decrementa
        a contagem de referências, não garante a chamada imediata deste método.
        """
        print(f"[Log] Objeto do Aluno {self.nome} destruído e memória liberada.")
    