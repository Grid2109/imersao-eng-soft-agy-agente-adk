# Fluxo de Trabalho: Geração de Flashcards e Quiz de Revisão Ativa

Siga os passos na ordem para transformar o material de estudo em um pacote de revisão de alta retenção.

---

## Passo 1: Análise e Decomposição do Material

1. Leia atentamente o material fornecido (ou analise o tópico indicado).
2. Identifique os **3 a 6 pontos-chave**:
   - Definições e conceitos centrais.
   - Regras de funcionamento e sintaxe.
   - Diferenças cruciais e comparações ("X vs Y").
   - Armadilhas comuns, erros frequentes e casos de borda.

## Passo 2: Construção dos Flashcards (Recuperação Ativa)

1. Use `load_skill_resource` para consultar `references/tecnicas_recuperacao.md` se precisar calibrar o formato dos cartões.
2. Crie de **5 a 8 flashcards** atômicos:
   - **Frente:** Uma pergunta direta, objetiva e sem ambiguidade. Deve exigir recuperação ativa da memória (evite perguntas de "sim/não").
   - **Verso:** A resposta concisa (1 a 3 linhas no máximo), destacando a palavra-chave ou regra fundamental.
3. Organize os flashcards em ordem lógica de complexidade (dos conceitos básicos às aplicações práticas).

## Passo 3: Elaboração do Quiz de 5 Perguntas

Crie exatamente **5 questões de múltipla escolha** distribuídas nos seguintes níveis de domínio:
* **Questão 1:** Compreensão conceitual direta (definição ou princípio fundamental).
* **Questão 2:** Aplicação prática (como usar ou resolver um problema comum).
* **Questão 3:** Análise de código / cenário (interpretar um trecho ou fluxo de execução).
* **Questão 4:** Identificação de erro ou armadilha (qual o comportamento inesperado ou erro comum).
* **Questão 5:** Síntese / integração (relação com boas práticas ou caso realista).

Para cada questão:
* Formule o enunciado com clareza.
* Ofereça 4 alternativas: **A**, **B**, **C** e **D**.
* Apenas **uma** alternativa deve estar correta.
* Os distratores devem ser plausíveis, baseados em confusões conceituais reais, e não alternativas absurdas.

## Passo 4: Gabarito e Explicações Detalhadas

Para cada uma das 5 perguntas:
1. Indique a alternativa correta (ex.: **Gabarito: B**).
2. Explique em 1 ou 2 frases **por que** a alternativa correta está certa.
3. Se relevante, aponte resumidamente por que os principais distratores estão errados.

## Passo 5: Formatação da Resposta

1. Use `load_skill_resource` para ler `assets/revisao_template.md`.
2. Preencha o template completo com os flashcards, o quiz e o gabarito.
3. Não omita nenhuma seção do template.
