#!/usr/bin/env python3
"""
Script para baixar 98 imagens do catálogo
Execute este script na pasta raiz do seu projeto:
  python3 download_images.py

Estrutura esperada:
  validacao-imagens-catalogo/
  ├── index.html (já existe)
  ├── index_local.html (galeria com URLs Netlify)
  ├── download_images.py (este arquivo)
  └── images/ (será criada)

As imagens serão nomeadas pelo ID da CATEGORIA:
  img_2.jpg, img_7.jpg, img_9.jpg, img_12.jpg, etc.
"""

import urllib.request
import os
import time
from pathlib import Path

# Dados extraídos do Excel: (categoria, url)
IMAGES = [
    (2, "https://contentinfo.autozone.com/znetcs/product-info/en/US/avp/5469/image/8/"),
    (7, "https://static-content.cromwell.co.uk/images/854_854/g/jeeps/960/ctl9600111m.jpg"),
    (9, "https://i5.walmartimages.com/seo/Supmedic-Blue-Nitrile-Exam-Gloves-5-mil-Powder-Free-Latex-Free-Food-Safe-Disposable-Medical-Glove-100-Pcs-Large_31c409b2-8318-41e7-8788-466f2f83b53a.168caccd2b25f80254c8cd03e31a775d.jpeg"),
    (12, "https://static.wixstatic.com/media/133823_0cd2dbe2718e4d5bbf45c50c0536a196~mv2.png/v1/fill/w_500,h_500,al_c,q_85,enc_auto/133823_0cd2dbe2718e4d5bbf45c50c0536a196~mv2.png"),
    (14, "https://wcsafety.com/cdn/shop/files/3m-peltor-optime-98-h9a-earmuffs-nrr-25-over-the-h_800x.jpg?v=1782295626"),
    (16, "https://img.uline.com/is/image/uline/S-21682G-L_US?$LargeRHD$"),
    (18, "https://hoffmanboots.com/cdn/shop/files/2008-09-09_12.12.01.jpg?v=1775582114&width=1946"),
    (20, "https://images.globalindustrial.com/images/co/761290IN_1wco.gif?t=1664286141901"),
    (23, "https://mobileimages.lowes.com/product/converted/820909/820909502173.jpg"),
    (24, "https://i5.walmartimages.com/seo/Craftsman-8-Piece-Assorted-Screwdriver-Set_43a7bf24-c62e-4925-991a-f32dd613e7e0.d0b2de67227b35ebffa7a4417654f8ce.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF"),
    (25, "https://2e1293630802db8d0d56-50fcdb1c10e3e49a3d1b0541a2f13b69.ssl.cf1.rackcdn.com/product/images/f34aa598939141a09445d37f170b8330.jpg"),
    (27, "https://i5.walmartimages.com/seo/Deli-10-inch-Curved-Jaw-Locking-Pliers-Vice-Grips-Plier-with-Wire-Cutter-Locking-Adjustable-Vise-Grips-for-Clamping-Twisting-Welding_2c3461b8-1711-41e3-b479-fba3a6a3834d.e21b6f6dd6015498ba5029dde66c4df9.jpeg"),
    (28, "https://media-www.canadiantire.ca/product/fixing/tools/cutting-measuring/0577165/fatmax-25-magnetic-tip-tape-a3ae92c1-76c7-4dad-b5f0-8e3e1c683599-jpgrendition.jpg"),
    (29, "https://cdn11.bigcommerce.com/s-l73l7lwqjy/images/stencil/1280x1280/products/1320/8198/digital_caliper7__28099.1675286157.jpg?c=2&imbypass=on"),
    (30, "https://i5.walmartimages.com/seo/Hyper-Tough-16-Ounce-Claw-Hammer-with-Fiberglass-Handle_e0d866aa-7cd2-4d51-ad90-ce9a7e22eb88_1.58cc82e01710cb54ba43045117563858.jpeg"),
    (31, "https://microless.com/cdn/products/9d59b0223728d5c0ec5e3a7045123071-hi.jpg"),
    (33, "https://www.kleintools.com/sites/default/files/product-assets/catalog-imagery/original/klein/ls12_bls12_locked_alt1.jpg"),
    (34, "https://m.media-amazon.com/images/I/717HkNqIFCL.jpg"),
    (35, "https://www.toolhavenusa.com/wp-content/uploads/2025/08/8400349036696_710026.webp"),
    (36, "https://i5.walmartimages.com/seo/SKIL-SPT77W-01-15-Amp-7-1-4-Aluminum-Corded-Electric-Worm-Drive-Circular-Saw_e5ba1bd4-d126-4e99-bfe7-77becf12084d_1.9d47e6060ac4a4b9c3b4c4e0253bed55.jpeg"),
    (39, "https://i5.walmartimages.ca/images/Enlarge/422/058/1422058.jpg"),
    (41, "https://0295-cdn.dib-moce-cdn.info/Data/ItemImage-501980-q5w87j-870zpk-5l5tsg.jpg?AutoCrop=1&CropHeight=1440&CropWidth=1440&Height=1440&Padding=1&Quality=50&Resize=Auto&Revision=g4CG&Timestamp=g9dsFG&Width=1440"),
    (43, "https://cdn.mscdirect.com/global/images/ProductImages/9721370-21.jpg"),
    (45, "https://www.resllcstore.com/cdn/shop/files/IMG_0005-Photoroom_390a9b4f-d1cd-4270-96dd-7b2974561b45.jpg?v=1731021881&width=1445"),
    (47, "https://i5.walmartimages.com/seo/4-Pack-LED-Shop-Light-for-Garage-4ft-Linkable-5000K-Daylight-40W-Surface-Mount-Suspended-Mount_852a2840-198e-4814-977e-e3df5c317e46.983d99433ab2288edfed56325e6ac236.jpeg"),
    (49, "https://zuniposimages.blob.core.windows.net/posimages/17190_000_001.jpg"),
    (51, "https://m.media-amazon.com/images/I/81Gvp15P4FL.jpg"),
    (52, "https://images-na.ssl-images-amazon.com/images/I/71oomjybNyL.jpg"),
    (54, "https://i5.walmartimages.com/seo/ENERLITES-20-Amp-Heavy-Duty-Toggle-Light-Switch-Single-Pole-20A-120-277V-Grounding-Screw-Commercial-Grade-UL-Listed-81201-W-White_1efeeea4-3ba6-4429-b6e4-467d411bce0c.076d8e9e0585d38259283be852f942e7.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF"),
    (56, "https://assets.wfcdn.com/im/03269543/compr-r85/3793/379303615/Red+Letter+Led+Exit+Sign+With+Battery+Backup%2C+Two+Adjustable+Heads+Emergency+Lights.jpg"),
    (59, "https://cdn.amplifi.pattern.com/4622c276-eb22-4aa7-b1dc-b2073fdc9d0e_medium.jpg"),
    (61, "https://m.media-amazon.com/images/I/61lHUJkwt7L._AC_SL1500_.jpg"),
    (63, "https://mobileimages.lowes.com/productimages/a01c842a-c570-45be-ad8f-490cfc1185c8/67585337.jpeg?size=pdhism"),
    (65, "https://store.ottawatoollibrary.com/wp-content/uploads/2024/03/240302-06.jpg"),
    (66, "https://www.multifunctiontools.com/wp-content/uploads/2024/11/65151690-scaled.jpg"),
    (68, "https://mobileimages.lowes.com/productimages/ce424fab-5dee-44ed-8fa1-3474c2aef646/48423962.jpg?size=pdhism"),
    (70, "https://i5.walmartimages.com/seo/Gas-Line-Ptfe-Thread-Sealant-Tape-1-2-In-X-260-In-Yellow-Full-Density-Bundle-of-2-Rolls_c5add9a5-596e-4c0b-833b-7b06a7a6a724.5f53e90edc3f2734c1712a091604de90.jpeg?odnHeight=640&odnWidth=640&odnBg=FFFFFF"),
    (72, "https://voomisupply.com/cdn/shop/files/71iSAyYDtOL._AC_SL1500.jpg?v=1722742369"),
    (74, "https://mobileimages.lowes.com/productimages/f2aae846-6dd5-44eb-b08d-1ff859b10348/05215073.jpg?size=pdhism"),
    (76, "https://m.media-amazon.com/images/I/61HNCsETkqL._AC_SL1500_.jpg"),
    (79, "https://i5.walmartimages.com/seo/Uxcell-3Pcs-3-4-19mm-ID-x-6Ft-Pipe-Insulation-Foam-Tube_4ad91354-e419-4ab5-8c15-45894ae52c26.1660dceac5a4e34e044a96bdf6457a76.jpeg"),
    (81, "https://m.media-amazon.com/images/I/71Wo+cp08DL._AC_.jpg"),
    (83, "https://haste-uae.com/wp-content/uploads/2026/02/ID340420204788-0102_preview.jpg"),
    (85, "https://jacksonsystems.com/wp-content/uploads/2026/03/PRCD405A_anglefront-1-scaled.jpg"),
    (87, "https://img.vevorstatic.com/us/LNSPCBYC150GPPQCEV1/original_img-v1/condensate-pump-m100-12.jpg?timestamp=1686794734000&format=webp&format=webp"),
    (89, "https://i5.walmartimages.com/seo/Nashua-2-in-x-60-yd-Silver-Premium-Duct-Tape-357-2_5070f20b-7a3b-4e7f-927a-caa3012900f6.7502b15cbcbeafe08a7e9fbddc004998.jpeg"),
    (91, "https://cdn11.bigcommerce.com/s-3ihov9f/images/stencil/1280x1280/products/35721/114690/us_BXSLMH1HP110VEVAMV1_original_img-v3_recovery-machine-m100-1.2__75138.1679726432.jpg?c=2"),
    (92, "https://images.thdstatic.com/productImages/01320a0c-e964-4554-a0f3-984756960ffc/svn/master-flow-flexible-ductwork-f6ifd8x300-64_1000.jpg"),
    (94, "https://haste-uae.com/wp-content/uploads/2025/02/VDG-1.png"),
    (95, "https://down-id.img.susercontent.com/file/id-11134207-7ra0i-mb3kirm2pzo90c"),
    (98, "https://images.alpinehomeair.com/1000x1000/nws/photos/furnacefilterrack_3A2820BD-6E3F-4749-BDAB-006604ACE7FE.jpg"),
    (100, "https://texlift.com/cdn/shop/files/Manual-Pallet-Jack-5500-lbs-Capacity-Model-US-PTM55K-Jack-Pallet-TEXLIFT-30092298387525.jpg?v=1777456600&width=1200"),
    (102, "https://apim.canadiantire.ca/v1/product/api/v1/product/image/0600624p?baseStoreId=CTR&lang=en_CA&subscription-key=c01ef3612328420c9f5cd9277e815a0e&imwidth=1244&impolicy=gZoom"),
    (104, "https://media.tractorsupply.com/is/image/TractorSupplyCompany/2532921?wid=554&hei=554&qlt=90&fmt=jpeg&resMode=sharp2&op_usm=0.9,1.0,8,0"),
    (106, "https://img.uline.com/is/image/uline/H-2941-72A_txt_USEng?$LargeRHD$"),
    (107, "https://m.media-amazon.com/images/I/51J0KcG9VcL._AC_SL1500_.jpg"),
    (108, "https://i5.walmartimages.com/seo/Gladiator-Cargo-Nets-SUT100-6-x-8-ft-Heavy-Duty-Trailer-Cargo-Net_6b08548a-a184-4c65-ba42-b81eda27aa82.71f8a298bad7b7fb2eb9bc8a00601cf0.jpeg"),
    (110, "https://i.pinimg.com/originals/51/d1/ab/51d1abf2d1ce2949105e94883cfc53af.jpg"),
    (112, "https://www.kroger.com/product/images/large/front/0075007120871"),
    (114, "https://m.media-amazon.com/images/I/51uvUqvnR9L._SL1000_.jpg"),
    (117, "https://m.media-amazon.com/images/I/6148w+qtA5L._AC_SL1365_.jpg"),
    (119, "https://media.cityelectricsupply.com/media/dottie/5mb381/images/dottie_918344_p_lrg.webp"),
    (121, "https://cdn11.bigcommerce.com/s-gdy1ehz/images/stencil/1280x1280/products/26679/26778/848__62509.1740407462.png?c=2"),
    (122, "https://m.media-amazon.com/images/I/61zNXBn4gvL._AC_SL1500_.jpg"),
    (124, "https://www.zoro.com/static/cms/product/large/ZYgiffSdKQVanhaTPGWnXXbpmyD14pvsp.JPG"),
    (126, "https://i5.walmartimages.com/seo/12-x-1-White-Ruspert-Coated-Hex-Washer-Head-Self-Drilling-Screws-100-pcs_dc54ea43-b213-497d-8eda-a209e6a6d5c2.2853edbb611d416f361089f2068724af.jpeg"),
    (128, "https://mobileimages.lowes.com/productimages/18002a31-f0fd-4990-b194-a53e59f0a6ff/15526917.jpg?size=pdhism"),
    (130, "https://www.permatex.com/wp-content/uploads/2021/12/24210_Main-720x720-ee44a4cc-0edf-4d50-a7e5-ebb89c6549cd.png"),
    (131, "https://m.media-amazon.com/images/I/81pA33jcCFL.jpg"),
    (133, "https://www.uboltit.com/media/products/images/products/7459_65dcf8a7f386e_proimg.png"),
    (136, "https://images.tekton.com/assets/tekton-retaining-ring-pliers-set-prr90003_front.jpg?width=1536&quality=75"),
    (138, "https://www.neisupplies.com/wp-content/uploads/2024/04/803686.JPG"),
    (139, "https://www.lickingspoon.com/wp-content/uploads/2025/09/colorful_microfiber_cleaning_cloths_v3wv8.jpg"),
    (141, "https://img.vevorstatic.com/us/DJSDTBT3538QKFWB8V0/original_img-v1/mop-bucket-with-wringer-f1.jpg?timestamp=1714439761000&format=webp"),
    (143, "https://i5.walmartimages.com/seo/Plasticplace-55-60-Gallon-Heavy-Duty-Trash-Bags-1-0-Mil-Black-Garbage-Can-Liners-100-Count_5bd9c6f4-9a88-4f04-ab03-08cbdeb82ccc.62928d5651cd33bed1ea427836629fc0.jpeg"),
    (145, "https://i5.walmartimages.com/seo/Professional-Lysol-Disinfectant-Spray-Spray-Aerosol-19-fl-oz-0-6-quart-Fresh-Scent-1-Each-Clear-Bundle-of-2-Each_8cf52b94-fa16-4699-bd5b-e62884a7be1b.e3cf9a8f17fe7b4f65e3270ed5df1818.jpeg"),
    (147, "https://mobileimages.lowes.com/productimages/602096b3-7765-4527-a91f-1b7ea2957708/86141834.jpeg?size=pdhism"),
    (148, "https://m.media-amazon.com/images/I/714fNQ7ds8L.jpg"),
    (150, "https://m.media-amazon.com/images/I/71e2rLxgSOL._AC_SL1500_.jpg"),
    (152, "https://store.w-p.co.uk/netalogue/zoom/109385.jpg"),
    (155, "https://www.floorbuffers.com/cdn/shop/products/404417-red-scrubbing-pads-case_700x700.jpg?v=1669663229"),
    (155, "https://m.media-amazon.com/images/I/71Ccsh05ehL._SL1500_.jpg"),
    (157, "https://i5.walmartimages.com/seo/IMM-Replacement-for-Century-GF2054-Electric-Motor-1-2-hp-1725-RPM-115-Volts-Sleeve-Bearing-Belt-Drive-Blower-Motor_121f6b5f-e5d8-4f38-965b-8a9e0d8bfea5.09123b139b6da2e6d3dc1015031cc44e.jpeg"),
    (159, "https://5.imimg.com/data5/SELLER/Default/2025/10/550491497/CZ/LP/YO/51544140/soler-drive-500x500.jpg"),
    (161, "https://www.rockymountainbearings.com/cdn/shop/files/pillowblock1_2997030c-2cd6-4c50-89c8-2c94113e3df0_1024x1024@2x.jpg?v=1761871390"),
    (164, "https://vbindustrialsupply.com/cdn/shop/files/5267338_61ab9c5c-39be-420f-a57c-34218edb60f10_1024x1024.jpg?v=1773281678"),
    (166, "https://m.media-amazon.com/images/I/81NxsS342tL._AC_UF894,1000_QL80_.jpg"),
    (168, "https://m.media-amazon.com/images/I/61CJXK1WKEL._AC_SL1500_.jpg"),
    (171, "https://www.warehouse-lighting.com/cdn/shop/files/productImages_2FT8-4FT-TYPB-2E-18W-40K-C_1.jpg?v=1686694484"),
    (173, "https://i5.walmartimages.com/seo/Dewalt-DW4541-Type-27-Depressed-Center-Fast-Cutting-Grinding-Wheel-4-1-2-in-Dia-x-1-4-in-T_acb1cf65-7bc1-4cf1-8d42-f156338fb2a4.109834e694ada9200a06505c0f455eb8.jpeg"),
    (176, "https://cdn11.bigcommerce.com/s-qz13ep5fb4/images/stencil/1280x1280/products/97583/226717/5005785b-2a86-4c52-a8c7-f819dbbd949e__77256.1674883046.jpg?c=1"),
    (178, "https://i5.walmartimages.com/seo/Scotch-Super-77-Multi-Purpose-Spray-Adhesive-13-5-Oz_7713d284-e4eb-494b-bf48-d3ee6d83c6b8.aa06ebd6003e539d364f30227b9f9306.jpeg"),
    (181, "https://i5.walmartimages.com/seo/GE-Advanced-Silicone-Kitchen-Bath-Sealant-Pack-of-1-Clear-10-1-fl-oz-Cartridge_9028e055-0cc9-49ec-b534-1cf2e6ca13e2.4b449f2e46b6473538877b30c1b58a84.jpeg"),
    (183, "https://i5.walmartimages.com/seo/CRC-03086-Food-Grade-Penetrating-Oil-Aerosol-11-Oz_77f16119-fa24-4f84-b634-deb1afb58d5f.5196de802f91757f132e911b58eb9356.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF"),
    (185, "https://trdsf.com/cdn/shop/files/complete-electrical-loto-kit_1440x.png?v=1722620325"),
    (186, "https://images.globalindustrial.com/images/1500x1500/B726492.jpg"),
    (188, "https://topprotools24.com/wp-content/uploads/2025/08/51ZijTHB0RL._SL1000_.jpg"),
    (190, "https://cdn11.bigcommerce.com/s-f4083/images/stencil/1280x1280/products/169197/227254/LIFT-HDFC-17WG-D__15092.1643737997.jpg?c=2"),
]

def get_file_extension(url):
    """Detecta a extensão do arquivo pela URL"""
    url_lower = url.lower()
    if ".png" in url_lower:
        return ".png"
    elif ".gif" in url_lower:
        return ".gif"
    elif ".webp" in url_lower:
        return ".webp"
    else:
        return ".jpg"

def main():
    if len(IMAGES) == 0:
        print("❌ Nenhuma imagem para baixar!")
        return

    # Criar pasta images
    images_dir = Path("images")
    images_dir.mkdir(exist_ok=True)

    print(f"\n{'='*70}")
    print(f"Iniciando download de {len(IMAGES)} imagens...")
    print(f"As imagens serão nomeadas pela CATEGORIA")
    print(f"Pasta de destino: {images_dir.absolute()}")
    print(f"{'='*70}\n")

    downloaded = 0
    failed = 0
    failed_list = []

    for idx, (categoria, url) in enumerate(IMAGES, 1):
        ext = get_file_extension(url)
        filename = f"img_{categoria}{ext}"
        filepath = images_dir / filename

        try:
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
            )

            with urllib.request.urlopen(req, timeout=10) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.content)

            print(f"✓ [{idx:3d}/{len(IMAGES)}] {filename}")
            downloaded += 1

        except Exception as e:
            failed += 1
            failed_list.append((categoria, str(e)[:50]))
            print(f"✗ [{idx:3d}/{len(IMAGES)}] {filename:15} - {str(e)[:40]}")

        time.sleep(0.1)

    # Resumo
    print(f"\n{'='*70}")
    print(f"✓ Sucesso: {downloaded}/{len(IMAGES)}")
    print(f"✗ Falhas: {failed}/{len(IMAGES)}")
    print(f"{'='*70}\n")

    if failed_list:
        print("Categorias com falha:")
        for cat, error in failed_list[:10]:
            print(f"  Cat {cat}: {error}")
        if len(failed_list) > 10:
            print(f"  ... e mais {len(failed_list) - 10}")

    files_created = len(list(images_dir.glob('img_*')))
    print(f"\n✓ Arquivos criados em images/: {files_created}")

if __name__ == "__main__":
    main()
