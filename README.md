<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->
# Scrapper e Identificador de Notícias

#### Aluno: [André Luiz de Mattos Gonçalves](https://github.com/almattos2008/Monografia_bi)
#### Orientador: [Felipe Borges](https://github.com/FelipeBorgesC).

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".


---

### Resumo

Este trabalho tenta capturar as notícias das páginas principais de alguns sites de notícias brasileiros e classificá-los de acordo com temas de notícias encontradas nos
próprios sites de notícias.


### 1. Introdução

O trabalho que segue busca criar um web scrapper eficiênte, que consiga capturar, dos sites de notícias, as chamadas e as identifique de forma eficiênte com modelos já existentes no mercado. 

### 2. Modelagem

Primeiro foi feito um trabalho de capturar as notícias dos sites, buscando uma a uma as chamadas das notícias nos principais sites de notícias. Essas informações são salvas em um banco de dados
MySql. 
Depois essas informações são acessadas no banco de dados e identificadas com dois modelos, facebook/bart-large-mnli e cross-encoder/nli-distilroberta-base, em ambos os casos, 
as notícias foram tokenizadas, retiradas algumas stopwords e traduzidas para o inglês. Elas foram identificadas em Inglês e em Português para que as eficiências fossem comparadas.
Foram capturadas também notícias de economia para que futuramente um modelo pudesse ser trabalhado no caminho de identificar notícias em português com melhor eficiência.
Foram determinadas manualmente cerca de 1000 temas reais (theme) das notícias e outras 1000 foram determinadas automaticamente, retiradas das áreas de economia dos sites de notícias. Dessa forma, fazer uma comparação com o que foi classificado por cada modelo, com o tema real da notícia,.    




### 3. Resultados

Alguns problemas que foram percebidos ao longo do desenvolvimento e que foram endereçados:


* Notícias vazias foram apagadas;
* Caracteres que causam confusão com o SQL como '"' e '%' foram retirados;
* Espaços maiores que de 1 caracter foram apagados;
* Frases menores que 5 palavras também foram ignoradas;
* Quebras de linha "('<\/br>')" também foram evitadas.

Foi observado que as notícias traduzidas para o inglês tiveram um melhor resultado do que aquelas em português, porém os resultados foram bem insatisfatórios de qualquer jeito.

Alguns temas não tiveram número suficiente de ocorrências para chegarmos a alguma conclusão, mas o tema com maior ocorrência que é o de economia teve um resultado muito ruim, com o melhor modelo acertando somente 16,18% das vezes.

O tema de esporte foi o que teve melhor resultado, mesmo sendo ainda insatisfatório. Foram 82 ocorrências tendo, nos dois modelos, com palavras traduzidas, tendo resultado superior a 70%

O modelo 'theme_prediction_face' em inglês teve um resultado levemente superior aos outros.

A tabela abaixo mostra a quantidade de ocorrências de cada tema pesquisado e compara com as predições.

Cada coluna mostra o número de acertos para cada modelo, com sua porcentagem representada logo abaixodo número absoluto de acertos. O total demonstra qual a classificação real do de cada tema, classifição que foi feita pelo autor do trabalho e no tema economia, cerca de 800 registros foram feitos automaticamente, buscando informações diretamente dos temas de economia dos sites. 

| theme          | theme\_prediction\_face\_pt | theme\_prediction\_roberta\_pt | theme\_prediction\_face | theme\_prediction\_roberta | Total |
| -------------- | --------------------------- |--------------------------------| ----------------------- | -------------------------- | ----- |
| Economia       | 150                         | 22                             | 163                     | 124                        | 1007  |
|                | 14,896%                     | 2,185%                         | 16,187%                 | 12,314%                    |       |
| arte           | 4                           | 2                              | 2                       | 4                          | 7     |
|                | 57,143%                     | 28,571%                        | 28,571%                 | 57,143%                    |       |
| ciencia        | 3                           | 0                              | 9                       | 5                          | 18    |
|                | 16,667%                     | 0%                             | 50%                     | 27,778%                    |       |
| clima          | 12                          | 6                              | 7                       | 7                          | 13    |
|                | 92,308%                     | 46,154%                        | 53,846%                 | 53,846%                    |       |
| comida         | 6                           | 0                              | 14                      | 14                         | 15    |
|                | 40%                         | 0%                             | 93,333%                 | 93,333%                    |       |
| educacao       | 8                           | 4                              | 10                      | 7                          | 13    |
|                | 61,538%                     | 30,769%                        | 76,923%                 | 53,846%                    |       |
| eleicoes       | 19                          | 31                             | 45                      | 63                         | 275   |
|                | 6,909%                      | 11,273%                        | 16,364%                 | 22,909%                    |       |
| entretenimento | 30                          | 7                              | 33                      | 37                         | 100   |
|                | 30%                         | 7%                             | 33%                     | 37%                        |       |
| esporte        | 50                          | 19                             | 60                      | 65                         | 82    |
|                | 60,976%                     | 23,171%                        | 73,171%                 | 79,268%                    |       |
| estilo         | 0                           | 0                              | 1                       | 0                          | 1     |
|                | 0%                          | 0%                             | 100%                    | 0%                         |       |
| guerra         | 0                           | 1                              | 4                       | 14                         | 34    |
|                | 0%                          | 2,941%                         | 11,765%                 | 41,176%                    |       |
| justica        | 2                           | 0                              | 8                       | 5                          | 40    |
|                | 5%                          | 0%                             | 20%                     | 12,5%                      |       |
| moda           | 2                           | 0                              | 3                       | 2                          | 5     |
|                | 40%                         | 0%                             | 60%                     | 40%                        |       |
| musica         | 4                           | 8                              | 8                       | 3                          | 10    |
|                | 40%                         | 80%                            | 80%                     | 30%                        |       |
| natureza       | 4                           | 3                              | 14                      | 5                          | 34    |
|                | 11,765%                     | 8,824%                         | 41,176%                 | 14,706%                    |       |
| negocios       | 0                           | 0                              | 26                      | 18                         | 40    |
|                | 0%                          | 0%                             | 65%                     | 45%                        |       |
| policial       | 13                          | 6                              | 2                       | 3                          | 25    |
|                | 52%                         | 24%                            | 8%                      | 12%                        |       |
| politica       | 21                          | 2                              | 43                      | 18                         | 110   |
|                | 19,091%                     | 1,818%                         | 39,091%                 | 16,364%                    |       |
| saude          | 18                          | 4                              | 50                      | 23                         | 97    |
|                | 18,557%                     | 4,124%                         | 51,546%                 | 23,711%                    |       |
| tecnologia     | 18                          | 0                              | 20                      | 18                         | 28    |
|                | 64,286%                     | 0%                             | 71,429%                 | 64,286%                    |       |
| viagem         | 0                           | 0                              | 8                       | 7                          | 12    |
|                | 0%                          | 0%                             | 66,667%                 | 58,333%                    |       |
| violencia      | 36                          | 24                             | 59                      | 51                         | 75    |
|                | 48%                         | 32%                            | 78,667%                 | 68%                        |       |



### 4. Conclusões

Como demonstrado na tabela acima, os modelos não conseguiram alcançar um acerto confortável para fazer predições. Ficando a maior parte abaixo dos 50% de acertos.

Portanto, não foi encontrado um modelo muito eficiente para a identificação de notícias em português.

O modelo "theme_prediction_face" foi que obteve maior resultado, sendo o que teve maior porcentagem de acerto em 15 dos 22 temas escolhidos, seguido do "theme_prediction_roberta" tendo melhor resultado em 6 de 22 temas. Atenção, empates de primeiro lugar são contados para os temas empatados.

O modelo "theme_prediction_face_pt" teve melhor resultado em 3 temas e o  "theme_prediction_robeta_pt" em 1.

Dessa forma podemos concluir que os modelos que as notícias foram traduzidas para o inglês tiveram melhor resultado que os que ficaram simplesmente em português. Isso pode se dever ao fato de que os modelos são feitos para a lingua inglesa, dessa forma perde-se nas predições que são feitas do português em modelos em inglês e possivelmente perde-se também nas traduções feitas para se adequar ao modelo estrangeiro.

Dessa forma, observa-se que é necessário o desenvolvimento de um modelo treinado em português para termos a chance de um resultado mais robusto.

  





---

Matrícula: 202.100.403

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
