---
name: revisao-ativa
description: Recebe um material, tema ou código de estudo e gera flashcards de recuperação ativa e um quiz interativo de 5 perguntas com alternativas, gabarito e explicações. Use quando a pessoa quiser revisar, testar conhecimentos, criar flashcards ou simular questões sobre um assunto estudado.
---

# [IMPORTANTE] UTILIZAR ESTA SKILL PARA REVISÃO ATIVA E QUIZZES

Esta skill transforma qualquer material de estudo (resumo, anotações, código-fonte, tópicos ou capítulos) em ferramentas de **recuperação ativa**: flashcards diretos e atômicos e um quiz prático de 5 perguntas de múltipla escolha com gabarito comentado.

Aprender com eficácia exige testar a memória em vez de apenas reler o material passivamente.

## Regra de Ativação (Gating Rule)

Verifique se a mensagem ou a conversa contém o **conteúdo a ser revisado**:

| # | Informação obrigatória | Exemplo |
|---|---|---|
| 1 | **Material ou Tema**: texto, código, anotações ou tema bem delimitado | "Estudei sobre Closures em JavaScript" ou texto colado |

* **Se faltar o conteúdo/tema:** **NÃO chame** a ferramenta `load_skill_resource` e não carregue nenhum arquivo de `references/` ou `assets/`. Faça **uma única mensagem**, curta e amigável, pedindo o texto, anotações ou o assunto específico que a pessoa deseja revisar.
* **Se o nível ou foco não for especificado:** assuma o nível intermediário ou geral do tema, declare a suposição brevemente e prossiga.
* **Se o conteúdo estiver presente:** prossiga imediatamente para as instruções abaixo.

## Instruções (apenas depois que o gating for satisfeito)

1. Use a ferramenta `load_skill_resource` para ler `references/workflow.md`.
2. Siga **estritamente** os passos do `references/workflow.md`. Ele indica o momento certo de carregar `references/tecnicas_recuperacao.md` e `assets/revisao_template.md`.
3. Se for a primeira revisão da conversa, você pode consultar `assets/exemplo_revisao.md` para calibrar o nível de profundidade e clareza esperado.
4. Entregue os flashcards e o quiz de 5 perguntas exatamente na estrutura do `assets/revisao_template.md`.

## Regras gerais

* Responda sempre em **português do Brasil**, tom encorajador, objetivo e focado em aprendizado prático.
* **Atomicidade dos flashcards:** cada flashcard deve cobrir exatamente **um** conceito. Evite perguntas genéricas ou respostas em parágrafos longos.
* **Qualidade do quiz:** 5 perguntas de múltipla escolha (A, B, C, D) com apenas 1 alternativa correta e distratores realistas, acompanhadas de justificativa clara.
* **Código quando relevante:** se o tema envolver programação, inclua pequenos trechos de código limpo e idiomático nas questões.
