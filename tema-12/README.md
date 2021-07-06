# Trilha Devops e Cloud Basics: Terraform - Tema 12

**Objetivo:** Usando Terraform, gere o código para criar todo o seu ambiente dentro da AWS do zero.

## Instalação do Terraform
O primeiro passo é instalar o Terraform, para tanto foi consultada a documentação oficial e os seguintes passos foram reproduzidos.

**1.** Verificação se o sistema está atualizado e instalação dos pacotes gnupg, software-properties-common e curl. Para isso:
~~~
sudo apt-get update && sudo apt-get install -y gnupg software-properties-common curl
~~~

**2.** Adição da chave HashiCorp GPG.
~~~
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
~~~

**3.** Adição do repositório oficial HashiCorp Linux.
~~~
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
~~~

**4.** Atualização dos pacotes para adicionar o repositório e instalação do Terraform CLI.
~~~
sudo apt-get update && sudo apt-get install terraform
~~~

**5.** Para verificar se a instalação deu certo, basta digitar o comando abaixo em que aparecerá os subcomandos disponíveis do terraform.
~~~
terraform -help
~~~

## Provisionamento da instância EC2 e instalação do Jenkins
Para subir uma instância EC2 pelo terraform, o código foi dividido em dois arquivos, instance.tf e variables.tf, que serão explicados a seguir.

### instance.tf
Esse arquivo é responsável por fazer o provisionamento da instância EC2, conta com a definicação do provedor, que nesse caso é a aws, definindo sua região e perfil do usuário. Em seguida há a criação dos grupos de segurança, do par de chaves e da instância em si. Neste momento, o provisionador remote-exec chama um script para executar comandos remotos. Portanto, nesse bloco faz a instalação do jenkins, do git, do docker e do docker-compose na máquina criada. Além disso, ele sobe os clusters do kibana e do elasticsearch, com o docker-compose up.

### variables.tf
Esse arquivo determina as variáveis usadas no arquivo principal do provisionamento da instância. Foi criado por motivos de organização e descreve a região que a instância será implementada, as credencias da aws, o perfil do usuário, nome da instância, ami e o tipo que será usado.

Agora, para validar o código e executá-lo são necessários três comandos do terraform:

**1.** O comando terraform init é usado para inicializar um diretório de trabalho contendo os arquivos de configuração do Terraform. Este é o primeiro comando que deve ser executado após escrever uma nova configuração do Terraform ou clonar uma existente.
~~~
terraform init
~~~

**2.** O comando plano de terraform cria um plano de execução. Nele, é possível visualizar o que será feito antes da execução em si.
~~~
terraform plan
~~~

**3.** Por fim, o comando terraform apply executa as ações propostas em um plano do Terraform.
~~~
terraform apply
~~~

Em seguida, basta ir ao console da AWS e verificar se a instância foi criada. É possível conectar à nossa instância EC2 por SSH por meio de um nome DNS público, basta digitar o seguinte comando:
~~~
ssh -i <nome da private key> ec2-user@<dns público>
~~~

Agora iremos verificar a instalação do Jenkins, para tanto acessaremos o Jenkins por meio do navegador da web usando o nome / endereço IP DNS público: 8080

## Configuração do Jenkins
Após seguir todos os passos acima, é preciso configurar o Jenkins.

**1.** Será solicitada a senha do administrador para ter acesso a ela, digite o seguinte comando no terminal:
~~~
sudo cat /var/lib/jenkins/secrets/initialAdminPassword
~~~
Copie o código gerado e cole no campo da página do Jenkins.

**2.** Na página de **Customize Jenkins**  clique em **Install Suggested Plugins**

**3.** Crie um usuário administrador e **Save and Continue**

**4.** Na parte inicial do Jenkins, clique em **Manage Jenkins** e depois em **Manage Plugins**

**5.** Na aba de **Available**, busque por **Amazon EC2** a selecione e clique em **Install without restart**

**6.** Após a instalação, clique em **Back to dashboard** e clique na opção **Configure a Cloud**

**7.** Clique em **Add a new cloud** e depois em **Amazon EC2**

**8.** Por fim, preencha os campos solicitados utilizando as **key pair da AWS Credentials.**

Também é necessário, dar permissão ao usuário Jenkins para executar ações sudo. Para isso, no terminal da EC2 digite o seguinte comando
~~~
sudo vi /etc/sudoers
~~~

Nesse caso, utilizei o editor vim, mas é possível utilizar outros como o nano. Depois do comando acima, adicione a linha abaixo no final do arquivo.
~~~
jenkins ALL=(ALL) NOPASSWD: ALL
~~~

## Criando JOB
Para criar um novo job é necessário seguir os passos abaixo:

**1.** Clique em **New Item**, no menu à esquerda. Depois é preciso preencher um nome para esse job e o tipo dele. Iremos selecionar a opção **Pipeline** e clicar em **Ok.**

**2.** A partir desse passo, iremos configurar o pipeline criado.

**3.** Na aba **General**, selecione a opção **GitHub Project** e em **Project url** preencha a url do seu projeto do GitHub.

**4.** Na aba **Build Triggers**, selecione a opção **GitHub hook trigger for GITScm polling.**

**5.** Em seguida, na aba **Pipeline**, na opção de Definition selecione **Pipeline script from SCM** e na opção **SCM** selecione **Git**. Será solicitado a url do repositório e caso seja um repositório privado, é preciso digitar suas credenciais do git (username e password).

**6.** Verifique a branch que você gostaria de puxar, nesse exercício utilizamos a **master** mesmo.

**7.** E na aba de **Script Path**, certifique-se que o nome do arquivo Jenkins está correspondente ao do que se deseja executar.

**8.** Por fim, clique em **Save**.

## Jenkins File 
Para rodar a aplicação, foi criado um Jenkins File, que a partir do código no github, irá executar os comandos atráves dos estágios abaixo:
- **Prepare to build:** Verifica se o docker está ativo e inicia os containers do elasticsearch e do kibana.
- **Prepare enviroment:** Instala as bibliotecas necessárias para rodar o tema e as credenciais da AWS para fazer o sync.
- **Build:** Roda a aplicação, main.py
- **Deploy:** Faz o sync do arquivo de saída com o bucket da AWS e exporta os objetos do kibana do tema 11, para o elasticsearch.

## Visualização no Kibana
Para visualizar os objetos enviados, incluindo o dashboard, é necessário acessar o kibana atráves do comando abaixo:
~~~
http://<IPv4 da instância>:5601
~~~
- No menu lateral, na aba do kibana, vá em dashboard
- Aparecerá o dashboard Tema 11, clique nele para visualizar
- Para ver os outros objetos salvos, no menu lateral, na aba do kibana, vá em saved objects
- Terá uma lista com todos os objetos importados
