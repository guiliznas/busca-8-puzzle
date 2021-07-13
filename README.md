# busca-8-puzzle
Atividade de faculdade sobre métodos de busca com A*.

# Execução
Para rodar a busca, basta rodar o modulo src
```
python3.6 src
```

Parâmetros válidos:
- modo: O modo de busca (custo_uniforme, a_simples, a_complexo);
- tamanho: Qual a dimensão do tabuleiro (Ex: se for 3x3, passar 3);
- inicial: Caso queira passar um estado inicial para a busca, informar a lista de valores, sendo 0 a casa vazia (Ex: 1,2,3,4,5,6,7,8,0). Caso vazio, será gerado um novo estado aleatório;
Para mais informações é possível verificar a ajuda
```
python3.6 src --help
```

Exemplo de busca:
```
python3.6 src --modo=a_complexo --tamanho=3 --inicial=3,1,2,4,7,5,6,8,0
```

# Resultado

Ao finalizar a busca, será apresentado:
- O caminho para solucionar o jogo;
- A quantidade de nodos expandidos (que foram conhecidos durante a busca);
- A quantidade de nodos criados (que foram analisados, comparados e coletados os filhos, por exemplo);
- O máximo de nodos abertos simultaneamente na fronteira;
- O tamanho total do caminho percorrido para chegar na conclusão;

------





Entrada:
- Um tabuleiro desordenado (com o espaço vazio em qualquer lugar)
- Algoritmo de busca

Saída esperada:
- O total de nodos visitados
- O total de nodos expandidos/criados
- O maior tamanho da fronteira durante a busca
- O tamanho do caminho
  
Tipos de buscas esperadas:
- Custo uniforme (sem heurística)
- A* com uma heurística simples
- A* com a heurística mais precisa que conseguir

Relatório:
- Representação do estado (estrutura de dados)
- Estrutura e dados para a fronteira e nodos fechados
- Descrição das heurísticas e simulações de seus valores
  - Breve descrição da implementação
- Como foi gerenciada a fronteira, verificações, quais estapas foram feitas ao adicionar um estado (explicar estratégia, respectivos métodos e possibilidades além do que foi implementado)
- Métodos principais e breve descriçãod o fluxo do algoritmo
- Se não alcançou algum objetivo, explicar o que faria VS o que foi feito. Qual problema encontrado e limitações da implementação

Informar referenciais teóricos/práticos.

Para avaliação:
- Utilizar uma estrutura de dados e busca adequada
- Implementar heurística matematicamente
- Considera todo o trabalho realizado, não só a saída

Considerar apenas a solução possível padrão, com o espaço vazio na ultima casa (3:3).


Adicionais:
- Os algoritmos precisam funcionar para qualquer objetivo.
- Necessário montar a estrutura toda de forma genérica (ex: n-puzzle, ser possível executar 15-puzzle).