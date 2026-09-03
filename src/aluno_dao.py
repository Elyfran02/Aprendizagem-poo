from typing import Optional

from .aluno import Aluno


class No:
    """
    Classe auxiliar que representa um 'Nó' ou 'Elo' da Lista Encadeada.
    """
    def __init__(self, aluno: Aluno):
        self.aluno: Aluno = aluno
        """tipagem de dados, dizendo que a vriável é do tipo aluno
        """
        self.proximo: Optional['No'] = None
        """o primeiro aponta pro próximo nó, que é do tipo No, e o segundo é None, pois não há próximo nó ainda
        """

class AlunoDAO:
    """
    Data Access Object para a classe Aluno.
    Utiliza uma Lista Encadeada Simples como estrutura de armazenamento em memória.
    """
    
    def __init__(self):
        """sem parametro de atributo
        """
        # O 'head' (cabeça) é o ponteiro para o primeiro elemento da lista encadeada
        # O 'tail' (cauda) é o ponteiro para o último, otimizando a inserção para O(1)
        self.head: Optional[No] = None
        self.tail: Optional[No] = None

    def inserir(self, aluno: Aluno) -> None:
        """Insere um novo aluno no final da lista encadeada."""
        novo_no = No(aluno)
        
        # Se a lista estiver vazia, o novo nó é tanto a cabeça quanto a cauda
        if self.head is None:
            self.head = novo_no
            self.tail = novo_no
        # Caso contrário, adiciona após a cauda atual e atualiza a cauda
        else:
            if self.tail: # Checagem para o type checker
                self.tail.proximo = novo_no
                self.tail = novo_no

    def alterar(self, matricula: str, novos_dados: Aluno) -> bool:
        """
        Altera os dados de um Aluno baseado na matrícula.
        Retorna True se alterou com sucesso, False se não encontrou.
        """
        atual = self.head
        while atual is not None:
            if atual.aluno.matricula == matricula:
                # Mantém a matrícula original (geralmente é chave primária imutável)
                atual.aluno.nome = novos_dados.nome
                atual.aluno.data_nascimento = novos_dados.data_nascimento
                atual.aluno.peso = novos_dados.peso
                atual.aluno.altura = novos_dados.altura
                atual.aluno.sexo = novos_dados.sexo #adicionado
                atual.aluno.endereco = novos_dados.endereco #adicionado
                return True
            atual = atual.proximo
            
        return False

    def obter_por_matricula(self, matricula: str) -> Optional[Aluno]:
        """Realiza uma pesquisa exata baseada no número da matrícula."""
        atual = self.head
        while atual is not None:
            if atual.aluno.matricula == matricula:
                return atual.aluno
            atual = atual.proximo
            
        return None

    def obter_por_nome(self, nome: str) -> list[Aluno]:
        """
        Realiza uma pesquisa parcial ou exata baseada no nome do Aluno.
        Retorna uma lista com as ocorrências para facilitar o uso na GUI.
        """
        resultados = []
        atual = self.head
        nome_busca = nome.lower()
        
        while atual is not None:
            if nome_busca in atual.aluno.nome.lower():
                resultados.append(atual.aluno)
            atual = atual.proximo
            
        return resultados

    def listar(self) -> list[Aluno]:
        """
        Lista todos os Alunos extraindo-os da lista encadeada 
        e retornando em ordem alfabética pelo nome.
        """
        todos_alunos = []
        atual = self.head
        
        # 1. Extrai todos os objetos da lista encadeada
        while atual is not None:
            todos_alunos.append(atual.aluno)
            atual = atual.proximo
            
        # 2. Ordena usando a função nativa sort do Python baseada no atributo 'nome'
        todos_alunos.sort(key=lambda a: a.nome.lower())
        
        return todos_alunos

    def excluir(self, matricula: str) -> bool:
        """
        Exclui um Aluno pela sua matrícula ajustando os ponteiros da lista encadeada.
        Retorna True se excluiu, False se não encontrou.
        """
        atual = self.head
        anterior = None
        
        while atual is not None:
            if atual.aluno.matricula == matricula:
                # Caso 1: O nó a ser removido é a cabeça da lista
                if anterior is None:
                    self.head = atual.proximo
                    # Se a lista ficou vazia após a remoção, a cauda também é None
                    if self.head is None:
                        self.tail = None
                # Caso 2: O nó está no meio ou no final
                else:
                    anterior.proximo = atual.proximo
                    # Se o nó removido era a cauda, atualiza a cauda para o nó anterior
                    if atual == self.tail:
                        self.tail = anterior
                
                # Apenas decrementa a contagem de referência. O Garbage Collector chamará __del__.
                del atual.aluno 
                return True
                
            anterior = atual
            atual = atual.proximo
            
        return False