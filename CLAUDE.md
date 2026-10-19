# validacao-imagens-catalogo

Galeria estática para validar visualmente as imagens do catálogo (uma imagem por categoria).
Publicada no Netlify: https://validacao-imagens-catalogo.netlify.app/ (deploy automático a partir da `main`).

## Estrutura

- `catalog.json` — **fonte única dos dados**. Lista de `{ category, name, sourceUrl, image }`.
  `image` é o caminho local (`images/img_<categoria>.<ext>`) ou `null` se ainda não foi baixada.
- `index.html` — galeria (HTML/CSS/JS puro, sem build). Carrega `catalog.json` via `fetch`.
- `images/` — imagens locais, nomeadas por categoria.
- `download_images.py` — baixa para `images/` o que falta no catálogo e atualiza o `catalog.json`.
- `netlify.toml` — publica a raiz, define cache e `noindex`.

## Como trabalhar

- Nunca commitar direto na `main`: criar branch, abrir PR e validar no Deploy Preview do Netlify.
- Rodar localmente (o `fetch` não funciona via `file://`):
  `python3 -m http.server 8000` e abrir http://localhost:8000
- Para adicionar/alterar uma categoria: editar só o `catalog.json` (e rodar `download_images.py`).
  Não duplicar dados no HTML nem no script.
- `catalog.json` é formatado com 2 espaços e termina com newline.

## Convenções

- Sem dependências nem build: manter HTML/JS/Python da biblioteca padrão.
- Textos da interface em português (pt-BR).
- Montar o DOM com `textContent`/`createElement` (nomes de produto contêm aspas, ex.: `3/8"-16`).
- Baixar imagens de terceiros só quando o usuário pedir; o site é interno e não deve ser indexado.

## Pendências conhecidas

- Categorias 41, 102 e 183 estão sem imagem local (`image: null`); a galeria mostra "Imagem pendente".
- Categoria 155 tinha duas URLs na lista original; o catálogo guarda a segunda (a que o script antigo deixava prevalecer).
