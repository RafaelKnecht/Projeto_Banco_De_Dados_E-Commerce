#  Projeto E-Commerce (Python + MySQL)
 
Este projeto é uma implementação de um sistema de e-commerce prático, desenvolvido para a disciplina de Projeto de Banco de Dados.
 
O objetivo principal foi integrar um banco de dados **MySQL** com uma interface de terminal controlada por **Python**. O projeto aplica conceitos essenciais de SQL, incluindo tabelas, constraints, triggers, functions, procedures e views, gerenciados por um programa interativo.
 
## Integrantes do Grupo
 
* **João Marcos Pessoa Silva**
* **Miguel Luis Vieira De Melo Boa Viagem**
* **Rafael Andrade Knecht**
* **Vinicius Nunes Ananias Helcias Rodrigues**
 
 
---
 
## Sobre o Sistema
 
O sistema simula o back-end e a lógica de negócios de uma loja virtual, capaz de armazenar e gerenciar informações sobre:
 
* **Clientes:** Com dados cadastrais, incluindo restrição para sexo (`'M'`, `'F'` ou `'O'`).
* **Clientes Especiais:** Tabela separada para clientes que ganham `cashback`.
* **Vendedores:** Que podem ser pessoa física (`PF`) ou jurídica (`PJ`).
* **Produtos:** Com nome, descrição, estoque e valor.
* **Vendas:** Registrando o cliente, vendedor, transportadora e valor total.
* **Logs de Eventos:** Para auditoria automática das ações dos *triggers*.
 
###  Tecnologias Utilizadas
 
* **Linguagem de Banco de Dados:** MySQL
* **Linguagem de Programação:** Python
* **Conector:** `mysql-connector-python`
 
---
 
##  Funcionalidades da Interface (Python)
 
O script principal (`main.py`) oferece uma interface de menu simples no terminal para interagir com o banco de dados.
 
| Opção | Descrição |
| :---: | :--- |
| **1** | Cadastrar novo cliente |
| **2** | Listar todos os clientes |
| **3** | Cadastrar novo produto |
| **4** | Listar todos os produtos |
| **5** | Registrar uma nova venda |
| **6** | Executar `PROCEDURE` de reajuste salarial |
| **7** | Executar `PROCEDURE` de sorteio de clientes |
| **8** | Consultar `VIEW` de vendas por vendedor |
| **9** | Consultar `VIEW` de clientes especiais |
| **0** | Sair do sistema |
 
---
 
##  Lógica de Negócio (Triggers, Functions e Procedures)
 
O próprio banco de dados executa regras complexas de forma automática:
 
| Recurso | Descrição |
| :--- | :--- |
| **Trigger (`trg_cliente_especial`)** | Se uma venda for **acima de R$ 500,00**, o cliente recebe **2% de cashback** e é adicionado à tabela `cliente_especial`. |
| **Trigger (`trg_vendedor_especial`)** | Se uma venda for **acima de R$ 1000,00**, o vendedor recebe um **bônus salarial de 5%** e é adicionado à tabela `funcionario_especial`. |
| **Trigger (`trg_remover_cliente_especial`)** | Automaticamente remove o cliente de `cliente_especial` caso o seu saldo de cashback seja **zerado**. |
| **Function (`Calcula_idade`)** | Retorna a idade exata de um cliente com base na `data_nascimento`. |
| **Procedure (`Venda`)** | Reduz a quantidade do produto no estoque após cada registro de venda. |
| **View (`vw_vendas_por_vendedor`)** | Tabela virtual que exibe a quantidade e o valor total de vendas agrupadas por vendedor. |
 
---
 
##  Diagrama do Banco de Dados
 
A estrutura do banco de dados foi modelada para garantir a normalização e o correto relacionamento entre as entidades.
 
 
 
---
 
##  Como Executar
 
Para rodar este projeto em seu computador, siga os passos abaixo:
 
1.  **Baixe o Projeto**
    * Faça o download ou clone deste repositório para sua máquina local.
 
2.  **Inicie o Servidor de Banco de Dados**
    * Certifique-se de que seu servidor **MySQL** local (via XAMPP, WAMP, MySQL Workbench, etc.) esteja **ligado e funcionando**.
 
3.  **Crie e Popule o Banco de Dados**
    * Use seu cliente de banco de dados preferido para se conectar ao servidor.
    * Execute o arquivo `.sql` (o script com `CREATE TABLE`, `INSERT`, etc.). Isso criará o banco de dados `ecommerce`, todas as tabelas e inserirá os dados de teste.
 
4.  **Configure a Conexão no Python**
    * **Abra o(s) arquivo(s) `.py`** do projeto.
    * Encontre e atualize as credenciais de conexão (`host`, `user`, `password`, `database`) para que correspondam exatamente às configurações do seu servidor MySQL local.
 
5.  **Instale as Dependências e Execute**
    * Abra um terminal na pasta do projeto.
    * Instale a biblioteca de conexão SQL:
        ```bash
        pip install mysql-connector-python
        ```
    * Execute o programa principal:
        ```bash
        python main.py
        ```
