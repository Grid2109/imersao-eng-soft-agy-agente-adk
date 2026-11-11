# Exemplo de Saída: Revisão Ativa de JavaScript (Funções e Escopo)

Abaixo está um exemplo completo calibrado no nível de qualidade esperado:

---

## 🧠 Pacote de Revisão Ativa: JavaScript (Funções, Escopo e Arrow Functions)

**Tópico:** Funções e Escopo em JavaScript · **Nível:** Iniciante/Intermediário · **Total:** 6 Flashcards e Quiz de 5 Questões

---

### 🗂️ 1. Flashcards de Recuperação Ativa

| # | Frente (Pergunta / Desafio) | Verso (Resposta Atômica) |
|---|---|---|
| 1 | Qual é a principal diferença de comportamento do `this` em uma Arrow Function comparada a uma função tradicional? | A Arrow Function herda o `this` do escopo léxico onde foi criada; funções normais definem seu próprio `this` dinamicamente conforme a chamada. |
| 2 | O que acontece se tentarmos chamar uma `function declaration` antes de sua definição no código? | Funciona normalmente graças ao *hoisting* (içamento completo da declaração e do corpo da função). |
| 3 | O que acontece se tentarmos chamar uma `function expression` atribuída a uma variável `const` antes de sua linha de declaração? | Lança um `ReferenceError` porque a variável está na TDZ (*Temporal Dead Zone*). |
| 4 | O que define um *Closure* em JavaScript? | Uma função que "lembra" e mantém acesso às variáveis do seu escopo léxico externo, mesmo após a função externa ter retornado. |
| 5 | Parâmetros com valores padrão (`default parameters`) são avaliados em tempo de compilação ou em tempo de execução? | Em tempo de execução (*call time*), da esquerda para a direita. |
| 6 | Qual método de função permite invocar uma função definindo explicitamente o `this` e passando argumentos como um array? | `.apply(thisArg, [argsArray])`. |

---

### 📝 2. Quiz de Fixação (5 Perguntas)

#### Questão 1: Conceito de Hoisting
Qual das seguintes formas de criação de função pode ser invocada com sucesso antes da linha em que foi declarada no código?
- A) `const soma = function(a, b) { return a + b; };`
- B) `function soma(a, b) { return a + b; }`
- C) `const soma = (a, b) => a + b;`
- D) `var soma = (a, b) => a + b;`

#### Questão 2: Comportamento do Escopo e Variáveis
Analise o trecho a seguir:
```javascript
function contador() {
  let cont = 0;
  return function() {
    cont++;
    return cont;
  };
}
const c1 = contador();
c1();
console.log(c1());
```
Qual será a saída impressa no console?
- A) `0`
- B) `1`
- C) `2`
- D) `undefined`

#### Questão 3: Arrow Functions e Parâmetros Rest
Qual das afirmações sobre *Arrow Functions* é **INCORRETA**?
- A) Arrow functions não possuem seu próprio objeto `arguments`.
- B) Arrow functions não podem ser usadas como funções construtoras com `new`.
- C) Arrow functions sempre exigem a palavra-chave `return`, mesmo em corpos de uma única linha.
- D) Arrow functions têm vinculação léxica de `this`.

#### Questão 4: Parâmetros Padrão e Valores Falsy
Considere o código:
```javascript
function configurar(porta = 3000) {
  return porta;
}
console.log(configurar(0));
```
Qual o retorno da chamada?
- A) `3000`, porque `0` é um valor falsy.
- B) `0`, porque parâmetros padrão só são ativados quando o argumento é `undefined`.
- C) `null`.
- D) Lança um `TypeError`.

#### Questão 5: Closures em Laços de Repetição
Observe o laço abaixo:
```javascript
for (var i = 0; i < 3; i++) {
  setTimeout(() => console.log(i), 100);
}
```
O que será exibido no console após 100ms?
- A) `0`, `1`, `2`
- B) `3`, `3`, `3`
- C) `undefined`, `undefined`, `undefined`
- D) `0`, `0`, `0`

---

### 🔑 3. Gabarito Comentado

<details>
<summary>Clique para conferir o gabarito e as explicações</summary>

1. **Resposta: B** — Apenas `function declaration` sofre hoisting completo de sua assinatura e corpo. Expressões de função em variáveis sofrem hoisting apenas da variável (como `undefined` no caso de `var`, ou entram na TDZ no caso de `const/let`).
2. **Resposta: C** — Devido ao closure, `c1` preserva a referência à variável `cont`. A primeira invocação incrementa para `1` e a segunda para `2`.
3. **Resposta: C** — Incorreta: em arrow functions de expressão única, o retorno é implícito (ex.: `(a, b) => a + b`).
4. **Resposta: B** — Valores padrão do ES6 só são acionados se o valor recebido for estritamente `undefined`. O valor `0` é perfeitamente válido como argumento.
5. **Resposta: B** — Como `var` tem escopo de função e não de bloco, todas as três callbacks do `setTimeout` compartilham a mesma variável `i`, que já vale `3` quando as callbacks executam. Se usasse `let`, a saída seria `0, 1, 2`.

</details>

---

💡 **Dica de estudo:** Se errou a questão 5, revise a diferença entre escopo de bloco (`let`) e escopo de função (`var`) no capítulo de closures!
