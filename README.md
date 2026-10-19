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
| `catalog.json` | Dados do catálogo (categoria, nome, URL de origem, imagem local) |
| `index.html` | Galeria com filtro por categoria e botão de copiar URL |
| `images/` | Imagens locais (`img_<categoria>.<ext>`) |
| `download_images.py` | Baixa as imagens que faltam (`--dry-run`, `--force`) |
| `netlify.toml` | Configuração de publicação, cache e headers |

## Fluxo de mudança

1. Criar uma branch e fazer as alterações (dados em `catalog.json`).
2. Abrir um PR: o Netlify gera um Deploy Preview para validar.
3. Merge na `main` publica em produção.

Veja o `CLAUDE.md` para convenções e pendências.
