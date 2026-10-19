# validacao-imagens-catalogo

Galeria estática para validar visualmente as imagens do catálogo (uma imagem por categoria).
Publicada no Netlify: https://validacao-imagens-catalogo.netlify.app/ (deploy automático a partir da `main`).

## Estrutura

- `index.html` — galeria (HTML/CSS/JS puro, sem build). Contém a relação dos produtos no array
  `products` (`{ category, name, image }`), usado para a pesquisa por categoria.
  `image` é o caminho (`images/img_<categoria>.<ext>`) ou `null` se a imagem está pendente.
- `images/` — imagens, nomeadas por categoria. As imagens são trocadas direto nessa pasta.
- `netlify.toml` — publica a raiz, define cache e `noindex`.

## Como trabalhar

- Nunca commitar direto na `main`: criar branch, abrir PR e validar no Deploy Preview do Netlify.
- Rodar localmente: `python3 -m http.server 8000` e abrir http://localhost:8000
- Ao trocar uma imagem por outra de extensão diferente, atualizar o campo `image` do produto
  em `index.html` (e remover o arquivo antigo de `images/`).
- Manter apenas `index.html` e `images/` como conteúdo do site: sem scripts auxiliares nem dados em arquivos separados.

## Convenções

- Sem dependências nem build.
- Textos da interface em português (pt-BR).
- Montar o DOM com `textContent`/`createElement` (nomes de produto contêm aspas, ex.: `3/8"-16`).
- O site é interno e não deve ser indexado.

## Pendências conhecidas

- Categorias 41, 102 e 183 estão sem imagem (`image: null`); a galeria mostra "Imagem pendente".
