# busca-8-puzzle

Atividade de faculdade sobre métodos de busca com A*.

## Entrada

Para rodar a busca, basta rodar o modulo src

``` bash
python3.6 src
```

Parâmetros válidos:

- modo: O modo de busca (custo_uniforme, a_simples, a_complexo, a_inversoes). O padrão, e mais aprimorado, é a_complexo;
- tamanho: Qual a dimensão do tabuleiro (Ex: se for 3x3, passar 3);
- inicial: Caso queira passar um estado inicial para a busca, informar a lista de valores, sendo 0 a casa vazia (Ex: 1,2,3,4,5,6,7,8,0). Caso vazio,
será gerado um novo estado aleatório;
- objetivo: Caso queira passar um estado objetivo, informat a lista de valores, sendo 0 a casa vazia (Ex: 1,2,3,4,5,6,7,8,0). Caso vazio,
será usado o objetivo padrão com a casa vazia no final;

Para mais informações é possível verificar a ajuda

``` bash
python3.6 src --help
```

Exemplo de busca:

``` bash
python3.6 src --modo=a_complexo --tamanho=3 --inicial=3,1,2,4,7,5,6,8,0
```

## Saída

Ao finalizar a busca, será apresentado:

- O caminho para solucionar o jogo;
- A quantidade de nodos expandidos (que foram identificados durante a busca);
- A quantidade de nodos criados/visitados (que foram analisados, comparados e coletados os filhos, por exemplo);
- O maior tamanho da fronteira durante a busca (tamanho máximo da fronteira);
- O tamanho total do caminho percorrido para chegar na conclusão;
- Tempo decorrido na busca;

------

## Simulações

Para testar o algoritmo de busca, rodamos as seguintes simulações:

| Método                 | Estado inicial    | Qtd movimentos | Nodos expandidos | Tempo decorrido |
|------------------------|-------------------|----------------|------------------|-----------------|
| A* Heurística inversoes| 1,2,3,4,5,6,0,7,8 | 2              | 8610             | 19.15s          |
| A* Heurística simples  | 1,3,5,4,6,2,8,7,0 | 18             | 4179             | 3.89s           |
| A* Heurística completa | 1,3,5,4,6,2,8,7,0 | 18             | 1018             | 0.25s           |
| A* Heurística completa | 7,4,2,1,8,0,5,3,6 | 19             | 826              | 0.18s           |
| A* Heurística completa | 1,2,5,3,0,4,6,7,8 | 22             | 3886             | 3.20s           |
| A* Heurística completa | 7,5,3,4,1,8,2,0,6 | 25             | 12536            | 32,87s          |
| A* Heurística completa | 4,7,5,0,2,1,3,6,8 | 27             | 16715            | 67,88s          |
