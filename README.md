# Step One: nova landing page

Nova versão da página https://step-one.pt/, focada em gerar leads. Usa as mesmas imagens, as mesmas cores (laranja `#FC8424`, cinzento, creme), a mesma fonte (Raleway) e segue a ordem de secções do original. Muda o que trava a conversão.

- `index.html`: a página completa (HTML, CSS e JS num só ficheiro, sem dependências).
- `assets/img/`: as fotografias do site original, convertidas para WebP em 2 tamanhos.
- `assets/fonts/`: Raleway alojada no próprio site (sem Google Fonts).

Para ver localmente: `python3 -m http.server` dentro desta pasta e abrir http://localhost:8000.

## Análise do site atual (24/09/2026)

| # | Problema | Impacto | Na nova página |
|---|---|---|---|
| 1 | **Formulário longo e só no fundo**: 7 campos obrigatórios de uma vez (nome, email, telemóvel, 3 seleções, número 0–10) mais a checkbox | É o maior travão. Pedir os dados pessoais logo no início afasta quem ainda está "só a ver" | **Quiz em 5 passos**: primeiro 4 perguntas de um toque (objetivo → obstáculo → compromisso → investimento) e só no fim nome, telemóvel e email. Barra de progresso e "60 segundos" |
| 2 | **Hero em slider**: 2 slides a rodar, CTA "Quero começar já!" pequeno, mensagem dividida | Os sliders dispersam a atenção e o 2.º slide quase não é visto | Um só hero com a promessa principal ("Come o que gostas enquanto perdes peso"), mais 3 botões "Qual é o teu objetivo?" que já respondem ao 1.º passo do quiz |
| 3 | **Página muito pesada**: 11,8 MB e 141 pedidos no mobile, PNGs de 1–2,7 MB, 53 CSS e 43 JS, 11 plugins (incluindo 3 plugins de formulários: Forminator, Elementor Forms e Contact Form 7) | Anúncios pagos a levar tráfego para uma página lenta = leads perdidos antes de a página abrir | **0,23 MB e 9 pedidos** na carga inicial. WebP responsivo, lazy-load, zero plugins |
| 4 | **Antes/depois um de cada vez** num carrossel, sem contexto | A melhor prova do negócio fica escondida | Carrossel com 3 visíveis no desktop, etiquetas Antes/Depois, duração e tipo de plano, contador e CTA logo abaixo |
| 5 | **Não explica como funciona** (só aparece numa FAQ fechada) | Incerteza = não preencher | Secção "Como funciona" em 4 passos e secção "O que está incluído" |
| 6 | **Testemunhos um a um** num slider, com botões "Read more" em inglês e gralhas | Pouca prova social visível | Os 8 testemunhos visíveis ao mesmo tempo, em estilo de mensagem (gralhas de escrita corrigidas) |
| 7 | **Não fala das dores do cliente** | O visitante não se identifica | Secção "Reconheces-te em alguma destas?" com as objeções que o próprio formulário já recolhe |
| 8 | **Sem CTA fixo no mobile**, e "VAGAS LIMITADAS" sem link | A maioria das visitas é mobile, e o CTA fica longe | Barra fixa no fundo do mobile (aparece depois do hero e esconde-se no formulário). Todas as faixas "Vagas limitadas" levam ao quiz e mostram o mês atual |
| 9 | Contraste fraco: texto cinzento-claro em fundo cinzento, texto branco sobre laranja, texto em cima da foto no mobile ("Emagrecimento") | Difícil de ler | Botões laranja com texto escuro (contraste AA), texto sobre fotos só com gradiente escuro por trás |
| 10 | SEO: sem meta description, título genérico | Menos cliques no Google e nas partilhas | Título, description e Open Graph |
| 11 | Formulário sem UTMs úteis (só um campo escondido "utm_source") | Não se sabe que anúncio gera leads | Guarda `utm_*`, `fbclid` e `gclid` e envia-os com cada lead. Eventos `quiz_start`, `quiz_step`, `generate_lead` e `cta_click` no dataLayer, e `Lead` no Pixel da Meta |

Mantive tudo o que o site já prometia (+50 clientes ativos, sem fidelização com 15 dias de aviso, planos no próprio dia, resultados em 4–8 semanas, restrições alimentares, casa ou ginásio). **Não inventei preços, números nem garantias.**

## Antes de publicar (obrigatório)

1. **Destino dos leads**: em `index.html`, no bloco `CONFIG` no fim do ficheiro, preencher `formEndpoint` com um URL de webhook que aceite POST JSON. Sem isto, o formulário mostra um erro e **não guarda nada**. Opções:
   - **SureTriggers** (já está instalado no WordPress): criar um "Webhook trigger" e ligá-lo ao destino atual dos leads (email, Google Sheets, CRM).
   - Make, Zapier ou n8n, com a mesma lógica.
   - Campos enviados: `nome, telemovel, email, objetivo, obstaculo, comprometimento, investimento, consentimento, pagina, referrer, enviado_em, utm_*`.
2. **WhatsApp** (recomendado): preencher `whatsapp` com o número em formato `3519XXXXXXXX`. Aparece um botão WhatsApp na barra do mobile e no ecrã de "Candidatura recebida". Com o número vazio, os botões ficam escondidos.
3. **Tracking**: `gtmId` (GTM-TR3396WB) e `metaPixelId` (1332430662011467) já vêm do site atual. Só carregam depois de o visitante aceitar cookies. No GTM, criar uma conversão com o evento `generate_lead`.
4. **Confirmar os textos**: a secção "Como funciona" (passo 2, "a equipa contacta-te") e a FAQ "O que acontece depois de enviar?" descrevem um contacto após a candidatura. Confirmar que é assim que trabalham.
5. **Autorização das fotos e testemunhos**: a página diz que as imagens foram "partilhadas por clientes com autorização". Confirmar que é verdade para todas.

## Como publicar no WordPress

- **Opção A (a mais rápida e leve)**: carregar a pasta `step-one/` para o alojamento (por exemplo `step-one.pt/lp/`) e apontar os anúncios para lá.
- **Opção B**: criar uma página no Elementor com o template "Elementor Canvas" e um widget HTML com o conteúdo de `index.html`, com as imagens carregadas na Biblioteca de Media (atualizar os caminhos `assets/img/...`). Perde parte do ganho de velocidade, porque o WordPress continua a carregar os plugins.
- Depois de publicar, desativar os plugins de formulários que deixarem de ser usados e o HurryTimer (está carregado mas não é usado).

## Próximos testes A/B sugeridos

- Título do hero: "Come o que gostas enquanto perdes peso" vs. "Perde gordura sem passar fome".
- Pergunta do investimento: manter como filtro vs. retirar (mais leads, menos qualificados).
- Mostrar um preço de referência ("a partir de X €/mês"), que costuma qualificar os leads e aumentar a confiança.
