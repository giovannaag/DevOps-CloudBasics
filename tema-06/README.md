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
Esse arquivo é responsável pela análise dos datasets da IMDB, utilizando três funções que selecionam as informações necessárias para retornar uma lista com os 10 atores que mais fizeram filmes nos últimos 10 anos, para que, no arquivo tweets_analysis.py, seja recuperado os últimos 10 tweets correspondentes a cada ator da lista. O comportamento de cada função será explicado nos tópicos abaixo.

#### select_movies()


#### select_cast(movies_dataframe)


#### top10_actors()


### - tweets_analysis.py 
Esse arquivo é responsável pela seleção dos tweets a partir da lista de atores gerada pela função top10_actors() do arquivo movies_analysis.py. Utilizando a API do twitter para fazer a recuperação dos dados necessários. Contém duas funções que serão descritas abaixo.

#### authentication()

#### select_tweets(top10_actors)


### - main.py
Esse arquivo é responsável por executar as funções criadas, em um mesmo local. Consiste na importação da função top10_actors() do arquivo movies_analysis.py, atribuindo o retorno dessa função na variável actorsList. E também, importa a função select_tweets() do arquivo tweets_analysis.py, passando como parâmetro a variável actorsList, o que irá gerar o arquivo.csv contendo os últimos 10 tweets dos 10 atores que mais fizeram filmes nos últimos 10 anos.  
