# Guia de montagem no Framer: passo a passo

> ✅ **Já montado e publicado em https://tftelecom-chapeco.framer.website**. Este guia documenta como o site foi feito e serve para refazer ou editar.

Tempo estimado: 1h30 a 2h. O plano gratuito do Framer é suficiente (publica em `seusite.framer.website`).
**Modelo visual:** abra `prototipo/site-completo.html` no navegador. Cada seção dele é uma seção a recriar no Framer.

## 1. Criar o projeto
1. Crie uma conta em framer.com → **New Project** → **Blank** (ou um template gratuito de "Services").
2. **Site Settings → General**: título "TF Telecom — Internet fibra em Chapecó" e a descrição do arquivo `codigo-framer/seo-head.html`.
3. **Site Settings → General → Language**: **Portuguese** (gera `lang="pt-BR"`, importante para leitores de tela).
4. Fonte: em Text, escolha **Poppins** (Google Fonts, já disponível no Framer).
5. Cores (Assets → Colors): Azul `#1F4FE0`, Azul-escuro `#0B2FB0`, Marinho `#0A1F6E`, Amarelo `#FFD200`.

## 2. Montar as seções (componentes nativos do Framer)
Use **Stack** em todas as seções para que a responsividade funcione sozinha.

| Seção | Conteúdo | ID (âncora) |
|---|---|---|
| Menu | Logo (`prototipo/logo-tf.webp`) + links Planos, Assistente, Vantagens, Dúvidas, Contato + botão amarelo | — |
| Hero | "Chegamos em **Chapecó**", "+ Internet por menos preço", 3 vantagens, botões e card 400 MEGA R$ 99,90 | `inicio` |
| Planos | 3 cards: 400 Mega R$ 99,90 · 500 Mega R$ 119,90 (destaque "Mais vendido") · 600 Mega R$ 129,90. Cada botão leva ao WhatsApp | `planos` |
| Assistente | **Embed** com `assistente-tf.html` (passo 3) | `assistente` |
| Vantagens | 100% fibra, Wi-Fi 6, instalação grátis, indique e ganhe | `vantagens` |
| Dúvidas | 5 perguntas (textos no protótipo). Use o componente **Accordion** do Framer | `duvidas` |
| Contato | "Assine já!", WhatsApp (49) 92002-3806, (49) 3329-6270, horário | `contato` |

ID da seção: selecione a seção → painel direito → **Scroll Section / ID**. No menu, aponte os links para `#planos`, `#assistente` etc.
Link do WhatsApp nos botões: `https://wa.me/5549920023806?text=Quero%20o%20plano%20500%20MEGA`.

## 3. Assistente com IA (HTML + CSS + JS)
1. Na seção Assistente, pressione **I** → **Embed** → **Type: HTML** → cole **todo** o `codigo-framer/assistente-tf.html`.
2. Largura: **Fill** (máx. 880px). Altura: **1050px** no desktop e **1800px** no breakpoint **Phone**. Essas alturas foram medidas e cabem em todos os estados do assistente, sem barra de rolagem. (Se o visitante aumentar a fonte com o botão A+, o próprio Embed ganha rolagem interna. Isso é esperado.)
3. Planos, preços e WhatsApp já estão no bloco `CONFIG` do `<script>`. No futuro, mude só ali.
4. Fundo da seção: azul-claro `#F3F6FF`, para destacar o painel azul.

## 4. Botão de WhatsApp com status (fixo na tela)
O Embed do Framer roda dentro de um *iframe*. Por isso o botão precisa ser fixado **pelo Framer**:
1. Insira um **Embed (HTML)** e cole `codigo-framer/botao-whatsapp-status.html`.
2. Tamanho: **300 × 60** (no breakpoint Phone, **220 × 56**).
3. Painel direito → **Position: Fixed** → ancore no canto inferior direito, a 16px das bordas.
4. Coloque-o no topo da lista de camadas, para ficar acima de tudo.

## 5. SEO (opcional, recomendado)
- **Site Settings → General**: a descrição e a imagem social (use o anúncio "Chegamos Chapecó").
- Se o seu plano liberar **Custom Code**: cole o bloco `<script type="application/ld+json">` de `seo-head.html` em "Start of `<head>`".

## 6. Registrar leads numa planilha (opcional, "automação")
1. No Make: crie um cenário **Webhooks → Custom webhook** → **Google Sheets → Add a row**.
2. Copie a URL do webhook e cole em `CONFIG.webhook` no `assistente-tf.html`.
3. Cada clique em "Contratar/Enviar pelo WhatsApp" vira uma linha na planilha, com plano ou categoria, prioridade e protocolo.

## 7. Responsividade
1. Adicione os breakpoints **Tablet (810)** e **Phone (390)**.
2. No Phone: menu vira ícone (componente Navigation com variante mobile), os cards de planos ficam em coluna e o título do Hero fica com cerca de 40px.
3. Teste no **Preview** em cada tamanho.

## 8. Acessibilidade (checklist)
- Todas as imagens com **Alt Text** (logo: "TF Telecom").
- Apenas **um H1** (Hero). Os títulos de seção são H2.
- Navegue só com **Tab**: o foco aparece em amarelo e as abas do assistente mudam com as setas ← →.

## 8.1 Recursos para deficientes visuais (já prontos no assistente)
- **A− / A+**: texto de 80% a 160%.
- **Alto contraste**: preto, branco e amarelo, sem imagens de fundo.
- **Leitura em voz alta**: lê cada pergunta, as opções e os resultados em português. Os resultados também têm o botão "🔊 Ouvir".
- **Ditado por voz** (🎤) no "Preciso de ajuda": funciona no Chrome, no Edge e no Android. **Depois de publicar, teste o microfone.** Se o Framer bloquear o microfone dentro do Embed, o botão avisa e o cliente pode digitar normalmente.
- As escolhas do visitante ficam salvas no navegador dele.
- Teste também com um leitor de tela: **NVDA** (Windows, grátis) ou **TalkBack** (Android).

## 9. Publicar e gerar evidências
1. **Publish** → `https://<nome>.framer.website`.
2. Prints do site publicado no desktop e no celular (Chrome: F12 → ícone de celular).
3. Coloque o link e os prints no README e siga o `CHECKLIST_ENTREGA.md`.
