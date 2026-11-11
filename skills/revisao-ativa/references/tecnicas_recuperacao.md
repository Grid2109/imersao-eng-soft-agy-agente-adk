# Técnicas de Recuperação Ativa e Criação de Flashcards

A ciência cognitiva demonstra que **tentar recuperar uma informação da memória** produz retenção substancialmente superior à releitura passiva ou marcação com marca-texto.

---

## 1. Princípio da Atomicidade dos Flashcards

Um bom flashcard testa **um único fato ou conceito** (mínima unidade de informação):
* ❌ **Ruim (sobrecarregado):** "O que é o DOM, como selecionamos elementos e como adicionamos eventos?"
* ✔️ **Bom (atômico):** "Qual método do DOM seleciona o primeiro elemento que coincide com um seletor CSS?" → `document.querySelector('seletor')`.

### Benefícios da atomicidade:
* A avaliação de acerto/erro é binária e precisa (você sabe na hora se acertou ou errou).
* Facilita a revisão rápida em ferramentas como Anki, Notion ou cartões físicos.

---

## 2. Padrões Recomendados para Flashcards

1. **Conceito Direto:**
   * *Frente:* "Qual a diferença fundamental entre `let` e `const` em JavaScript?"
   * *Verso:* "`let` permite reatribuição de valor; `const` cria uma referência imutável (não pode ser reatribuída)."
2. **Preenchimento de Lacuna (Cloze Deletion mental):**
   * *Frente:* "Em JavaScript, o método de array que retorna um novo array transformado chama-se ______."
   * *Verso:* "`.map()`"
3. **Previsão de Saída (Output Prediction):**
   * *Frente:* "Qual o retorno de `typeof null` em JavaScript?"
   * *Verso:* `'object'` (comportamento histórico legado da linguagem)."

---

## 3. O Efeito de Teste no Quiz

O quiz de 5 perguntas funciona como um teste de consolidação imediata:
* Reduz a ilusão de competência (a sensação falsa de que "já sei o assunto só porque acabei de ler").
* Cria pontos de ancoragem para revisões futuras no cronograma espaçado.
