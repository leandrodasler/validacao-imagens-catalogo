# Validação de imagens do catálogo

Galeria estática para conferir as imagens do catálogo, uma por categoria.
Produção: https://validacao-imagens-catalogo.netlify.app/

## Rodar localmente

```bash
python3 -m http.server 8000
# http://localhost:8000
```

## Estrutura

| Arquivo | Função |
|---|---|
| `index.html` | Galeria com a relação dos produtos, filtro por categoria e botão de copiar URL |
| `images/` | Imagens (`img_<categoria>.<ext>`), trocadas direto na pasta |
| `netlify.toml` | Configuração de publicação, cache e headers |

## Fluxo de mudança

1. Criar uma branch e fazer as alterações (imagens em `images/`, relação em `index.html`).
2. Abrir um PR: o Netlify gera um Deploy Preview para validar.
3. Merge na `main` publica em produção.

Veja o `CLAUDE.md` para convenções e pendências.
