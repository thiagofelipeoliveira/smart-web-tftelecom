# Roteiro do vídeo pitch (até 4 minutos)

**Como gravar:** Loom (grátis) ou OBS, tela + câmera no canto. Publique no YouTube como **Não listado** e teste o link em uma aba anônima antes de enviar.

---

### 0:00 – 0:30 · Problema
**Tela:** Instagram/redes da empresa (ou um print de conversa de WhatsApp desorganizada).
> "Olá, eu sou o Thiago. A TF Telecom é um provedor de internet fibra. Até hoje, o cliente só achava a gente pelas redes sociais e, para qualquer coisa — saber qual plano contratar, pedir boleto ou avisar que a internet caiu — tinha que mandar mensagem e esperar alguém fazer a triagem na mão. Isso gera demora e venda perdida."

### 0:30 – 0:50 · Solução
**Tela:** Home do site publicado (tftelecom-chapeco.framer.website).
> "Criei um site responsivo para a TF Telecom em Chapecó, com os planos de 400, 500 e 600 Mega, e um assistente com inteligência artificial que faz o primeiro atendimento sozinho — recomenda o plano certo e direciona cada pedido para o setor correto."

### 0:50 – 1:50 · Aplicação funcionando
**Tela:** Rolar a página → abrir o assistente → fazer o quiz ao vivo.
> "O cliente responde quatro perguntas: onde usa, quantas pessoas, o que faz e quanto quer gastar. O assistente calcula a demanda e recomenda o plano — e explica o porquê. Se o ideal passa do orçamento, ele ajusta e mostra a alternativa. Um clique e a conversa de venda chega no WhatsApp já pronta."

**Tela:** Aba "Preciso de ajuda" → digitar "Minha internet caiu desde ontem".
> "Aqui o cliente escreve com as palavras dele. O sistema identifica que é suporte técnico, marca prioridade alta, gera um protocolo e já dá uma dica de primeiro atendimento."

**Tela:** Abrir no celular (F12 → modo celular).
> "E tudo funciona no celular, que é de onde vem a maioria dos nossos clientes. Pensei também em quem tem deficiência visual: com um toque, o assistente lê as perguntas em voz alta, o cliente pode ditar a mensagem em vez de digitar, aumentar a letra ou usar o alto contraste."

**Tela (rápido):** clicar em 🔊 Leitura em voz alta (deixar o áudio tocar 2 segundos), depois em Alto contraste e A+.

### 1:50 – 2:20 · Plataforma no-code
**Tela:** Editor do Framer — mostrar seções, Stacks e breakpoints.
> "A base foi feita no Framer. Usei o próprio Agent de IA do Framer para gerar as seções a partir de um briefing, ajustei tudo no editor visual (versões para computador, tablet e celular) e publiquei com um clique em tftelecom-chapeco.framer.website. Sem servidor e sem custo."

### 2:20 – 3:10 · Personalizações com padrões web
**Tela:** Painel do Embed + trechos do código (CONFIG, CSS, função `classificar`).
> "Mas o Framer não tem um recomendador nem um classificador pronto. Então usei um componente Embed com HTML, CSS e JavaScript próprios. No HTML, estrutura semântica e ARIA para leitores de tela. No CSS, variáveis da marca, grid responsivo e foco visível para quem navega pelo teclado. No JavaScript, a lógica do quiz e o classificador. Também criei um botão de WhatsApp que mostra se o atendimento está aberto agora."

### 3:10 – 3:40 · IA e automação
**Tela:** digitar "minha internete caiu" (com erro) → mostrar confiança e "palavras que mais pesaram"; depois `testes/RESULTADOS.md`.
> "O recurso inteligente é um modelo de aprendizado de máquina, um Naive Bayes, treinado no próprio navegador. Ele entende a mensagem mesmo com erro de digitação, mostra a confiança e as palavras que pesaram na decisão. Testei com 26 frases que ele nunca viu: a primeira versão, só com palavras-chave, acertava 73%; o modelo atual acerta 92%, e a urgência é detectada em 100% dos casos. Tudo sem custo de API e sem enviar dados a terceiros, respeitando a LGPD. E, com um webhook no Make, cada pedido pode virar uma linha numa planilha."

### 3:40 – 4:00 · Diferencial e fechamento
**Tela:** Site no celular.
> "O diferencial é unir a velocidade do no-code com o controle dos padrões web: um atendimento que funciona 24 horas, organiza os pedidos e ajuda a vender. No-code não significa ausência de conhecimento técnico. Obrigado!"
