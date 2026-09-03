# Galeria de Produtos - Setup Correto

## 📋 Resumo

Agora temos os dados corretos do Excel com:
- **98 categorias** (IDs: 2, 7, 9, 12, 14, 16, ... 190)
- **98 imagens** (uma para cada categoria)
- **URLs corretas** do Netlify

## Estrutura Final do Repositório

```
validacao-imagens-catalogo/
├── index.html                     (galeria em produção - URLs externas)
├── index_local_netlify.html       (galeria com URLs do Netlify)
├── download_images.py             (script para baixar as 98 imagens)
├── images/                        (pasta com 98 imagens)
│   ├── img_2.jpg      (categoria 2)
│   ├── img_7.jpg      (categoria 7)
│   ├── img_9.jpg      (categoria 9)
│   └── ... até img_190.jpg
└── README.md
```

## 🚀 Passo a Passo

### 1. Preparar o Repositório

Coloque os seguintes arquivos na raiz do projeto:
- `download_images.py`
- `index_local_netlify.html`

### 2. Executar o Download

Na sua máquina (fora da VM Cowork):

```bash
cd ~/Projects/validacao-imagens-catalogo
python3 download_images.py
```

**O que acontece:**
- Cria pasta `images/` automaticamente
- Baixa as 98 imagens com os nomes corretos:
  - `img_2.jpg`, `img_7.jpg`, `img_9.jpg`, etc.
- Mostra progresso e resumo final

**Tempo estimado:** 3-5 minutos

### 3. Testar Localmente

Abra a galeria no navegador:

```bash
open index_local_netlify.html
```

Ou use um servidor local:

```bash
python3 -m http.server 8000
# Acesse: http://localhost:8000/index_local_netlify.html
```

**A galeria carregará as imagens do Netlify:**
```
https://validacao-imagens-catalogo.netlify.app/images/img_2.jpg
https://validacao-imagens-catalogo.netlify.app/images/img_7.jpg
... etc
```

### 4. Fazer Commit e Push

Após validar as imagens:

```bash
# Ver status
git status

# Adicionar tudo
git add .

# Commit
git commit -m "Adicionar 98 imagens com categorias corretas

- Imagens nomeadas por ID de categoria (img_2.jpg, img_7.jpg, etc.)
- index_local_netlify.html referencia URLs do Netlify
- Todas as 98 categorias do Excel"

# Push
git push origin main
```

Netlify fará deploy automaticamente! 🎉

### 5. Verificar no Netlify

Após o push, a galeria estará disponível em:
- **Live:** https://validacao-imagens-catalogo.netlify.app/index_local_netlify.html

Ou renomeie o arquivo se quiser como página padrão:

```bash
# Opcionalmente:
mv index.html index_external.html
mv index_local_netlify.html index.html
git add .
git commit -m "Usar galeria com URLs Netlify como padrão"
git push origin main
```

## 📊 Dados Corretos

Total de categorias: **98**

Primeiras 10 categorias: 2, 7, 9, 12, 14, 16, 18, 20, 23, 24
Últimas 10 categorias: 155, 157, 159, 161, 164, 166, 168, 171, 173, 176, 178, 181, 183, 185, 186, 188, 190

## ✅ Checklist

- [ ] Baixar `download_images.py` e `index_local_netlify.html`
- [ ] Colocar na raiz do projeto `validacao-imagens-catalogo/`
- [ ] Executar `python3 download_images.py`
- [ ] Verificar se `images/` foi criada com 98 arquivos
- [ ] Testar `index_local_netlify.html` localmente
- [ ] Fazer `git add .` e `git commit`
- [ ] Fazer `git push origin main`
- [ ] Verificar deploy no Netlify

## 🔗 URLs das Imagens

Padrão: `https://validacao-imagens-catalogo.netlify.app/images/img_{CATEGORIA}.jpg`

Exemplos:
- `https://validacao-imagens-catalogo.netlify.app/images/img_2.jpg`
- `https://validacao-imagens-catalogo.netlify.app/images/img_7.jpg`
- `https://validacao-imagens-catalogo.netlify.app/images/img_190.jpg`

---

**Pronto!** As imagens estão organizadas corretamente e o index referencia as URLs do Netlify! 🎨
