# Step One: landing page de conversão

Página única e estática (`index.html` + `assets/`), sem dependências nem build. Na Vercel: importar o repositório e carregar em Deploy.

Carga inicial: **0,28 MB e 12 pedidos**. O site atual em WordPress carrega 11,8 MB em 141 pedidos.

## O que a página faz para gerar mais leads

1. **Quiz em ecrã inteiro em vez de formulário.** Todos os botões abrem um quiz de 5 perguntas de um toque: objetivo, obstáculo, plano, compromisso 0–10 e investimento. Depois há um ecrã "a preparar a tua recomendação" e aparece o **plano recomendado personalizado**, com um antes/depois parecido com o objetivo escolhido. Só nesse momento se pedem nome, telemóvel e email.
2. **Antes/depois interativos.** As 10 fotos foram separadas em antes e depois, e cada uma é um comparador que se arrasta. O do topo anima sozinho para mostrar que é interativo. Há filtros "Só alimentação" e "Alimentação + treino".
3. **Topo com promessa clara**: "Perde gordura a comer o que gostas", prova social (+50 clientes ativos), CTA principal e um resultado visível logo à primeira vista.
4. **Venda por etapas**: dor ("O problema nunca foste tu") → método (flexível, personalizado, acompanhado) → serviços → **tabela comparativa** (Step One vs. dieta da internet vs. ginásio sem plano) → como funciona → testemunhos → planos → garantia → equipa → FAQ → CTA final.
5. **Testemunhos numa conversa de WhatsApp** a correr dentro de um telemóvel, mais citações em destaque.
6. **Planos** Alimentação, Completo (recomendado) e Treino. Cada botão abre o quiz com o plano já escolhido. Os preços não aparecem.
7. **"0 fidelização" em destaque** como garantia (cancelar ou pausar com 15 dias de aviso).
8. **Urgência e recuperação**: barra "Vagas limitadas em <mês atual>", barra fixa com CTA no telemóvel e aviso "Antes de saíres…" no desktop (uma vez por sessão).
9. **Medição**: `cta_click`, `quiz_open`, `quiz_step`, `quiz_complete`, `generate_lead`, `exit_intent_shown` no dataLayer; `Lead`, `QuizOpen` e `QuizComplete` no Pixel da Meta. Cada lead leva `utm_*`, `fbclid` e `gclid`. No GTM, a conversão principal deve ser `generate_lead`.

Todos os factos vêm do site atual: +50 clientes, sem fidelização com 15 dias de aviso, planos no próprio dia, 4–8 semanas, casa ou ginásio, restrições alimentares, vídeos dos exercícios. Não foram inventados preços, números nem garantias.

## Obrigatório antes de pôr anúncios

No fim do `index.html`, no bloco `CONFIG`:

- **`formEndpoint`**: URL de um webhook que receba POST JSON (SureTriggers, Make, Zapier, n8n ou CRM). **Sem isto, o formulário mostra um erro e o lead não fica guardado.**
  Campos enviados: `nome, telemovel, email, objetivo, obstaculo, plano, comprometimento, investimento, plano_recomendado, consentimento, pagina, referrer, enviado_em, utm_*`.
- **`whatsapp`**: número no formato `3519XXXXXXXX`. Ativa o botão WhatsApp no telemóvel e no ecrã final.
- `gtmId` e `metaPixelId` já vêm do site atual e só carregam depois de o visitante aceitar cookies.

## A confirmar

- Que a equipa contacta cada pessoa depois do quiz (é o que a página promete).
- Autorização de todos os clientes para as fotos e testemunhos (o repositório é público: considerar torná-lo privado).
- Que o plano "só treino" existe (a FAQ original diz que se pode escolher só um dos planos).

## Testes A/B sugeridos

- Título: "Perde gordura a comer o que gostas" vs. "Come o que gostas enquanto perdes peso".
- Mostrar um preço de referência ("a partir de X €/mês") nos planos.
- Retirar a pergunta do investimento (mais leads, menos qualificados).

## Colar no WordPress (Elementor)

Usar o ficheiro **`elementor.html`**, não o `index.html`. É a mesma página, mas com as imagens e as fontes em endereços absolutos (CDN jsDelivr, a partir deste repositório). Com o `index.html` as imagens não aparecem, porque os caminhos `assets/img/...` passam a apontar para `step-one.pt/assets/...`, que não existe.

1. Criar uma página nova e, em **Modelo**, escolher **Elementor Canvas** (sem cabeçalho nem rodapé do tema).
2. Adicionar um contentor em **largura total**, sem padding, e dentro dele um widget **HTML**.
3. Colar todo o conteúdo de `elementor.html` e publicar.

Se o repositório passar a privado, o CDN deixa de funcionar. Nesse caso, carregar a pasta `assets/` para o WordPress (ou usar o link da Vercel) e substituir o endereço base no ficheiro.
