# Trilha DevOps e Cloud Basics: Windows and Powershell - Tema 08
O objetivo do tema é rodar o código do tema 06 de forma agendada e sincronizar os arquivos de saída com o bucket S3 da AWS. Contudo, esse processo deve ser feito em uma VM Windows. Para cumprir o objetivo, após a instalação da VM Windows utilizando o VirtualBox, foi criado um script powershell para automatizar a execução do código e o agendador de tarefas do Windows para realizar o agendamento.

## Preparação da máquina instalada
Após a instalação da máquina, foi necessário realizar as seguintes instalações:
  - Pyhton e as bibliotecas pandas e tweepy, para que fosse possível rodar o código do tema 06 que utiliza essa linguagem e as respectivas bibliotecas;
  - AWS cli e configuração;
  - Git para que fosse possível clonar o repositório e efetuar o versionamento do presente tema, na própria VM criada.
 
### Instalando Python e bibliotecas via powershell
Para fazer a instalação do pyhton foi utilizado o gerenciador de pacotes Chocolatey e este [link](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10) foi utilizado como referência. 
  
  **Instalando chocolatey:**
  ~~~
  $script = New-Object Net.WebClient
  $script.DownloadString("https://chocolatey.org/install.ps1")
  iwr https://chocolatey.org/install.ps1 -UseBasicParsing | iex
  choco upgrade chocolatey
  ~~~
  
- Depois de executar os comandos acima é necessário fechar o powershell e abri-lo novamente.

 **Instalando python:**
 ~~~
 choco install -y python3
 ~~~
 
 Para verificar se ele foi instalado corretamente, digite o comando abaixo para verificar a versão instalada:
 ~~~
 python --version
 ~~~
 
 A saída deve ser como:
 ~~~
 Python 3.9.5
 ~~~
 
 - Depois de executar os comandos acima é necessário fechar o powershell e abri-lo novamente.

**Instalando pip:**

Como gerenciador de pacotes do Python iremos uitlizar o pip, para tanto é necessário instalá-lo com o comando abaixo:
~~~
python -m pip install --upgrade pip
~~~

**Instalando bibliotecas:**

E agora, para baixar as bibliotecas necessárias para execução do código, digite as seguintes linhas de comando:
~~~
pip install pandas
pip install tweepy
~~~

### Instalando AWS CLI e configurando 
Para que seja possível fazer o sync do arquivo de saída com o s3 da aws, é preciso acesso à AWS. Ao instalar o AWS cli temos acesso a todos os serviços e dessa maneira, será possível realizar a tarefa desejada. Para instalar é preciso seguir os passos da documentação oficial, encontrado neste [link](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/install-cliv2-windows.html).

Após a instalação é necessário fazer a configuração com as chaves de acesso, para tanto digite o seguinte comando:
~~~
aws configure
~~~

### Instalando git
O gerenciador de pacotes Chocolatey também foi utilizado para instalar o git. Basta digitar o seguinte comando:
~~~
choco install git 
~~~
Para verificar se ele foi instalado corretamente, digite o comando abaixo para verificar a versão instalada:
~~~
git --version
~~~

## Criando um script Powershell
Iremos fazer um exemplo teste para criar um script Powershell. É preciso utilizar qualquer editor de texto que deseja, iremos utilizar o VSCode com a extensão do Powershell instalada. Abaixo segue os passos necessários.

**1.** Abra o VSCode e selecione a pasta que deseja salvar o script. Após isso, criei um novo arquivo com o nome script_teste.ps1.

**2.** Com o arquivo salvo, o VSCode entenderá que a linguagem utilizada será o powershell e todos os comandos estarão disponíveis. O script terá somente uma mensagem "teste", para isso digite o seguinte comando no arquivo:

~~~
Write-Host "teste"
~~~

**3.** Agora salve o arquivo e abra o Windows Powershell. Entre na pasta que o script foi salvo e digite o seguinte comando para executá-lo:

~~~
.\script_teste.ps1
~~~

**4.** Se tudo estiver certo, a saída no terminal deverá ser:

~~~
teste
~~~

## Agendando uma tarefa no Windows
Para agendar a execucção do script iremos utilizar o agendador de tarefas do windows. Para tanto, siga os passos abaixo.
  1. Entre no agendador de tarefas do Windows (pode ser tanto pelo pesquisa no menu ou apertando win+R e inserindo "taskchd.msc")
  2. Clique em Ação e em Criar Tarefa Básica no menu superior
  3. Insira o nome e descrição da tarefa, em seguida clique em Avançar
  4. Escolha quando você deseja executar
  5. Escolha Iniciar um Programa na sessão Ação
  6. Em Programa/Script, insira o caminho do Powershell: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
  7. Em Adicione argumentos, insira o caminho do script: C:\Users\Giovanna\Desktop\devops-cloudbasics\tema-08\script_tema08.ps1
  8. Faça a revisão e clique em concluir.
  
