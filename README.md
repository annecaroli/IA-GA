# ALgoritmo Genético

> Trabalho desenvolvido na disciplina de Inteligência Artificial
>
> Professor Eduardo Max
> 
> Alunas: Anne e Mellyssa
> 
> Ifes - Campus Serra

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

Antes de passar pela avaliação, o cromossomo deve passar por uma etapa de decodificação. Nesta etapa, é realizado um cálculo para converter seu valor binário para seu número real equivalente.

![image](https://user-images.githubusercontent.com/9114468/151906508-eea9ddc5-8e07-4ca7-8aa5-d4802f5b7a29.png)

3. Função objetivo

Em seguida, o valor real é normalizado para estar no dentro do domínio proposto nos requisitos.

![image](https://user-images.githubusercontent.com/9114468/151906633-469463f7-46ac-43d3-9a80-8e0de2dce52b.png)


4. Avaliação

Cada indivíduo da população é avaliado para que seja determinado o seu grau de adaptação

![image](https://user-images.githubusercontent.com/9114468/151906068-ce097d6e-5ba6-4587-a5a6-191fd70f4c6d.png)

5. Seleção

A seleção é a responsável pela perpetuação de boas características na espécie. Para o problema vigente, a seleção é realizada através de torneio, os se escolhem dois indivíduos aleatoriamente e o mais adaptado é selecionado.

![image](https://user-images.githubusercontent.com/9114468/151906935-54c5ef43-771b-4a47-9a24-c71bf442480c.png)

6. Crossover

O crossover tem como objetivo propagar os esquemas mais adequados na população e para isso foi determinado que fosse realizado através de um ponto de corte, a ser escolhido aleatoriamente.

![image](https://user-images.githubusercontent.com/9114468/151907067-e7505d83-9130-4f08-be54-ade54273a1cb.png)


7. Mutação

A mutação opera sobre os indivíduos resultantes do processo de cruzamento e com uma probabilidade pré-determinada em 1% efetua algum tipo de alteração em sua estrutura

![image](https://user-images.githubusercontent.com/9114468/151907140-be307e1b-695c-4e49-bdcf-5280624a3d0b.png)


# 5 Resultados

# 6 Conclusões
