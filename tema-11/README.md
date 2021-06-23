# Trilha DevOps e Cloud Basics: Stack ELK - Tema 11
**Objetivo:** Fazer a instalação em conteneires Docker da Stack ELK, gerando uma URL para o Kibana, capturando os logs do processo de pesquisa do twitter, como os termos resultados e a quantidade de resultados.

## Instalação da Stack ELK
Para baixar a stack ELK, é preciso baixar as ferramentas que fazem parte do conjunto, sendo elas o: elasticsearch, kibana e logstash. Para fazer a instalação iremos utilizar o docker compose. A seguir estão os passos necessários da instalação, seguindo como referência a documentação oficial da elastic.co

**1: Construção do docker-compose.yml**

Para instalar o elasticsearch e kibana, iremos utilizar o docker compose, dessa maneira as distribuições instaladas estarão em execução no docker, e não na máquina local. O arquivo docker-compose.yml possui um cluster do elasticsearch e outro do kibana, essa quantidade foi considerada adequada para o tamanho da aplicação. 

**2: Execução do docker-compose**

Para abrir os clusters criados, digite o seguinte comando:
~~~
docker-compose up
~~~

**3: Para testar o elasticsearch**

Abra o localhost:9200, na página web deverá ter um mensagem como esta:
~~~
{
  "name" : "elasticsearch",
  "cluster_name" : "es-docker-cluster",
  "cluster_uuid" : "uUdyDCVARNibrrP2rxV1Fg",
  "version" : {
    "number" : "7.13.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "9a7758028e4ea59bcab41c12004603c5a7dd84a9",
    "build_date" : "2021-05-28T17:40:59.346932922Z",
    "build_snapshot" : false,
    "lucene_version" : "8.8.2",
    "minimum_wire_compatibility_version" : "6.8.0",
    "minimum_index_compatibility_version" : "6.0.0-beta1"
  },
  "tagline" : "You Know, for Search"
}
~~~

**4: Abrir o kibana**

E por fim, para abrir o kibana e ver a configuração visual da stack, digite localhost: 5601.

## Importando o arquivo csv para a stack ELK
Para realizar a importação do arquivo de saída contendo os tweets foi utilizada a biblioteca elasticsearch do python, com isso a conexão e a criação do index se deram na forma de um arquivo .py, que possui a função readTweets() e a função indexTweets(), que serão explicadas logo abaixo.

**1. Importação das bibliotecas necessárias**
~~~
import csv
from collections import deque
import elasticsearch
from elasticsearch import helpers
~~~
- A biblioteca csv será responsável por transformar o arquivo csv lido, em um dicionário;
- A função deque, da biblioteca collections será utilizada para auxiliar na conexão entre o código e o stack ELK;
- A biblioteca elasticsearch e a função helpers, farão a conexão, enviando o dicionário criado a partir do arquivo csv. Com isso, ele será indexado para o Elasticsearch e poderá ser utilizado no kibana para montagem de um dashboard.

**2. Função readTweets()**

Nessa função, o arquivo csv será lido e convertido para um dicionário, sendo lido um dado de cada vez.

**3. Função indexTweets()**
~~~
es = elasticsearch.Elasticsearch()
 
es.indices.delete(index="tweets", ignore=404)
deque(helpers.parallel_bulk(es, readTweets(), index="tweets"), maxlen=0)
es.indices.refresh()
~~~
Por fim, ele cria uma instância do elasticsearch, conectando à aquela que está sendo utilizada, visto que só é uma, então não precisamos defini-la. Ele verifica se já existe um index com o nome de tweets, e caso exista ele deleta para criar um novo. 
Já o helpers faz a importação em lote do dicionário que criamos, passando a instância do Elasticsearch criada, a função que gera o dicionário e nome do index que será criado, nesse caso tweets.
E na última linha, o refresh fica responsável por atualizar o index. 

## Execução do código
Na main do código, nós chamamos a função indexTweets(), para que dessa forma, sempre que o código for executado, ocorra a atualização do índice. É importante salientar que antes de executar o código, é necessário verificar se os contêineres foram iniciados, caso contrário a conexão com o elasticsearch não funcionará. Portanto, precisamos digitar o comando docker-compose up. Em caso de erro: elasticsearch exited with code 78, é necessário digitar o código abaixo no terminal e executar o docker-compose up novamente. Esse erro ocorre devido a baixa memória. 
~~~
sudo sysctl -w vm.max_map_count=262144
~~~

## Dashboard para visualização de dados
Depois de indexar o arquivo de saída para o elasticsearch, foi criado um dashboard no kibana para visualização de dados. Ao todo, há 7 visualizações que podemos encontrar as seguintes informações:
- Tweets count per date: Gráfico que demonstra a relação de tweets por data, é descrito o dia atual e até 8 dias atrás.
- Tweets count per actor: Tabela que demonstra a relação dos 9 atores que tiveram tweets publicados sobre eles, e a contagem dos mesmos.
- Total of tweets: Métrica que demonstra o total de tweets.
- Count of retweets: Métrica que demonstra o total de retweets.
- Count of favourites: Métrica que demonstra o total de favoritos.
- Text of tweets: Painel que demonstra os textos dos tweets em si.
- Count of tweets per user location: Por fim, o gráfico de  barras demonstra a contagem de tweets a partir da localização do usuário. É importante salientar que alguns usuários não colocam a localização precisa e portanto há algumas informações inconsistentes no gráfico. 

### Arquivo de exportação de objetos
Caso queira visualizar o dashboard, há o arquivo objects_exportation.ndjson que inclui todos os objetos criados citados acima e o indíce tweets também, portanto é só seguir os passos abaixo para que você possa visualizar os tweets e importar o index sem precisar rodar o código. 
- Abra o kibana, no menu lateral esquerdo, vá em Management -> Stack Manegement
- Novamente no menu lateral esquerdo, vá em Kibana -> Saved objects
- Por fim, no menu superior direto, terá a opção de import que você selecionará o arquivo .ndjson e todos os objetos e index serão carregados. 

