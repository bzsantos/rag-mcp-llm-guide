# Código-fonte do livro — Desenvolvimento de Sistemas Inteligentes com RAG e MCP

Este repositório contém todo o código do livro, organizado de duas formas complementares:

## 📁 `capitulos/`

Um diretório por capítulo (`capitulo-01-...` até `capitulo-28-...`), contendo **exatamente** os
arquivos, scripts e comandos apresentados naquele capítulo — na mesma ordem em que aparecem no
livro. Use esta pasta se você está lendo o livro capítulo a capítulo e quer conferir seu código
contra o que foi escrito ali.

Cada pasta de capítulo pode conter:

- `src/assistente_corporativo/...` — arquivos da aplicação backend introduzidos ou alterados naquele capítulo.
- `src/...` (nos capítulos de front-end) — arquivos do projeto React.
- `comandos.sh` — todos os comandos de terminal usados no capítulo (instalação de pacotes, Docker, etc.), na ordem em que aparecem.
- `testes.http` — as requisições de teste do capítulo, prontas para rodar com a extensão **REST Client** do VS Code.
- `trechos_ilustrativos.md` — pequenos trechos de código mostrados no texto sem um arquivo-alvo específico (exemplos conceituais, variações mostradas em caixas de destaque).

> ⚠️ Como o livro ensina a construir a aplicação **incrementalmente** (o mesmo arquivo é criado em
> um capítulo e ampliado nos seguintes), alguns arquivos aparecem em mais de uma pasta de capítulo,
> cada vez com o conteúdo daquele momento. Isso é proposital — acompanha exatamente a progressão do livro.

## 📁 `projeto-final/`

A aplicação **completa e consolidada**, já com todos os capítulos aplicados — pronta para clonar,
instalar e rodar. Se você quer o resultado final funcionando (não a jornada capítulo a capítulo),
comece por aqui. Veja `projeto-final/README.md` para instruções de execução.

- `projeto-final/backend/` — API FastAPI completa (RAG + MCP + Auth + Testes).
- `projeto-final/frontend/` — Interface React completa.

## Como usar com o GitHub

Sugestão de organização ao subir para o GitHub:

```
seu-repositorio/
├── capitulos/          (copie a pasta capitulos/ inteira)
├── backend/             (copie o conteúdo de projeto-final/backend/)
├── frontend/             (copie o conteúdo de projeto-final/frontend/)
└── README.md             (este arquivo, ou um personalizado)
```

Ou, se preferir manter a estrutura exatamente como está aqui, basta arrastar a pasta
`codigo_extraido/` inteira para dentro de um novo repositório Git:

```bash
cd codigo_extraido
git init
git add .
git commit -m "Código-fonte do livro: Desenvolvimento de Sistemas Inteligentes com RAG e MCP"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
git push -u origin main
```
