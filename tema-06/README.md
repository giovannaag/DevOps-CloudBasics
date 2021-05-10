# Trilha DevOps e Cloud Basics: Python - Tema 06

O objetivo do tema é utilizar bibliotecas do python e a API do twitter para recuperar os últimos 10 tweets sobre os 10
atores que mais fizeram filmes nos últimos 10 anos, a partir dos datasets disponíveis no site do IMDB. A explicação do presente
código será descrita nos tópicos seguintes.

## O que é necessário?

### 1º  - Bibliotecas do Python
O código utiliza duas bibliotecas para sua execução: Pandas para análise e manipulação dos dados e Tweepy para uso da API
do twitter. 

### 2º - Datasets
Foram utilizados três datasets disponibilizados pela IMDB, são eles: title.principals, title.basics e name.basics. O download pode 
ser feito nesse [link](https://datasets.imdbws.com/). Após o download, é necessário salvar os arquivos em uma pasta nomeada <b>datasets</b>, logo
o caminho dos arquivos deve seguir as seguintes estruturas:

#### Arquivo [title.principals.tsv.gz](https://datasets.imdbws.com/title.principals.tsv.gz)

Diretório: datasets/title.principals/data.tsv
  
#### Arquivo [title.basics.tsv.gz](https://datasets.imdbws.com/title.basics.tsv.gz)

Diretório: datasets/title.basics/data.tsv

#### Arquivo [name.basics.tsv.gz](https://datasets.imdbws.com/name.basics.tsv.gz)

Diretório: datasets/name.basics/data.tsv

## Como é o funcionamento do código?
O código está estruturado em três arquivos .py, são eles: movies_analysis.py, tweets_analysis.py e main.py. A seguir, será descrito a função de cada um.

### - movies_analysis.py
Este arquivo é responsável pela análise dos datasets da IMDB, utilizando três funções que selecionam as informações necessárias para retornar uma lista com os 10 atores que mais fizeram filmes nos últimos 10 anos, para que, no arquivo tweets_analysis.py, seja recuperado os últimos 10 tweets correspondentes a cada ator da lista. O comportamento de cada função será explicado nos tópicos abaixo.

#### select_movies()
Esta função lê o dataset title.basics, que contém todos os filmes e seriados registrados na base do IMDB. Após a leitura, ele gera um dataframe que ṕassa por um processamento, ou seja, é selecionado apenas os filmes que tenham sido lançados nos últimos 10 anos, utilizando a variável last10years para localizar os filmes somente acima ou igual aos últimos 10 anos. Por fim, é retornado esse dataframe.  

#### select_cast(movies_dataframe)
Esta função irá receber o dataframe gerado pela função select_movies() e irá ler o dataset title.principals que contém o cast dos filmes, esse dataset também passa por um processamento que selecionará somente os dados da categoria de ator ou atriz, gerando um dataframe filtrado do cast. Após isso, é realizado um merge entre o dataframe dos filmes, recebido por parâmetro, e o dataframe do cast, recém gerado. Dessa maneira, será gerado um dataframe contendo somente os atores e atrizes presentes nos filmes lançados nos últimos 10 anos. 

#### top10_actors()
Em um primeiro momento, esta função irá gerar um movies_dataframe a partir da função select_movies() e também irá gerar um cast_dataframe a partir da função select_cast(), passando o movies_dataframe como parâmetro. Após isso, será lido o dataset name.basics que contém as informações básicas de todas pessoas registradas na base do IMDB, gerando o names_dataframe. E para retornar o top 10 atores que mais fizeram filmes nos últimos 10 anos, é utilizado o cast_dataframe para contar a quantidade com que cada código identificador (nconst) se repete. Dessa maneira, é gerado um dataframe top10_actors_dataframe com os 10 códigos que mais se repetiram. 

Agora, é preciso relacionar esses códigos dos top 10 atores com os seus respectivos nomes, para isso, é feito um merge entre o names_dataframe e o top10_actors_dataframe, gerando o dataframe top10_actores. Por fim, esse dataframe contendo o top 10 atores que mais fizeram filmes nos últimos 10 anos é convertido em uma lista somente com os nomes dos atores, que é retornada pela função.  

### - tweets_analysis.py 
Este arquivo é responsável pela seleção dos tweets a partir da lista de atores gerada pela função top10_actors() do arquivo movies_analysis.py. Utilizando a API do twitter para fazer a recuperação dos dados necessários. Contém duas funções que serão descritas abaixo.

#### authentication()
Esta função irá ler um arquivo.txt que contém as chaves de acesso para o uso da API do twitter, retornando um objeto do tipo tweepy.api.API, que será utilizado para executar as funções oferecidas pela API.

#### select_tweets(top10_actors)
Em um primeiro momento, esta função atribui a função authentication à variável api, para realizar a autenticação e fazer o uso da api. Essa variável possibilitará fazer as buscas necessárias para recuperar os tweets desejados. Após isso, é criado o dicionários tweets_dict que contém as principais chaves da estrutura de um tweet, que será usado para armazenar os tweets encontrados. 

Agora, para finalmente encontrar os tweets dos 10 atores que mais fizeram filmes nos últimos 10 anos, percorremos a lista dos nomes dos atores, que é recebida por parâmetro como top10_actors. Para percorrer, é criado um laço for que a cada iteração é realizado uma busca nos tweets, contendo como query o nome do ator ou atriz. Essa busca ocorre a partir da função Cursor() oferecida pela biblioteca Tweepy. É delimitado a busca de 10 tweets para que nosso propósito de recuperar os últimos 10 tweets se mantenha.

Posteriormente, é criado um novo laço for, ainda dentro do primeiro laço, para percorrer os tweets encontrados pelo Cursor. Dentro dele, também há outro laço responsável por percorrer as chaves de cada tweet encontrado, armazenando os valores no dicionário criado anteriormente (tweets_dict). 

Por fim, após percorrer toda a lista de atores e atrizes, convertemos o dicionário de tweets em um dataframe chamado de tweets_dataframe que é convertido num arquivo.csv, armazenado no diretório tweets e nomeado de tweetsTop10Actors.csv. 

### - main.py
Este arquivo é responsável por executar as funções criadas, em um mesmo local. Consiste na importação da função top10_actors() do arquivo movies_analysis.py, atribuindo o retorno dessa função na variável actorsList. E também, importa a função select_tweets() do arquivo tweets_analysis.py, passando como parâmetro a variável actorsList, o que irá gerar o arquivo.csv contendo os últimos 10 tweets dos 10 atores que mais fizeram filmes nos últimos 10 anos.  
