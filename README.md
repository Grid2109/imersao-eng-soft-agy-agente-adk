# Agente de Estudos - Mentor Personalizado com Google ADK

Este projeto consiste em um agente autônomo especialista em planejamento e mentoria de estudos, construído com o Google Agent Development Kit (ADK) em Python e integrado aos modelos generativos Gemini.

O objetivo do agente é transformar metas de aprendizado em cronogramas executáveis no mundo real, com distribuição de tópicos, revisões espaçadas, pontos de autoavaliação e exportação de uma agenda em formato CSV pronta para ser importada no Google Agenda. Além do cronograma, o agente também disponibiliza uma skill de revisão ativa para geração de flashcards atômicos e simulados práticos.

---

## Arquitetura e Engenharia do Agente

O desenvolvimento do agente priorizou boas práticas de engenharia de software com inteligência artificial, segurança de execução e otimização de contexto:

1. Divulgação Progressiva de Skills (Agent Skills Specification):
   Para evitar sobrecarga de contexto e consumo desnecessário de tokens na inicialização, as habilidades do agente foram implementadas segundo o padrão de divulgação progressiva:
   - Nível 1 (Metadados): Na inicialização, o agente carrega apenas nome e descrição das skills para descoberta.
   - Nível 2 (Instruções e Gating): O corpo da skill e suas regras de ativação são lidos sob demanda somente quando a intenção do usuário demanda aquela competência.
   - Nível 3 (Recursos Especializados): Documentos de suporte, fluxos de trabalho, regras de exportação e templates em formato Markdown são carregados dinamicamente apenas no momento exato em que são necessários.

2. Ferramentas de Arquivo Seguras (EnvironmentToolset):
   O agente tem acesso ao sistema de arquivos local restrito à pasta de planos por meio de uma subclasse customizada do EnvironmentToolset. Para manter a segurança da execução, apenas as operações de leitura (ReadFile) e gravação (WriteFile) foram expostas, sem acesso a comandos de terminal ou shell do sistema operacional.

3. Provedor de Instruções Dinâmico (Instruction Provider):
   Para permitir que o agente compreenda datas relativas (como "segunda que vem" ou "daqui a duas semanas") sem alucinações de calendário, implementei um provedor dinâmico que injeta a data atual do sistema e as referências exatas dos próximos dias da semana em tempo de execução.

---

## Habilidades do Agente (Skills)

O agente conta com duas skills modulares principais:

1. plano-de-estudos:
   - Regra de Ativação (Gating): Sem objetivo claro, prazo, disponibilidade semanal e nível atual, o agente recusa a montagem antecipada e faz perguntas focadas para coletar os dados faltantes.
   - Metodologia de Aprendizagem: Organiza módulos com prioridades, aplica intervalos de revisão espaçada (D+1, D+3 e D+7), checkpoints semanais de autoavaliação e reserva técnica de dias de margem para absorção de imprevistos.
   - Exportação para Google Agenda: Gera e grava um arquivo CSV válido no padrão do Google Agenda respeitando os dias e horários informados.
   - Replanejamento Resiliente: Quando o estudante relata sessões perdidas, o agente utiliza primeiro os dias de margem planejados para absorver o atraso, sem empilhar múltiplos conteúdos no mesmo dia e mantendo o prazo acordado.

2. revisao-ativa:
   - Recebe anotações, resumos, trechos de código ou temas de estudo.
   - Elabora flashcards focados no princípio de atomicidade (uma única pergunta direta por cartão e resposta concisa).
   - Constrói um quiz de fixação de 5 perguntas de múltipla escolha com distratores realistas, acompanhado de gabarito comentado e justificativas conceituais.

---

## Jornada do Projeto e Evolução

O projeto seguiu a trilha pedagógica da imersão, dividida em fases de maturidade de engenharia de software com IA:

### Fase 1: Construção e Validação Local (Marco deste Repositório)
- Exploração do uso de agentes de IA para desenvolvimento de software, utilizando o ecossistema Antigravity do Google.
- Criação de um agente que ajuda na elaboração de um plano de estudos, gerando um arquivo CSV na pasta local do ambiente.
- Uso do ADK (Agent Development Kit) para construir e testar o agente em um ambiente controlado.
- Desenvolvimento prático focado em orquestração de agentes, decomposição de tarefas técnicas e integração de ferramentas de IA no ciclo de desenvolvimento.
- Implementação da skill complementar de revisão ativa para geração de flashcards e quizzes.
- Este repositório reflete a conclusão completa desta fase, que corresponde ao marco de versionamento da Aula 4 do curso.

### Fase 2: Evolução para Nuvem (Roadmap Futuro)
Neste momento, optei por não realizar o deploy em nuvem, decidindo explorar essa etapa em uma oportunidade futura com outras abordagens de infraestrutura. Como visão de evolução da solução, o projeto prevê:
- Expandir o projeto para que o agente possa ser acessado remotamente, transformando-o em uma API gerenciada.
- Fazer o deploy do agente na nuvem (como no Agent Runtime ou Cloud Run), criando uma solução "agent as a service".
- Implementar a persistência dos dados (arquivo CSV) utilizando o Google Cloud Storage (GCS), substituindo a persistência local.
- Configurar autenticação e permissões usando Application Default Credentials (ADC) e contas de serviço para garantir segurança e acesso controlado.
- Demonstrar como o agente pode ser consumido por outros sistemas via API, abrindo possibilidades para integrações diversas.

---

## Ambiente de Execução e Contexto Prático

A proposta central da Imersão Dev foi trabalhar diretamente no Google Cloud Platform (GCP), utilizando escopo de projeto para gerenciar recursos de nuvem e créditos diários de US$ 5 disponibilizados para o laboratório. Iniciei e executei o desenvolvimento no Google Cloud Shell conforme planejado.

Durante o evento, devido ao esgotamento dos créditos diários de nuvem, optei por dar continuidade ao projeto reproduzindo o ambiente de ponta a ponta localmente na minha máquina com o gerenciador uv e o ADK Web. Isso me permitiu realizar todas as auditorias de código, refinamentos de calendário, testes de replanejamento e a implementação da nova skill sem bloqueios. Por opção técnica, decidi focar este repositório na entrega robusta da engenharia e execução local do agente, deixando o deploy em nuvem para ser realizado de outra forma em uma oportunidade futura.

---

## Como Executar

### Pré-requisitos

- Ambiente: Google Cloud Shell ou máquina local (Linux, macOS ou Windows).
- Python: versão 3.11 a 3.13 (o arquivo pyproject.toml restringe a execução a essa faixa).
- Gerenciador de pacotes uv: ferramenta rápida para gestão de ambientes Python. Para instalar o uv, siga o guia oficial em [docs.astral.sh/uv](https://docs.astral.sh/uv/getting-started/installation/).
- Chave de API do Google AI Studio: gerada gratuitamente em [aistudio.google.com/apikey](https://aistudio.google.com/apikey).

### Passo a passo

1. Clone o repositório e acesse a pasta do agente:
   ```bash
   git clone https://github.com/Grid2109/imersao-eng-soft-agy-agente-adk
   cd imersao-eng-soft-agy-agente-adk/agente-estudos
   ```

2. Configure o arquivo de ambiente:
   ```bash
   cp .env.example .env
   ```

   Abra o arquivo `.env` e preencha com sua chave de API e configurações:
   ```env
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   GEMINI_API_KEY=sua-chave-aqui
   MODEL=gemini-3.8-flash
   ```
   Caso o modelo 3.8 apresente instabilidade temporária (erro 503) ou atinja os limites diários do plano gratuito (erro 429), você pode alterá-lo no `.env` para modelos Flash compatíveis como `gemini-3.6-flash` ou `gemini-2.5-flash`, conforme detalhado na seção de Solução de problemas.

3. Sincronize as dependências e o ambiente virtual:
   ```bash
   uv sync
   ```

4. Inicie o servidor do ADK Web:
   ```bash
   uv run adk web --allow_origins="*"
   ```

Abra o endereço `http://127.0.0.1:8000` indicado no console e selecione o agente `app` para iniciar a interação.

> Aviso de cota: A chave gratuita do Google AI Studio possui limites de requisições por minuto (RPM) e por dia (RPD). Em testes frequentes, erros transitórios de cota (rate limit) são esperados.
>
> Aviso de segurança: O ADK Web serve só para desenvolvimento e depuração, não para produção. O parâmetro `--allow_origins="*"` foi utilizado para viabilizar testes locais e proxies de desenvolvimento, mas não deve ser utilizado em servidores expostos diretamente na internet.

---

## Prompts para Validação do Agente

Para testar o agente nos cenários previstos no projeto, utilize os seguintes exemplos:

1. Teste de Gating (pedido incompleto):
   ```text
   Quero organizar meus estudos de JavaScript.
   ```
   O agente deve responder solicitando apenas os dados que faltam (prazo, disponibilidade e nível atual) sem carregar recursos pesados.

2. Teste de Plano Completo e Gravação do CSV:
   ```text
   Quero aprender JavaScript para fazer meu primeiro projeto de portfólio em 5 semanas. Começo segunda que vem. Posso estudar segunda, quarta e sexta, 2h por dia às 19h. Já sei HTML e CSS, mas nunca programei.
   ```
   O agente deve apresentar a visão geral, cronograma com checkpoints e salvar o arquivo `agente-estudos/planos/plano-de-estudos.csv`.

3. Teste de Replanejamento e Ajuste Guiado (Prompt Steering):
   - Solicitação inicial de ajuste:
     ```text
     Perdi as sessões de quarta e sexta da primeira semana. Ajusta o plano?
     ```
   - Refinamento e correção de calendário:
     ```text
     Atenção: eu avisei que a quarta (18/11) e a sexta (20/11) foram perdidas! Portanto, não pode haver sessão na sexta 20/11. O cronograma deve recomeçar na segunda seguinte (23/11), empurrando os conteúdos para frente e absorvendo nas margens do final. Apresente o cronograma corrigido onde a semana 1 tem apenas a segunda-feira 16/11.
     ```
     O agente lê o CSV com `ReadFile`, aplica a cascata pedagógica correta e sobrescreve o arquivo no disco com `WriteFile`.

4. Teste de Revisão Ativa:
   ```text
   Estudei sobre Closures em JavaScript. Pode gerar flashcards e um quiz de 5 perguntas?
   ```
   O agente ativa a skill `revisao-ativa` e retorna os cartões de memorização e o quiz comentado.

---

## Importação no Google Agenda

Após a geração do plano pelo agente:
1. Localize o arquivo gerado em `agente-estudos/planos/plano-de-estudos.csv`.
2. No Google Agenda (pelo navegador no computador), acesse: Configurações -> Importar e exportar -> Importar.
3. Selecione o arquivo CSV, escolha a agenda de destino e conclua a importação para visualizar as sessões distribuídas no seu calendário.

---

## Agente em funcionamento

Registros visuais da interação com o agente no ADK Web e da importação das agendas no Google Agenda, organizados em sequência cronológica.

| Sequência | Etapa / Evidência | Caminho da imagem |
| :---: | :--- | :--- |
| 01 | Teste 1 (Gating): Pedido incompleto, agente pergunta apenas o que falta no chat | `docs/images/01-cenario-1-gating.png` |
| 02 | Teste 2 (Plano Completo): Visão geral, cronograma das 5 semanas e gravação com WriteFile | `docs/images/02-cenario-2-plano.png` |
| 03 | Teste 3 (Replanejamento - Tentativa Inicial): Primeira resposta após relatar sessões perdidas | `docs/images/03-cenario-3-replanejamento.png` |
| 04 | Teste 3 (Replanejamento - Correção): Ajuste via prompt steering, validação de dias e regravação do CSV | `docs/images/04-cenario-3-replanejamento-corrigido.png` |
| 05 | Google Agenda (Novembro): Visão mensal de novembro com início dos estudos e agendas sobrepostas | `docs/images/05-agenda-novembro.png` |
| 06 | Google Agenda (Dezembro): Visão mensal de dezembro com conclusão do projeto e absorção das margens | `docs/images/06-agenda-dezembro.png` |

> Para incluir as capturas no repositório, basta salvar os arquivos de imagem com os nomes indicados na pasta `docs/images/`.

---

## Solução de problemas

### Escolha de Modelos e Propósito de Engenharia

O modelo principal e titular deste projeto é o **`gemini-3.8-flash`**, configurado como fallback padrão no código (`agent.py`). Conforme a documentação oficial do Google, o Gemini 3.8 Flash foi concebido especificamente para engenharia de software de longo prazo, agentes autônomos complexos e fluxos corporativos, combinando alto raciocínio lógico e precisão em chamadas de ferramentas (tool calling) com a eficiência da linha Flash.

Durante o desenvolvimento com o plano gratuito (Free Tier) do Google AI Studio, instabilidades e limites de tráfego podem ocorrer. Quando for necessário substituir o modelo temporariamente, **não se deve escolher qualquer modelo aleatório da lista geral do Google**:

1. **Modelos da linha Pro (como `gemini-2.5-pro` ou `gemini-3.1-pro-preview`):** Possuem cota zero no plano gratuito (`limit: 0`), resultando em erros imediatos de descontinuação (404) ou recusa de cota (429).
2. **Por que modelos da linha Lite (como `gemini-3.1-flash-lite`) não são recomendados:** Modelos da linha Lite são projetados exclusivamente para tarefas de altíssima velocidade e baixa complexidade (como classificação de texto, roteamento simples e resumos superficiais). Eles não possuem a capacidade de raciocínio necessária para tarefas de engenharia de software e agentes autônomos, que exigem cálculo preciso de calendário, obediência estrita a esquemas estruturados (como o formato rígido de 6 colunas do CSV) e aplicação do efeito cascata pedagógico. Em testes práticos, modelos Lite apresentaram inconsistências de formatação e quebra de contagem de colunas na gravação de arquivos.
3. **Modelos Flash recomendados para substituição temporária:**
   - **`gemini-3.6-flash`:** Modelo da mesma geração avançada do 3.8, com alto rigor lógico, precisão matemática na geração de esquemas estruturados e excelente orquestração de ferramentas (tool calling).
   - **`gemini-3.5-flash`:** Alternativa intermediária robusta, com ótimo equilíbrio de raciocínio para agentes.
   - **`gemini-2.5-flash`:** Versão anterior consolidada e estável, com suporte nativo e comprovado a chamadas de função.

O código do agente (`agente-estudos/app/agent.py`) mantém o `gemini-3.8-flash` como padrão de fallback caso a variável de ambiente não seja informada. Qualquer troca de modelo é feita exclusivamente no arquivo `agente-estudos/.env` através da variável `MODEL`.

### Erro 503 (Serviço temporariamente indisponível)

O erro **503 UNAVAILABLE** indica sobrecarga transitória nos servidores do Google AI Studio para o modelo requisitado. O problema não decorre do código nem da chave de API e costuma normalizar espontaneamente após alguns minutos.

Se o modelo titular `gemini-3.8-flash` estiver passando por um pico de tráfego:
1. Abra o arquivo `agente-estudos/.env`.
2. Altere a variável para um modelo Flash alternativo:
   ```env
   MODEL=gemini-3.6-flash
   ```
3. Reinicie o servidor no terminal (`CTRL+C` e execute novamente `uv run adk web --allow_origins="*"`) para que o novo modelo seja carregado.
4. Quando o pico de tráfego passar, retorne para `MODEL=gemini-3.8-flash`.

### Erro 429 (Limite de cota excedido)

O erro **429 RESOURCE_EXHAUSTED** ocorre quando a conta atinge um dos limites do plano gratuito do Google AI Studio:

1. **Limite por minuto (RPM / TPM):** Envio de muitas requisições ou tokens em uma janela curta de 60 segundos. Basta aguardar de 30 a 60 segundos antes de reenviar o prompt.
2. **Limite diário (RPD):** Esgotamento do teto de requisições por dia no Free Tier (geralmente 20 requisições diárias para determinados modelos).
   
Como as cotas gratuitas do Google AI Studio são contabilizadas de forma independente por modelo, ao atingir o limite diário de um modelo você não precisa parar os testes:
1. Edite o `agente-estudos/.env` e aponte para outro modelo Flash recomendado com cota livre (por exemplo, alternar entre `gemini-3.6-flash`, `gemini-3.5-flash` ou `gemini-2.5-flash`).
2. Reinicie o ADK Web (`CTRL+C` e `uv run adk web --allow_origins="*"`) e continue a execução.

### Erro 401 (Chave não aceita)

Esse erro indica que o Google não aceitou a sua chave de API. Confira, nesta ordem:

1. O arquivo é `agente-estudos/.env` (dentro da pasta `agente-estudos`, não na raiz).
2. O nome da variável é exatamente `GEMINI_API_KEY`, sem espaços antes ou depois do `=`.
3. Você substituiu o `<sua-api-key>` pela chave real, sem os sinais `<` e `>` e sem aspas.
4. `GOOGLE_GENAI_USE_VERTEXAI=FALSE` está escrito assim, para usar a chave do AI Studio.
5. Você reiniciou o ADK Web depois de editar o `.env`. O arquivo só é lido quando o programa inicia.
6. A chave está ativa em [aistudio.google.com/apikey](https://aistudio.google.com/apikey). Se ela vazou em algum lugar público, o Google a bloqueia: gere uma nova.

---

## Contexto e Créditos

Este projeto foi desenvolvido durante a **Imersão Dev: Engenharia de Software na Era da IA**, promovida pela **Alura**, seguindo o roteiro prático e as especificações instruídas por **[John Garrido](https://github.com/johngarrido/alura-imersao-dev-agy)**.

- Concepção e Especificações Originais: O roteiro passo a passo do laboratório, o documento AGENTS.md, a arquitetura base do agente com o Google ADK, a skill plano-de-estudos e a sugestão do desafio da skill revisao-ativa foram concebidos e estruturados pelo instrutor John Garrido e pela equipe da Alura.
- Minha Atuação Prática no Projeto: Atuei no papel de engenheira de software realizando pair programming com agentes de IA (ecossistema Antigravity e modelos Gemini). Minha contribuição prática no ciclo de desenvolvimento incluiu:
  - A execução, teste e configuração do agente tanto no Google Cloud Shell quanto em ambiente local;
  - O diagnóstico e a resolução de não conformidades técnicas durante a auditoria (ajustes de cálculo de calendário para dias da semana, integridade das 6 colunas do CSV e regras de replanejamento com absorção de margem);
  - A implementação prática, testes e empacotamento da skill de extensão revisao-ativa;
  - A estruturação da documentação e a preparação do repositório para versionamento.
