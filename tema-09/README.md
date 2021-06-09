# Trilha DevOps e Cloud Basics: Jenkins - Tema 09

O objetivo do tema é automatizar o processo de deploy do código do tema 06, puxando o mesmo do reposítorio no github e fazendo o deploy dentro da EC2. Para tanto, iremos utilizar a ferramenta Jenkins, criando um pipeline responsável pela tarefa solicitada. Abaixo, segue as instruções necessárias.

## Preparação da EC2
Primeiramente, é necessário configurar uma porta TCP personalizada para liberar o acesso ao Jenkins. Para isso, crie uma regra no Security Group da sua instância para liberar a porta 8080. Os parâmetros que a regra deve possuir são os seguintes:
  
  - **Type:** CUSTOM TCP
  - **Protocol:** TCP
  - **Port Range:** 8080
  - **Source:** Custom (0.0.0/0)
  - **Description:** Porta Jenkins

## Instalação do Jenkins
Após liberar a porta 8080, iremos fazer a instalação do Jenkins. Para tanto, siga os passos:

**1.** Conecte-se à sua instância EC2

**2.** Atualize os pacotes
~~~
sudo yum update
~~~

**3.** Verifique se o java está instalado, caso contrário, instale o java
~~~
java -version
sudo yum install java-1.8.0
~~~

**4.** Faça o download do repositório do Jenkins
~~~
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
~~~

**5.** Importe um arquivo de chave do Jenkins-CI para permitir a instalação
~~~
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key 
~~~

**6.** Instale o Jenkins
~~~
sudo yum install jenkins
~~~

**7.** Inicie o Jenkins
~~~
sudo service jenkins start
~~~

**8.** Verifique o status do serviço do Jenkins
~~~
sudo systemctl status jenkins
~~~

**9.** Acesse o servidor Jenkins usando o Ipv4 público da sua EC2 na porta 8080, como no exemplo abaixo:
~~~
http://ipv4adress:8080
~~~

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

Também é necessário, dar permissão ao usuário Jenkins para executar ações sudo, tornando possível, por exemplo, a instalação de bibliotecas utilizadas no tema 06. Para isso, no terminal da EC2 digite o seguinte comando
~~~
$ vi /etc/sudoers
~~~

Nesse caso, utilizei o editor vim, mas é possível utilizar outros como o nano. Depois do comando acima, adicione a linha abaixo no final do arquivo.
~~~
jenkins ALL=(ALL) NOPASSWD: ALL
~~~

## Configurações GitHub
Para que o pipeline funcione corretamente, é necessário configurar a webhook no repositório do git. Para tanto, siga as instruções abaixo.

**1.** No github, na página do repositório em questão, vá em **Settings.**

**2.** No menu lateral do lado esquerdo, selecione **Webhooks**

**3.** Clique em **add webhook**

**4.** No campo de Payload URL, digite uma url com a seguinte configuração: http://<public ipv4 address da sua ec2>:8080/github-webhook/

**5.** Verifique se a caixa de seleção **Just the push event** está marcada

**6.** Clique em **Add webhook** no fim.

Agora, cada vez que você fizer um push no repositório em questão, o pipeline será executado automaticamente.

## Criando JOB
Para criar um novo job é necessário seguir os passos abaixo:

**1.** Clique em **New Item**, no menu à esquerda. Depois é preciso preencher um nome para esse job e o tipo dele. Iremos selecionar a opção **Pipeline** e clicar em **Ok.**

**2.** A partir desse passo, iremos configurar o pipeline criado.

**3.** Na aba **General**, selecione a opção **GitHub Project** e em **Project url** preencha a url do seu projeto do GitHub.

**4.** Na aba **Build Triggers**, selecione a opção **GitHub hook trigger for GITScm polling.**

**5.** Na aba **Pipeline**, na opção de Definition selecione **Pipeline script from SCM** e na opção **SCM** selecione **Git**. Será solicitado a url do repositório e caso seja um repositório privado, é preciso digitar suas credenciais do git (username e password).

**6.** Verifique a branch que você gostaria de puxar, nesse exercício utilizamos a **master** mesmo.

**7.** E na aba de **Script Path**, certifique-se que o nome do arquivo Jenkins está correspondente ao do que se deseja executar.

**8.** Por fim, clique em **Save**.

## Jenkins File 
O pipeline criado está dividido em 5 etapas, que serão explicadas a seguir.
- **Declarative: Checkout SCM:** Responsável por clonar e fazer o checkout do repositório do git, salvando o projeto no workspace do Jenkins. Essa etapa já está configurada, por esse motivo, não aparece no JenkinsFile.
- **Prepare enviroment:** Prepara a instância EC2 para a execução do código, instalando as bibliotecas necessárias e criando uma pasta onde será feito o deploy.
- **Test:** Roda o arquivo de teste.
- **Build:** Executa o arquivo.py.
- **Deploy:** Copia todos os arquivos do workspace do Jenkins para a pasta criada na EC2, de maneira que mantém os arquivos sempre atualizados toda vez que o pipeline é executado. Também dá permissão geral para a pasta criada e faz o sync para o s3 do arquivo de saída da execução.


