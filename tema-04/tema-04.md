# Trilha DevOps e Cloud Basics: AWS Basics - Tema 04

### **Para que serve:**

**VPC:** A Virtual Private Cloud da Amazon (VPC Amazon) permite que o usuário inicie recursos em uma rede virtual definida pelo mesmo, essa rede virtual se assemelha a um rede tradicional encontrada em um data center, com os mesmos benefícios de utilizar a infraestrutura dimensionável da AWS. 

**Roles:** Role é como uma identidade que possui políticas de permissões que determinam o que pode ser feito ou não. Ao contrário de ser associada a somente uma pessoa, com senhas ou chaves de acesso, pode ser assumida por qualquer usuário que necessite realizar determinada tarefa, atribuindo diferentes permissões. 

**NAT:** Os dispositivos NAT permitem que instâncias em uma sub-rede privada se conectem a internet ou a outros serviços da AWS, porém evita que a internet se conecte a uma dessas instâncias. 

**Security Gateways:** Permite a comunicação entre a VPC e a internet. Suas funcionalidades são fornecer um destino nas tabelas de rotas da VPC para o tráfego na internet e executar a NAT para instâncias com endereços IPv4 públicos. 

**Routes:** São regras que servem para determinar para que lugar o tráfego de rede de uma sub-rede ou gateway é direcionado. 

### **O que é VPC Peering e quando devemos utilizá-lo?**
VPC Peering é uma conexão de rede entre duas VPCs, que permite rotear o tráfego entre eles usando endereços privados IPv4 ou IPv6. Devemos utilizá-lo quando precisamos realizar um compartilhamento de recursos ou arquivos de um VPC, ou uma transferência de dados entre VPCs na mesma conta da AWS, de diferentes contas da AWS ou diferentes regiões. 
