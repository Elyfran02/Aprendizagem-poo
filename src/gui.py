import tkinter as tk
from datetime import datetime
from tkinter import messagebox, ttk

from .aluno import Aluno
from .aluno_dao import AlunoDAO
from .aluno_endereco import Endereco_aluno


class AlunoGUI(tk.Tk):
    """
    Interface Gráfica para o CRUD de Alunos.
    Totalmente desacoplada das regras de armazenamento, interagindo apenas com o AlunoDAO.
    """
    def __init__(self, dao: AlunoDAO):
        super().__init__()
        self.dao = dao
        
        self.title("Sistema de Gestão de Alunos (Lista Encadeada)")
        self.geometry("800x600")
        
        # Configuração inicial da Interface
        self._configurar_estilo()
        self._criar_formulario()
        self._criar_botoes_acao()
        self._criar_tabela_listagem()
        
        # Povoa a tabela ao iniciar a aplicação
        self.acao_listar_todos()

    def _configurar_estilo(self):
        style = ttk.Style(self)
        # O tema 'clam' possui um visual mais moderno e limpo
        style.theme_use('clam')

    def _criar_formulario(self):
        frame_form = ttk.LabelFrame(self, text="Dados do Aluno", padding=(10, 10))
        frame_form.pack(fill=tk.X, padx=10, pady=5)

        # Matrícula
        ttk.Label(frame_form, text="Matrícula:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.entry_matricula = ttk.Entry(frame_form, width=20)
        self.entry_matricula.grid(row=0, column=1, sticky=tk.W, padx=5)

        # Nome
        ttk.Label(frame_form, text="Nome:").grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
        self.entry_nome = ttk.Entry(frame_form, width=40)
        self.entry_nome.grid(row=0, column=3, sticky=tk.W, padx=5)

        # Data de Nascimento
        ttk.Label(frame_form, text="Data Nasc. (DD/MM/AAAA):").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.entry_data_nasc = ttk.Entry(frame_form, width=20)
        self.entry_data_nasc.grid(row=1, column=1, sticky=tk.W, padx=5)

        # Peso
        ttk.Label(frame_form, text="Peso (kg):").grid(row=1, column=2, sticky=tk.W, padx=(10, 0))
        self.entry_peso = ttk.Entry(frame_form, width=15)
        self.entry_peso.grid(row=1, column=3, sticky=tk.W, padx=5)

        # Altura
        ttk.Label(frame_form, text="Altura (m):").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.entry_altura = ttk.Entry(frame_form, width=20)
        self.entry_altura.grid(row=2, column=1, sticky=tk.W, padx=5)

        # Sexo adicionado
        ttk.Label(frame_form, text="Sexo(M/F): ").grid(row=2, column=2, sticky=tk.W, padx=(10,0))
        self.entry_sexo = ttk.Entry(frame_form, width=20)
        self.entry_sexo.grid(row=2, column=3, sticky=tk.W, padx=5)

        #endereco adicionado
        ttk.Label(frame_form, text="Endereco:").grid(row=3, column=0, sticky=tk.W, pady=2)

        #Rua
        ttk.Label(frame_form, text="Rua: ").grid(row=4, column=0, sticky=tk.W, pady=2)
        self.entry_rua = ttk.Entry(frame_form, width=20)
        self.entry_rua.grid(row=4, column=1, sticky=tk.W, padx=5)

        #num
        ttk.Label(frame_form, text="Número: ").grid(row=4, column=2, sticky=tk.W, padx=(10, 0))
        self.entry_num = ttk.Entry(frame_form, width=20)
        self.entry_num.grid(row=4, column=3, sticky=tk.W, padx=5)

        #cep
        ttk.Label(frame_form, text="CEP: ").grid(row=5, column=0, sticky=tk.W, pady=2)
        self.entry_cep = ttk.Entry(frame_form, width=20)
        self.entry_cep.grid(row=5, column=1, sticky=tk.W, padx=5)

        #bairro
        ttk.Label(frame_form, text="Bairro: ").grid(row=5, column=2, sticky=tk.W, padx=(10, 0))
        self.entry_bairro = ttk.Entry(frame_form, width=20)
        self.entry_bairro.grid(row=5, column=3, sticky=tk.W, padx=5)

        #cidade
        ttk.Label(frame_form, text="Cidade: ").grid(row=6, column=0, sticky=tk.W, pady=2)
        self.entry_cidade = ttk.Entry(frame_form, width=20)
        self.entry_cidade.grid(row=6, column=1, sticky=tk.W, padx=5)

        #unidade_federativa
        ttk.Label(frame_form, text="UF: ").grid(row=6, column=2, sticky=tk.W, padx=(10, 0))
        self.entry_unidade_federativa = ttk.Entry(frame_form, width=20)
        self.entry_unidade_federativa.grid(row=6, column=3, sticky=tk.W, padx=5)



    def _criar_botoes_acao(self):
        frame_botoes = tk.Frame(self)
        frame_botoes.pack(fill=tk.X, padx=10, pady=5)

        ttk.Button(frame_botoes, text="Inserir", command=self.acao_inserir).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_botoes, text="Alterar", command=self.acao_alterar).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_botoes, text="Excluir", command=self.acao_excluir).pack(side=tk.LEFT, padx=2)
        ttk.Button(frame_botoes, text="Limpar", command=self.limpar_campos).pack(side=tk.LEFT, padx=2)
        
        # Botões de Pesquisa/Listagem agrupados à direita
        ttk.Button(frame_botoes, text="Listar Todos", command=self.acao_listar_todos).pack(side=tk.RIGHT, padx=2)
        ttk.Button(frame_botoes, text="Pesquisar Nome", command=self.acao_pesquisar_nome).pack(side=tk.RIGHT, padx=2)
        ttk.Button(frame_botoes, text="Pesquisar Matrícula", command=self.acao_pesquisar_matricula).pack(side=tk.RIGHT, padx=2)

    def _criar_tabela_listagem(self):
        colunas = ("matricula", "nome", "data_nascimento", "peso", "altura", "sexo", "estado", "rua", "num", "cep", "bairro", "cidade", "unidade_federativa")
        self.tabela = ttk.Treeview(self, columns=colunas, show='headings', height=15)
        
        self.tabela.heading("matricula", text="Matrícula")
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("data_nascimento", text="Data de Nascimento")
        self.tabela.heading("peso", text="Peso (kg)")
        self.tabela.heading("altura", text="Altura (m)")
        self.tabela.heading("sexo", text="Sexo(M/F)") #adicionado
        self.tabela.heading("estado", text="Estado") #adicionado
        self.tabela.heading("rua", text="Rua")
        self.tabela.heading("num", text="Número")
        self.tabela.heading("cep", text="Cep") #adicionado
        self.tabela.heading("bairro", text="Bairro") #adicionado
        self.tabela.heading("cidade", text="Cidade") #adicionado
        self.tabela.heading("unidade_federativa", text="Unidade Federativa") #adicionado
        
        self.tabela.column("matricula", width=100, anchor=tk.CENTER)
        self.tabela.column("data_nascimento", width=100, anchor=tk.CENTER)
        self.tabela.column("peso", width=80, anchor=tk.CENTER)
        self.tabela.column("altura", width=80, anchor=tk.CENTER)
        self.tabela.column("sexo", width=80, anchor=tk.CENTER) #adicionado
        self.tabela.column("estado", width=200, anchor=tk.CENTER) #adicionado
        self.tabela.column("rua", width=150, anchor=tk.CENTER)
        self.tabela.column("num", width=70, anchor=tk.CENTER)
        self.tabela.column("cep", width=100, anchor=tk.CENTER) #adicionado
        self.tabela.column("bairro", width=150, anchor=tk.CENTER) #adicionado
        self.tabela.column("cidade", width=150, anchor=tk.CENTER) #adicionado
        self.tabela.column("unidade_federativa", width=200, anchor=tk.CENTER) #adicionado

        self.tabela.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.tabela.bind('<ButtonRelease-1>', self.selecionar_linha)

    # --- MÉTODOS AUXILIARES ---

    def _ler_formulario(self) -> Aluno:
        """Lê os campos do formulário, converte os tipos e retorna um objeto Aluno."""
        matricula = self.entry_matricula.get().strip()
        nome = self.entry_nome.get().strip()
        data_nasc_str = self.entry_data_nasc.get().strip()
        peso_str = self.entry_peso.get().replace(',', '.').strip()
        altura_str = self.entry_altura.get().replace(',', '.').strip()
        sexo_str = self.entry_sexo.get().strip().upper()
        endereco = Endereco_aluno(
            self.entry_rua.get().strip(),
            self.entry_num.get().strip(),
            self.entry_cep.get().strip(),
            self.entry_bairro.get().strip(),
            self.entry_cidade.get().strip(),
            self.entry_unidade_federativa.get().strip(),
        )

        if not all([matricula, nome, data_nasc_str, peso_str, altura_str, sexo_str]):
            raise ValueError("Todos os campos são obrigatórios e devem ser preenchidos.")

        try:
            # O aviso "Naive datetime" ocorre porque strptime() cria um objeto datetime
            # sem fuso horário. No entanto, como o objetivo é apenas a data de nascimento,
            # a informação de tempo/fuso é irrelevante. A chamada .date() no final
            # extrai somente o objeto 'date', que é o esperado, tornando o código
            # funcionalmente correto e o aviso seguro para ser ignorado neste contexto.
            data_nascimento = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato de data inválido. Use o formato DD/MM/AAAA.")
        
        try:
            peso = float(peso_str)
            if peso <= 0:
                raise ValueError()
        except ValueError:
            raise ValueError("Peso inválido. Deve ser um número positivo.")
            
        try:
            altura = float(altura_str)
            if altura <= 0:
                raise ValueError()
        except ValueError:
            raise ValueError("Altura inválida. Deve ser um número positivo.")

        try:
            sexo = str(sexo_str).upper()
            if sexo[0] not in ["M", "F"]:
                raise ValueError()
        except (ValueError, IndexError):
            raise ValueError("Sexo inválido. Digite M ou F.")
        
            
        return Aluno(matricula, nome, data_nascimento, peso, altura, sexo, endereco)

    def limpar_campos(self):
        self.entry_matricula.delete(0, tk.END)
        self.entry_nome.delete(0, tk.END)
        self.entry_data_nasc.delete(0, tk.END)
        self.entry_peso.delete(0, tk.END)
        self.entry_altura.delete(0, tk.END)
        self.entry_matricula.focus()
        self.entry_sexo.delete(0, tk.END)
        self.entry_rua.delete(0, tk.END)
        self.entry_num.delete(0, tk.END)
        self.entry_cep.delete(0, tk.END)
        self.entry_bairro.delete(0, tk.END)
        self.entry_cidade.delete(0, tk.END)
        self.entry_unidade_federativa.delete(0, tk.END)

    def _atualizar_tabela(self, alunos):
        """Limpa a tabela atual e a preenche com a lista de alunos fornecida."""
        for row in self.tabela.get_children():
            self.tabela.delete(row)
            
        for aluno in alunos:
            data_formatada = aluno.data_nascimento.strftime("%d/%m/%Y")
            self.tabela.insert("", tk.END, values=(
                aluno.matricula, 
                aluno.nome, 
                data_formatada, 
                f"{aluno.peso:.2f}", 
                f"{aluno.altura:.2f}",
                aluno.sexo,
                aluno.estado,
                aluno.endereco.rua,
                aluno.endereco.num,
                aluno.endereco.cep,
                aluno.endereco.bairro,
                aluno.endereco.cidade,
                aluno.endereco.unidade_federativa,
            ))

    def selecionar_linha(self, event):
        """Preenche o formulário com os dados da linha selecionada na tabela."""
        item_selecionado = self.tabela.focus()
        if item_selecionado:
            valores = self.tabela.item(item_selecionado, "values")
            self.limpar_campos()
            self.entry_matricula.insert(0, valores[0])
            self.entry_nome.insert(0, valores[1])
            self.entry_data_nasc.insert(0, valores[2])
            self.entry_peso.insert(0, valores[3])
            self.entry_altura.insert(0, valores[4])
            self.entry_sexo.insert(0, valores[5]) #adicionado
            self.entry_rua.insert(0, valores[7])
            self.entry_num.insert(0, valores[8])
            self.entry_cep.insert(0, valores[9])
            self.entry_bairro.insert(0, valores[10])
            self.entry_cidade.insert(0, valores[11])
            self.entry_unidade_federativa.insert(0, valores[12])

    # --- MÉTODOS DE AÇÃO (INTEGRAÇÃO COM O DAO) ---

    def acao_inserir(self):
        try:
            novo_aluno = self._ler_formulario()
            # Verifica se já existe para evitar duplicidade de matrícula
            if self.dao.obter_por_matricula(novo_aluno.matricula):
                messagebox.showwarning("Aviso", "Já existe um aluno com esta matrícula.")
                return
                
            self.dao.inserir(novo_aluno)
            messagebox.showinfo("Sucesso", "Aluno inserido com sucesso!")
            self.limpar_campos()
            self.acao_listar_todos()
        except ValueError as e:
            messagebox.showerror("Erro de Validação", f"Verifique os dados informados:\n{e}")

    def acao_alterar(self):
        try:
            aluno_atualizado = self._ler_formulario()
            sucesso = self.dao.alterar(aluno_atualizado.matricula, aluno_atualizado)
            if sucesso:
                messagebox.showinfo("Sucesso", "Dados do aluno alterados com sucesso!")
                self.limpar_campos()
                self.acao_listar_todos()
            else:
                messagebox.showerror("Erro", "Aluno não encontrado pela matrícula informada.")
        except ValueError as e:
            messagebox.showerror("Erro de Validação", f"Verifique os dados informados:\n{e}")

    def acao_excluir(self):
        matricula = self.entry_matricula.get().strip()
        if not matricula:
            messagebox.showwarning("Aviso", "Informe a matrícula do aluno que deseja excluir.")
            return
            
        confirmacao = messagebox.askyesno("Confirmar", f"Tem certeza que deseja excluir a matrícula {matricula}?")
        if confirmacao:
            sucesso = self.dao.excluir(matricula)
            if sucesso:
                messagebox.showinfo("Sucesso", "Aluno excluído com sucesso!")
                self.limpar_campos()
                self.acao_listar_todos()
            else:
                messagebox.showerror("Erro", "Aluno não encontrado.")

    def acao_listar_todos(self):
        alunos = self.dao.listar()
        self._atualizar_tabela(alunos)

    def acao_pesquisar_matricula(self):
        matricula = self.entry_matricula.get().strip()
        if not matricula:
            messagebox.showwarning("Aviso", "Informe a matrícula para pesquisar.")
            return
            
        aluno = self.dao.obter_por_matricula(matricula)
        if aluno:
            self._atualizar_tabela([aluno])
        else:
            self._atualizar_tabela([])
            messagebox.showinfo("Pesquisa", "Nenhum aluno encontrado com esta matrícula.")

    def acao_pesquisar_nome(self):
        nome = self.entry_nome.get().strip()
        if not nome:
            messagebox.showwarning("Aviso", "Informe um nome para pesquisar.")
            return
            
        alunos = self.dao.obter_por_nome(nome)
        self._atualizar_tabela(alunos)
        if not alunos:
            messagebox.showinfo("Pesquisa", "Nenhum aluno encontrado com este nome.")