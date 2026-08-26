# Tutorial: Criação, Estruturação e Execução de Projetos em Python

Este guia definitivo apresenta o passo a passo para iniciar, configurar e executar um novo projeto em Python, adotando as melhores práticas do mercado. O objetivo é garantir que seu projeto seja isolado, organizado e facilmente reproduzível.

> ATENÇÃO: Todas as instruções do Sistema Operacioal Windows serão
> realizadas através de linha de comando no Prompt de Comando - CMD 

## 1. Criação do Diretório Base

O primeiro passo é criar a pasta raiz onde todo o seu código e configurações irão residir. Nunca misture projetos diferentes na mesma pasta.

> No Windows, abrir a janela do CMD: Prompt de comando

**Comandos no Terminal: Prompt de comando**
```bash
cd\
mkdir projeto_01
cd projeto_01

```
**Verificar a Versão do Python Instalada:**
> Local no CMD -> c:\projeto_01>
```bash
python --version

```

## 2. Criação do Ambiente Virtual (venv)

Um Ambiente Virtual (Virtual Environment - venv) é uma instalação isolada do Python. Ele garante que as bibliotecas e versões que você utilizar neste projeto não interfiram no Python global do seu sistema operacional.

**Comando:**
> Local no CMD -> c:\projeto_01>
```bash
python -m venv venv

```

*(Nota: O segundo "venv" é o nome da pasta que será criada. É uma convenção da comunidade chamá-la de `venv`)*

---

## 3. Ativação do Ambiente Virtual

Antes de instalar bibliotecas ou rodar o código, você **precisa** ativar o ambiente virtual. Você saberá que deu certo quando a tag `(venv)` aparecer no início da linha do seu terminal.

**No Windows (Prompt de Comando):**
> Local no CMD -> c:\projeto_01>
```bash
venv\Scripts\activate.bat

```
> A partir da Ativação do Ambiente Virtual, o prompt do CMD fica: 
> (venv) C:\projeto_01>

**No Linux ou macOS:**

```bash
source venv/bin/activate

```

---

## 4. Estrutura de Arquivos Inicial

Com o ambiente ativado, crie os arquivos essenciais. Um projeto bem estruturado separa configurações, código-fonte e documentação.

Para criar os arquivos pelo terminal, você pode usar seu editor de código (como o VS Code: `code .`) ou criar manualmente a seguinte estrutura:

* **`main.py`** ou **`app.py`**: O arquivo principal, ponto de entrada da sua aplicação.
* **`README.md`**: Arquivo de texto explicando o que é o projeto e como rodá-lo.
* **`requirements.txt`**: Lista das bibliotecas externas necessárias para o projeto.
* **`src/`** *(pasta opcional, mas recomendada)*: Onde você colocará todos os outros módulos, classes e pacotes do seu sistema.

A estrutura final que vamos criar ficará com esta aparência:
> Local no CMD -> (venv) C:\projeto_01>
> projeto_01/
> ├── README.md
> ├── requirements.txt
> ├── documentos/
> ├── venv/
> ├── main.py 
> ├── src/
> │   ├── __init__.py
> └── tests/
> └── test_main.py

## 4.1. Criar a Estrutura do Diretório 

> Local no CMD -> (venv) C:\projeto_01>

**Criar os Diretórios: src e tests**
```bash
mkdir src documentos tests
```
**Gerar os arquivos essenciais**
```bash
echo. > README.md
```

```bash
echo. > main.py
```

```bash
echo. > requirements.txt
```

```bash
echo. > src/__init__.py
```

```bash
echo. > tests/__init__.py
```

```bash
echo. > tests/test_main.py
```

## 4.2. Abrir o VS Code no Diretório de trabalho:
> Local no CMD -> c:\projeto_01>
```bash
code .
```

## 4.3. O Arquivo `__init__.py`
O arquivo __init__.py (lido como dunder init, abreviação de "double underscore") tem um papel histórico e arquitetural fundamental no Python.
Em termos simples, ele diz ao Python que a pasta onde ele está localizado não é apenas uma pasta comum do Windows ou Linux, mas sim um "Pacote Python" (Package).
Embora ele muitas vezes fique completamente vazio no projeto, a presença ou o código contido nele serve para três objetivos principais:

* **Sinalizador de Pacote (Transformar Pasta em Módulo):** Sempre que você usa o comando import, o Python começa a vasculhar os diretórios procurando o que importar. Se você tem uma pasta chamada src com vários arquivos .py dentro, o __init__.py avisa ao interpretador: "Pode entrar aqui, esta pasta é um pacote oficial do nosso sistema".

* **4.1.2 Nota Histórica:**  Antes do Python 3.3, se uma pasta não tivesse o __init__.py, o Python se recusava a importar qualquer coisa de dentro dela. Hoje o Python até consegue ler pastas sem ele (chamados de Namespace Packages), mas a regra de ouro do mercado é sempre criá-lo para evitar comportamentos inesperados.

* **Inicialização Automática:** Como o nome "init" sugere, qualquer código escrito dentro deste arquivo será executado automaticamente na primeira vez que o pacote for importado em algum lugar.
Você pode usá-lo para iniciar uma conexão com o banco de dados, configurar logs ou carregar variáveis de ambiente assim que o seu sistema for "ligado".

* **O "Atalho" de Importações (Uso Mais Poderoso):** Este é o uso avançado mais comum. Em projetos grandes, os arquivos ficam muito aninhados. O __init__.py pode agrupar as importações para facilitar a vida de quem vai usar o seu código.

---

## 5. Gerenciamento de Dependências

Se o seu projeto precisar de bibliotecas que não vêm na instalação padrão do Python, utilize o gerenciador `pip`.

**Para instalar uma biblioteca (exemplo):**

```bash
pip install requests

```

**Para salvar as dependências:**
Sempre que instalar algo novo, atualize o seu arquivo `requirements.txt`.

```bash
pip freeze > requirements.txt

```

**Para instalar dependências de um projeto clonado/baixado:**

```bash
pip install -r requirements.txt

```

---

## 6. Controle de Versão (Git)

Inicie o Git para versionar o seu código. É vital garantir que a pasta do ambiente virtual (`venv/`) **não** seja enviada para o seu repositório (GitHub, GitLab), pois ela é gerada localmente.

**Comandos:**

```bash
git init
echo "venv/" > .gitignore
git add .
git commit -m "Commit inicial: Estrutura base do projeto"

```

---

## 7. Como Executar o Projeto

Para executar qualquer script Python, você deve usar o interpretador chamando o arquivo desejado. Siga estas regras sempre que for testar ou rodar a aplicação:

**Passo 7.1: Verifique o Ambiente Virtual**
Certifique-se de que o seu terminal está com o ambiente virtual ativado (o texto `(venv)` deve estar visível). Se não estiver, repita o **Passo 3**.

**Passo 7.2: Execute o arquivo principal**
Digite a palavra `python` seguida do nome do arquivo que contém a lógica principal de inicialização do seu sistema.

Se o seu arquivo principal se chama `main.py`:

```bash
python main.py

```

Se o ponto de entrada for a interface gráfica (como no nosso projeto de CRUD de Alunos, onde o arquivo principal é o `gui.py`):

```bash
python gui.py

```

**Dica de Especialista:** Caso o seu arquivo esteja dentro de uma pasta como `src`, você deve passar o caminho completo relativo a partir da raiz:

```bash
python src/main.py

```

---

## Resumo do Fluxo de Trabalho Diário

Toda vez que você for trabalhar neste projeto novamente no dia seguinte, o fluxo deve ser apenas este:

1. Abra o terminal na pasta do projeto.
2. Ative o ambiente virtual.
3. Escreva seu código.
4. Rode a aplicação (`python seu_arquivo.py`).