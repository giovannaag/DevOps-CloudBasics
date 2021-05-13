# Trilha DevOps e Cloud Basics: Linux and Bash - Tema 07
O objetivo do tema é rodar o código do tema 06 de forma agendada e sincronizar os arquivos de saída com o bucket S3 da AWS. Para tanto, foi criado um script Bash para automatizar a execução do código, em seguida...

## O que é o Bash?
Bash é o shell mais utilizado do Linux. E shell, que nesse caso estamos falando do Bash, é um interpretador de comandos. É a comunicação entre o usuário ou as aplicações desenvolvidas com o núcleo do sistema operacional, conhecido como kernel, essa comunicação se dá atráves do terminal de comandos.

## Para que serve um script?
Script em resumo é um conjunto de instruções que são interpretadas e executam determinada tarefa. Portanto, de modo simples, um script serve para automatizar a execucação de tarefas. 

## Como criar um script Bash?
Iremos fazer um exemplo teste para criar um script Bash. É preciso utilizar qualquer editor de texto que deseja, iremos utilizar o vim que pode ser executado diretamente no terminal. Abaixo segue os passos necessários.

  **1.**  Abra o terminal e digite o seguinte comando: 
  ~~~ 
  vi nomedoarquivo.sh 
  ~~~
  **2.** Em seguida irá abrir o editor vim, para começar a digitar aperte a tecla **i**.
  
  **3.** A primeira linha do arquivo deve ter o seguinte comando: 
  ~~~
  #!/bin/bash 
  ~~~
  **4.** Depois, você digita os comandos que seu script irá realizar, nesse exemplo iremos mostrar na tela a mensagem "teste", para isso utilizamos o comando **echo**:
  ~~~
  echo "teste"
  ~~~
  **5.** Para sair do modo de inserção, pressione a tecla **Esc** e em seguida a tecla **:**
  
  **6.** Por fim, para salvar e sair do editor digite o comando:
  ~~~
  :wq
  ~~~
  
E agora, para ativar o script e ver se ele está funcionando corretamente abra o terminal e siga os seguintes passos.

**1.** Se entrarmos na pasta que o script foi salvo e digitarmos nomedoarquivo.sh a seguinte mensagem de erro irá aparecer:  <i>command not found</i>. Isso se deve ao fato de que precisamos atribuir a permissão de execução para este arquivo portanto o primeiro passo é digitar o seguinte comando:
~~~
chmod a+x nomedoarquivo.sh
~~~

**2.** Agora se digitarmos o comando abaixo, o nome do arquivo aparecerá em verde e veremos as permissões atribuidas, o que sginifica que ele poderá ser executado.
~~~
ls -l nomedoarquivo.sh
~~~
**3.** Para finalmente executá-lo, é preciso digitar:
~~~
./nomedoarquivo.sh
~~~
Se tudo estiver certo, a saída no terminal deverá ser:
~~~
teste
~~~
