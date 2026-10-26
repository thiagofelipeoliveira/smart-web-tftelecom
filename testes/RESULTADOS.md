# Resultados dos testes do classificador

26 frases de teste que **não fazem parte do treino**, escritas como clientes reais escrevem: com erros de digitação ("internete", "bolto"), gírias ("a net tá lenta") e sem acento.

| Versão | Técnica | Acertos | Acurácia |
|---|---|---|---|
| v1 | Lista de palavras-chave | 19/26 | 73% |
| **v2 (atual)** | **Naive Bayes + correção de digitação + bigramas** | **24/26** | **92%** |

**Detecção de urgência:** 26/26 (100%).

## Erros restantes (v2) e o que eles ensinam
| Frase | Esperado | Resultado | Por quê |
|---|---|---|---|
| "sinal fraco no segundo andar" | Suporte | Geral | "fraco" não aparece no treino e "segundo" foi corrigido para "segunda" (de "segunda via") |
| "preciso do comprovante pra empresa" | Financeiro | Geral | "comprovante" aparece só 1 vez no treino e "empresa" puxa para Vendas |

Como melhorar: acrescentar em `TREINO` frases reais que chegam no WhatsApp da empresa. Quanto mais exemplos, maior a acurácia. Não é preciso mudar o código.

## Como rodar
```bash
pip install playwright
playwright install chromium
python testes/avaliar_classificador.py
```

---

# Auditoria de acessibilidade e qualidade

Ferramenta: **axe-core** (a mesma usada pelo Google Lighthouse), com regras WCAG 2.1 A/AA e boas práticas.

| Página / estado | Violações WCAG A/AA |
|---|---|
| Site completo (protótipo) | **0** |
| Assistente: quiz, resultado, classificador e alto contraste | **0** |
| Botão de WhatsApp | **0** (antes: contraste 4,3:1 → verde escurecido, agora 5,4:1) |

O único aviso restante no assistente, "a página deveria ter um título H1", é esperado: o assistente é um componente dentro da página do Framer, e o H1 fica no Hero do site.

Outras verificações automáticas:
- Nenhum ID duplicado no HTML.
- Todas as âncoras do menu apontam para seções existentes.
- Todos os links de WhatsApp usam o número 5549920023806, e o telefone fixo é `tel:+554933296270`.
- Navegação por teclado: as setas trocam de aba, Espaço marca uma opção e Enter avança.
- A validação do formulário leva o foco ao campo com erro.
- Proteção contra código malicioso: um nome digitado como `<b>x</b>` aparece como texto, sem ser executado.
