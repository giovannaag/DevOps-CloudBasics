# Trilha DevOps e Cloud Basics: Docker - Tema 10

**Objetivo:** Neste tema iremos rodar o código produzido em um container Docker, com base em tudo que foi desenvolvido até o momento. 

## Instalando o Docker
Como primeiro passo iremos instalar o docker localmente, utilizando o repositório oficial do mesmo. Isso para garantir a versão mais recente. Para isso, precisamos adicionar uma nova fonte de pacote, a chave GCP do Docker para garantir os downloads e por fim instalar o pacote. Abaixo segue os passos necessários. 

**1.** Vamos começar atualizando os pacotes já existentes, para tanto digite o seguinte comando no terminal:
~~~
sudo apt update
~~~

**2.** Agora, iremos instalar pacotes que permitem o apt utilizar pacotes pelo HTTPS:
~~~
sudo apt install apt-transport-https ca-certificates curl software-properties-common
~~~

**3.** Em seguida, adicionar a chave GCP do Docker:
~~~
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
~~~

**4.** E adicionar o repositório do docker nas fontes do apt:
~~~
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
~~~

**5.** Por fim, iremos atualizar os pacotes (agora com os pacotes do Docker adicionados):
~~~
sudo apt update
~~~

**6.** Agora, finalmente, instalaremos o Docker, para tanto:
~~~
sudo apt install docker-ce
~~~

**7.** Para verificar se ele está funcionando:
~~~
sudo systemctl status docker
~~~

O resultado deve mostrar que o serviço está ativo (aparece em verde).

### Executando os comandos Docker sem sudo (opcional)
Por questões de padrão, os comandos Docker só podem ser executados pelo usuário root ou por usuários que estão no grupo docker. Para que seja possível executar os comandos Docker sem necessidade do sudo na frente, é necessário seguir as instruções abaixo, caso queira ter essa liberdade dos comandos.

**1.** Adicionaremos o usuário ao grupo docker com o seguinte comando:
~~~
sudo usermod -aG docker <usuário>
~~~

**2.** Para inscrever o novo membro no grupo, digite:
~~~
su - <usuario>
~~~

**3.** Para conferir que o usuário está no grupo Docker, digite:
~~~
id -nG
~~~

## Instalando o Docker na EC2

Caso queira rodar na EC2 é necessário instalar o docker na instância EC2, utilizando o tutorial da documentação da AWS. Após acessar sua instância EC2, siga os passos abaixo para realizar a instalação do docker. 

**1.** Vamos começar atualizando os pacotes já existentes, para tanto digite o seguinte comando no terminal:
~~~
sudo yum update -y
~~~

**2.** Agora, instalaremos o pacote do Docker Engine na sua versão mais recente:
~~~
sudo amazon-linux-extras install docker
~~~

**3.** E por fim, inicie o docker:
~~~
sudo service docker start
~~~ 

### Executando o comando Docker sem sudo

Por questões de padrão, os comandos Docker só podem ser executados pelo usuário root ou por usuários que estão no grupo docker. Para que seja possível executar os comandos Docker sem necessidade do sudo na frente, é necessário digitar o código abaixo, caso queira ter essa liberdade dos comandos.
~~~
sudo usermod -a -G docker ec2-user
~~~

### Criando o Dockerfile
O dockerfile é o arquivo responsável pela criação da Imagem, ele será o guia do que a imagem irá executar, sendo assim, é a partir dele que podemos gerar o build e criar o container. Abaixo está a explicação de como foi estruturado o código do tema em questão.

~~~
FROM python:3 # Indica a imagem que será utilizada como ponto de partida, nesse caso é o pyhton. 

RUN mkdir /Tema10 # Roda o comando mkdir, responsável por criar a pasta tema 10 que será a pasta raiz quando o container for executado. 
WORKDIR /Tema10 # Muda para o diretório tema10 criado.

RUN pip install awscli # Instala o aws cli para ser possível sincronizar os arquivos de saída com o bucket. 

COPY . /Tema10/ # Copia todos os arquivos do diretório atual para o diretório tema10.

RUN bash aws_credentials.sh #Script para configurar as credenciais da AWS no docker.

RUN pip install -r requirements.txt  # Executa o comando que é responsável por instalar as bibliotecas descritas no arquivo requirements.txt - são elas: pandas, tweepy e wget. Elas são necessárias para execução do código.

CMD [ "python", "main.py" ]  # O comando CMD é responsável por executar a ordem dentro das [ ], no entanto ele só executa quando o container é criado e não no build da imagem.
~~~

### Fluxo de criação do container no terminal local
Antes de rodar o container no Jenkins, foi feito o teste local. Para tanto foram seguidos os passos abaixo:

**1.** Criação da imagem a partir do Dockerfile:
~~~
docker build -t imagem_tema10:1.0 -f Dockerfile .
~~~

**2.** Criação do container a partir da imagem:
~~~
docker run --name tema10_container -t -d tema10:1.0 python
~~~

**3.** Execução do código de verificação dos datasets:
~~~
docker exec -it tema10_container python datasets_verification.py
~~~

**4.** Execução do código de teste das funções da análise dos filmes: 
~~~
docker exec -it tema10_container python -m unittest movies_analysis_test.py
~~~

**5.** E por fim, a execução do código main:
~~~
docker exec -it tema10_container python main.py
~~~

### Criando o Jenkinsfile
Agora, todos esses passos que foram executados na mão pelo terminal local, iremos escrever em um Jenkinsfile que irá rodar um pipeline a partir dele, a fim de automatizar o processo de conteinerização da aplicação. Abaixo estão descritos os stages construídos e a função de cada passo.

- **Declarative: Checkout SCM:** Responsável por clonar e fazer o checkout do repositório do git, salvando o projeto no workspace do Jenkins. Essa etapa já está configurada, por esse motivo, não aparece no JenkinsFile.
- **Prepare to build:** Nessa etapa iremos fazer a instalação do docker e dar permissões para o usuário jenkins, assim como verificar o status do docker e iniciá-lo caso não esteja ativo.
- **Build:** Responsável pela criação da imagem e verificação de container já existente com o mesmo nome do qual será feito o run, em seguida, nesse mesmo stage. 
- **Prepare to test:** Executa o arquivo responsável pela verificação dos datasets, possibilitando o teste em seguida.
- **Test:** Executa o arquivo de teste.
- **Run:** Executa a main e faz a sincronização do arquivo de saída (dos tweets) com o bucket do s3. 
