# Para Visualizar o arquivo do tipo Markdown (.md): Ctrl + Shift + V

# Instalar Extensões no VS Code: Ctrl+Shift+X

> OBJETIVO: Preparação do Ambiente de Desenvolvimento

# 1. O "Coração" do Python (Obrigatórias)

Estas são as extensões oficiais da Microsoft e formam a base do desenvolvimento Python no VS Code.

* **Python (por Microsoft):** É a extensão principal. Ela permite que o VS Code encontre o seu Ambiente Virtual (`venv`), execute o seu código e integre as ferramentas de teste.
* **Pylance (por Microsoft):** É o "cérebro" do IntelliSense. Como nós usamos *Type Hints*, o Pylance vai ler isso e avisar em tempo real a tipagem dos atributos, autocompletando seus métodos com perfeição.
* **Python Debugger (por Microsoft):** Essencial para debugar o código. Permite colocar *breakpoints* (pontos de parada vermelhos) para você ver os dados transitando nas variáveis linha por linha sem precisar encher o código de `print()`.

# 2. Qualidade de Código e Formatação

Essas extensões vão formatar e corrigir seu código automaticamente.

* **Ruff (por Astral Software):** Esta é a recomendação mais moderna. O Ruff substitui ferramentas antigas (como Flake8, Black e isort). Ele é escrito em Rust e é absurdamente rápido. Se você der espaços errados ou importar bibliotecas e não usar, o Ruff vai sublinhar e, em muitos casos, consertar sozinho ao salvar o arquivo.
* **Mypy Type Checker (por Microsoft):** Se você quer programar Python profissionalmente, o Mypy é seu melhor amigo. Ele é um verificador de tipos rigoroso. Ele garante que a sua arquitetura Orientada a Objetos não tenha "furos" de tipagem.

# 3. Ferramentas Auxiliares para o Nosso Projeto

Principais ferramentas utilizadas para o desenvolvimento dos Projetos:

* **SQLite Viewer (por Florian Klampfer):** Visualiza um banco de Dados Local SQLite, sem precisar baixar um software de banco de dados externo.
* **autoDocstring (por Nils Werner):** Como estamos construindo classes, documentar os métodos é crucial. Com essa extensão, basta você digitar `"""` embaixo de um `def` e dar *Enter*; ela gera automaticamente um bloco de documentação no formato padrão preenchendo os parâmetros para você.
* **Markdown All in One (por Yu Zhang):** O objetivo da extensão é transformar o VS Code em um editor Markdown de alta produtividade. Ela agrupa (daí o nome "All in One") todas as funcionalidades essenciais que faltam no VS Code nativo, automatizando tarefas repetitivas de formatação para que você possa focar apenas no conteúdo do seu texto.
* **Markdown Preview Enhanced (por Yiyi Wang):** O principal objetivo da extensão é elevar a visualização de arquivos Markdown no VS Code a um nível acadêmico e profissional. Enquanto o visualizador nativo do VS Code é básico e focado apenas em formatação de texto simples, a versão "Enhanced" (Melhorada) transforma o seu editor em uma plataforma de publicação completa. O objetivo dela é permitir que você escreva documentos complexos — contendo fórmulas matemáticas, apresentações de slides e, principalmente, gráficos dinâmicos — sem nunca precisar sair do VS Code.
Gráficos de Arquitetura e Engenharia de Software
Mermaid: Renderiza Fluxogramas, Diagramas de Classe (UML), Diagramas de Sequência, Diagramas de Estado, Gráficos de Gantt (para cronogramas) e Gráficos de Pizza.
PlantUML: Suporta diagramas UML avançados (Casos de Uso, Implantação, Componentes) e diagramas de arquitetura de rede.
Graphviz (Linguagem DOT): Excelente para gerar diagramas de redes de computadores, organogramas corporativos e gráficos direcionados (nós e arestas interligados).
* **Mermaid - Mermaid Chart (por mermaidchart.com):** O objetivo principal das extensões focadas em Mermaid no VS Code (como a Mermaid Markdown Syntax Highlighting ou a Mermaid Preview) é trazer a filosofia de "Diagramas como Código" (Diagrams as Code) para dentro do seu editor, permitindo que você crie representações visuais complexas usando apenas texto simples. Embora o Markdown Preview Enhanced (que discutimos antes) já consiga renderizar o Mermaid, as extensões dedicadas puramente ao Mermaid servem para melhorar a sua experiência de escrita desses diagramas.
* **vscode-pdf (por tomoki1207):** Permitir a leitura e visualização de arquivos PDF diretamente dentro da interface do Visual Studio Code, sem que você precise abrir programas externos. 

---

**Como instalar tudo rapidamente:**
Basta abrir a aba de Extensões (`Ctrl+Shift+X`), digitar o nome da Extensão e clicar em "Install".