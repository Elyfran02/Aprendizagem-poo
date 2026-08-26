# 1. Padrões de Nomenclatura Utilizados: PEP 8

Para garantir a legibilidade, consistência e manutenibilidade do código, este projeto adota estritamente a **PEP 8** (Python Enhancement Proposal 8), que é o guia de estilo oficial e o padrão universalmente aceito pela comunidade para a escrita de código em Python.

A PEP 8 define convenções claras sobre como nomear diferentes estruturas dentro do sistema, baseando-se na premissa de que "o código é lido com muito mais frequência do que escrito". Os padrões adotados na nossa aplicação são:

* **Arquivos Fontes (Módulos):** Devem utilizar o padrão `snake_case` (letras minúsculas separadas por sublinhado). Arquivos devem ter nomes curtos e descritivos.
* *Exemplos:* `gui.py`, `aluno_dao.py`, `aluno.py`.


* **Classes:** Devem utilizar o padrão `PascalCase` (também conhecido como *UpperCamelCase*, onde a primeira letra de cada palavra é maiúscula e não há separadores).
* *Exemplos:* `Aluno`, `AlunoDAO`, `AlunoGUI`.


* **Atributos e Variáveis:** Devem utilizar o padrão `snake_case`.
* *Exemplos:* `data_nascimento`, `matricula`, `novo_aluno`.


* **Métodos e Funções:** Também devem seguir estritamente o padrão `snake_case`, indicando ações de forma clara. 
* *Exemplos:* `calcular_imc()`, `inserir()`, `obter_por_nome()`.

* **Atributos/Métodos Internos (Privados):** Em Python, o encapsulamento é feito por convenção. Métodos ou atributos que não devem ser acessados fora da própria classe recebem um *underscore* (sublinhado) no início do nome.
* *Exemplos:* `_ler_formulario()`, `_atualizar_tabela()`.