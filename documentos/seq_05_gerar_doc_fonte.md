# Gerar Documentação do Código Fonte

A extensão `autoDocstring` é excelente porque ela cria a "matéria-prima" da sua documentação diretamente no código. Agora que o seu código está cheio de blocos `"""`, você precisa de uma ferramenta externa (um gerador de documentação) que vai ler esses textos e transformá-los em uma página web (HTML) bonita e navegável.

Uma das principais ferramentas no ecossistema Python para fazer isso e  mais rápida é `pdoc`.

---

## A Opção Mais Rápida: `pdoc` (Zero Configuração)

Se você quer gerar a documentação **agora mesmo**, sem precisar configurar arquivos complexos, o `pdoc` é a melhor escolha. Ele lê seus arquivos e gera um site HTML instantaneamente, entendendo perfeitamente o formato gerado pelo `autoDocstring`.

**Passo a passo:**

1. Abra o terminal (com seu ambiente virtual ativado) e instale a biblioteca:
```bash
pip install pdoc

```

2. Execute o `pdoc` apontando para o seu arquivo principal ou pasta. Se o seu código estiver em um arquivo chamado `aluno.py`, digite:
```bash
pdoc aluno.py

```

*(Se você tiver uma pasta chamada `src` com vários arquivos, basta digitar `pdoc src/`).*

3. **O resultado:** O `pdoc` vai subir um servidor local e abrir o seu navegador automaticamente com um site contendo toda a documentação das suas classes, métodos e parâmetros organizados lindamente.

4. **Para exportar (salvar em HTML):** Se você quiser salvar os arquivos gerados para mandar para alguém, adicione a flag `-o` (output) e o nome de uma pasta:
```bash
pdoc aluno.py -o docs/

```
Isso criará uma pasta chamada `docs` com os arquivos HTML prontos.

5. **Para exportar (salvar em HTML) do Projeto_01:** Se você quiser salvar a documentação de todos os arquivos da pasta ***src*** para a pasta ***documentos*** do Projeto_01 basta executar o seguinte comando:
```bash
pdoc src/ -o documentos

```

