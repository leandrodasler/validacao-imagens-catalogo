# validacao-imagens-catalogo

Galeria estática para validar visualmente as imagens do catálogo (uma imagem por categoria).
Publicada no Netlify: https://validacao-imagens-catalogo.netlify.app/ (deploy automático a partir da `main`).

## Estrutura

- `index.html` — galeria (HTML/CSS/JS puro, sem build). Contém a relação dos produtos no array
  `products` (`{ category, name, path, products, skus, image }`), usado para a pesquisa por categoria.
  `name` e `path` vêm da árvore de categorias da VTEX (fonte da verdade, conta `demoindsupply`).
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

## Nomes das categorias (VTEX)

- O `category` é o ID da categoria na VTEX. `name` é o nome da categoria e `path` o caminho completo (ex.: `Safety > Eye Protection > Safety Glasses`).
- API pública (somente leitura, sem autenticação):
  `GET https://demoindsupply.vtexcommercestable.com.br/api/catalog_system/pub/category/tree/5`
- Ao mudar de conta ou se a árvore mudar, refazer `name`/`path` a partir dessa API; não editar nomes à mão.
- A imagem de cada categoria deve representar a categoria da VTEX (o nome mostrado), não outro produto.

## Contagem de produtos e SKUs (VTEX)

- `products` é **exato**: header `resources` de `GET /api/catalog_system/pub/products/search?fq=C:/<ids do caminho>/&_from=0&_to=0`
  (o filtro exige o caminho completo de IDs, ex.: `C:/5/6/7/`; inclui subcategorias).
- `skus` é uma **estimativa** (exibida com `~`): 3 páginas de 50 produtos espalhadas nos primeiros 2.500 resultados (limite de offset da busca),
  média de SKUs dos produtos ligados *diretamente* à categoria × produtos diretos, somada às subcategorias.
- A busca pública só enxerga produtos ativos/visíveis na vitrine. SKUs exatos exigem a Catalog API privada (AppKey/AppToken).
- É um snapshot (data no rodapé da página); refazer a coleta se o catálogo mudar. O script de coleta não fica no repositório.

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

- A galeria lista as 190 categorias da VTEX (inclusive as de topo e intermediárias). Só 95 têm imagem; as demais (`image: null`) aparecem como "Pending image".
- Muitas imagens atuais foram feitas para os nomes antigos e podem não representar a categoria da VTEX; revisar uma a uma.
