<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->
# Scrapper e Icentificador de Notícias

#### Aluno: André Luiz de Mattos Gonçalves(https://github.com/almattos2008/Monografia_bi)
#### Orientador: [Felipe Borges](https://github.com/FelipeBorgesC) e [Nome Sobrenome](https://github.com/link_do_github).
#### Co-orientador(/a/es/as): [Nome Sobrenome](https://github.com/link_do_github) e [Nome Sobrenome](https://github.com/link_do_github). <!-- caso não aplicável, remover esta linha -->

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".


---

### Resumo

Este trabalho tenta capturar as notícias das páginas principais de alguns sites de notícias brasileiros e classificá-los de acordo com temas de notícias encontradas nos
próprios sites de notícias.

### Abstract <!-- Opcional! Caso não aplicável, remover esta seção -->

<!-- trocar o texto abaixo pelo resumo do trabalho, em inglês -->

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

Donec molestie, ante quis tempus consequat, mauris ante fringilla elit, euismod hendrerit leo erat et felis. Mauris faucibus odio est, non sagittis urna maximus ut. Suspendisse blandit ligula pellentesque tincidunt malesuada. Sed at ornare ligula, et aliquam dui. Cras a lectus id turpis accumsan pellentesque ut eget metus. Pellentesque rhoncus pellentesque est et viverra. Pellentesque non risus velit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### 1. Introdução

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

### 2. Modelagem

Primeiro foi feito um trabalho de capturar as notícias dos sites, buscando uma a uma as chamadas das notícias nos sites principais. Essas informações são salvas em um banco de dados
MySql. 
Depois essas informações são acessadas no banco de dados e identificadas com dois modelos, facebook/bart-large-mnli e cross-encoder/nli-distilroberta-base, em ambos os casos, 
as notícias foram tokenizadas, retiradas algumas stopwords e traduzidas para o inglês. Elas foram identificadas em Inglês e em Português para que as eficiências fossem comparadas.
Foram capturadas também notícias de economia para que futuramente um modelo pudesse ser trabalhado no caminho de identificar notícias em português com melhor eficiência.

### 3. Resultados

Alguns problemas foram identificados, como notícias vazias, caracteres especiais como '"' etc. Eles foram identificados e impedidos de serem salvos no banco de dados.
Foi observado que as notícias traduzidas para o inglês tiveram um melhor resultado do que aquelas em português

### 4. Conclusões

Não foi encontrado um modelo muito eficiente para a identicicação de notícias em português.

---

Matrícula: 202.100.403

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
