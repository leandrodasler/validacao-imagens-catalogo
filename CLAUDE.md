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
- Todas as imagens de `images/` devem ser `.jpg` (conteúdo JPEG de verdade, não só a extensão), mantendo o nome
  `img_<categoria>.jpg`. Converter webp/png/gif antes de adicionar (achatar transparência sobre fundo branco).
  Assim o campo `image` do `index.html` não precisa mudar ao trocar uma imagem.
- Manter apenas `index.html` e `images/` como conteúdo do site: sem scripts auxiliares nem dados em arquivos separados.

## Convenções

- Sem dependências nem build. Única exceção: as fontes Inter e JetBrains Mono vêm do Google Fonts (com fallback para fontes do sistema).
- **Todo texto exibido na página deve estar em inglês** (interface, estados, mensagens, tooltips, `lang="en"`).
- Montar o DOM com `textContent`/`createElement` (nomes de produto contêm aspas, ex.: `3/8"-16`).
- O site é interno e não deve ser indexado.

## Visual (referência: dashboard "Tendra")

- Tokens de cor e fonte ficam em `:root` no `index.html`; reutilizar em vez de criar cores novas.
- Fundo externo cinza claro, painel branco arredondado (28px), cards com borda `--line` e raio 16-20px.
- Texto em Inter; rótulos pequenos em JetBrains Mono maiúsculo com espaçamento (`.label`, `.chip`).
- Chips coloridos: cinza (neutro), azul, âmbar (pendente), verde (ok). Botão primário escuro, secundários brancos com borda.
- Cards de resumo com barras segmentadas (`.bars`); estado vazio/pendente com borda tracejada.

## Pendências conhecidas

- Categorias 41, 102 e 183 estão sem imagem (`image: null`); a galeria mostra "Imagem pendente".
