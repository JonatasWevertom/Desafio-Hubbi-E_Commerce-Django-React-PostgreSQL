# E-Commerce Django React

## Back-End

### PostgreSQL

1. Instale o PostgreSQL e suas dependencias para ver o banco de dados em tempo real.
    - PostgreSQL: "https://www.postgresql.org/download/"
    - PGAdmin4: "https://www.pgadmin.org/download/"
    - psycopg2: `pip install psycopg2`
    (Este comando só é necessario caso os requirements falhem em instalar a dependencia.)
    - Para criar um banco de dados, se estiver usando o PGAdmin4 basta criar um usuario do banco e depois criar um banco dentro de databases na coluna esquerda clicando com o botao direito do mouse e depois clicando em create database.
    
### Django

1. Instalar um virtual enviroment de sua preferencia como anaconda ou vitualenv.
    (Recomendado em caso de usar diferentes versões de dependencias e blibliotecas em um mesmo dispositivo.)
    - Anaconda: "https://www.anaconda.com/"
    - VirtualEnv: "https://virtualenv.pypa.io/en/latest/installation.html"
    - Crie seu ambiente virtual e o inicie, nas documentações acima ensina a inicializar em cada caso.

2. Instalar os requirements para baixar todas dependencias da aplicação.
    - Estando no diretorio .../backend/algoritimos/ execute o comando o comando: `pip install -r requirements.txt`
    
3. Colocar o servidor no ar.
    - Estando no diretorio .../backend/algoritimos/src/e_commerce_app execute o comando `python manage.py runserver`
    
## Frontend
 
### JavaScript
 
1. Instale o node.js em sua maquina de preferencia o lts
    - Node.js: "https://nodejs.org/en/"
    
2. Instalar dependencias
    - Estando no diretorio .../frontend/algorimitos/ execute `npm install`
    
3. Executar servidor frontend
    - Execute o comando `npm start`
    
## Geral
 
1. Opções de paths para acessar no frontend após criação de usuario (/login para criar o usuario ou logar caso ja tenha conta)
    - /
    - /member
    - /previewImages
    - /cartView
    - /detail_product
    - /product
    - /seller_product_list
    - /login
    - /signup
