# IA-GA
Trabalho desenvolvido na disciplina de Inteligência Artificial
----

# 1 Introdução

1. O que são AG?
Os algoritmos genéticos utilizam conceitos provenientes do princípio de seleção natural para abordar uma série ampla de problemas, em especial de otimização. Inspirado na maneira como o darwinismo explica o processo de evolução das espécies, John Holland decompôs o funcionamento dos AGs nas etapas de inicialização, avaliação, seleção, cruzamento, mutação, atualização e finalização.

* Avaliação: avalia-se a aptidãoo das soluções (indivíduos da população);
* Seleção: indivíduos são selecionados para a reprodução. A probabilidade de uma dada solução ser selecionada é proporcional à sua aptidão;
* Cruzamento: características das soluções escolhidas são recombinadas, gerando novos indivíduos;
* Mutação: características dos indivíduos resultantes do processo de reprodução são alteradas, acrescentando assim variedade à população;
* Atualização: os indivíduos criados nesta geração são inseridos na população;
* Finalização: verifica se as condições de encerramento da evolução foram atingidas

Os Ag possuem uma série de características. As que mais se destacam são:os AGs não trabalham sobre o domínio do problema, mas sim sobre representações de seus elementos; altp grau de generalidade, paralelismo explícito, busca estocástica, busca cega e facilidade no uso das restrições. 

2. Definições de palavras chaves importantes

* Indivíduos: são a unidade fundamental de um algoritmo genético. Neste trabalho, representamos os indivíduos como cromossomos;
* Genótipo: consiste na informação presente na estrutura de dados que engloba os genes de um indivíduo
* Fenótipo: é o resultado do processo de decodificação do genoma de um indivíduo;
* Grau de adaptação: representa o quão bem a resposta representada por indivíduo soluciona o problema proposto. E calculado por uma função chamada objetivo;
* Grau de aptidão: diz respeito ao nível de adaptação de um indivíduo em relação à população à qual ele pertence;
* Geração: diz respeito ao número de vezes pelas quais a população passou pelo processo de seleção, reprodução, mutação e atualização;
* Elite: é composta pelos indivíduos mais adaptados da população;

3. Pseudocódigo

![image](https://user-images.githubusercontent.com/9114468/151905237-07b5e8f6-62db-44a2-8f7b-6904aaeb5dc7.png)


# 2 Requisitos

Para o desenvolvimento deste trabalho, os seguintes requisitos deveriam ser observados:

* Minimozar a função *f(x) = cos(x) * x + 2*
* Espaço amostral x ∈ [−20,+20]
* Indíduos de 16 bits gerados aleatoriamente bit a bit
* Seleção realizada através de sorteio
* Crossover com taxa igual a 60%
* Mutação com taxa igual a 1%
* Utilizar 10 e 20 gerações
* Realizar Elitismo

# 3 Como rodar

Basta executar o comando

```
python3 main.py
```

# 4 Desenvolvimento

1. Geração da população inicial
Cada gene do indivíduo receberá como valor um elemento do conjunto binário [0, 1] sorteado de forma aleatoriamente uniforme

![image](https://user-images.githubusercontent.com/9114468/151906020-3da8ae19-947a-4043-a7cb-f465baf3f652.png)

2. Decodificação do cromossomo

Antes de passar pela avaliação, o cromossomo deve passar por uma etapa de decodificação. Nesta etapa, é realizado um cálculo para converter seu valor binário para seu número real equivalente e em seguida, o 

3. Avaliação

Cada indivíduo da população é avaliado para que seja determinado o seu grau de adaptação

![image](https://user-images.githubusercontent.com/9114468/151906068-ce097d6e-5ba6-4587-a5a6-191fd70f4c6d.png)

Para o problema vigente, a seguinte

# 5 Resultados

# 6 Conclusões
