Administração de Hotel com Django REST Framework
<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=Em%20Desenvolvimento&color=YELLOW&style=for-the-badge">
</p>

Uma API para administrar hotéis, onde usuários podem se cadastrar como hóspedes ou hoteleiros. Hoteleiros podem criar seus hotéis, quartos e editar suas reservas. Hóspedes podem fazer reservas para algum quarto do hotel.
Deploy da API: [link para o deploy se houver]
🔨 Funcionalidades do projeto:
- 1: Cadastro de usuários como hóspedes ou hoteleiros.
- 2: Hoteleiros podem criar e gerenciar seus hotéis e quartos.
- 3: Hóspedes podem fazer reservas para quartos de hotéis.
- EXTRA: API com autenticação de usuários e administradores, que podem editar o CRUD.
🛠️ Instalação:
- 1: Primeiramente clone esse repositório do projeto.

bash

git clone https://github.com/seu-usuario/seu-repositorio.git

- 2: Com o código já clonado, é recomendado instalar as bibliotecas/dependências em um ambiente virtual.

bash

cd seu-diretorio
python -m venv .venv

- 3: Ative o ambiente virtual.

bash

# No Windows
.venv\Scripts\activate

# No Mac/Linux
source .venv/bin/activate

- 4: Instale todas as dependências:

bash

pip install -r requirements.txt

- 5: Configure o banco de dados (PostgreSQL):

    Certifique-se de ter o PostgreSQL instalado e rodando.
    Crie um banco de dados para a aplicação.

- 6: Configure as variáveis de ambiente no arquivo .env:

env

DEBUG=True
SECRET_KEY=sua-chave-secreta
DATABASE_URL=postgres://seu-usuario:sua-senha@localhost:5432/seu-banco-de-dados

- 7: Aplique as migrações do banco de dados:

bash

python manage.py migrate

- 8: Inicie o servidor Django:

bash

python manage.py runserver

- 9: Configure e inicie o Celery e o Redis:

    Certifique-se de ter o Redis instalado e rodando.
    Inicie o Celery:

bash

celery -A seu_projeto worker -l info

- 10: (Opcional) Rode o Docker:

    Certifique-se de ter o Docker instalado.

bash

docker-compose up --build

Algumas ressalvas:

    O Django por padrão roda na porta 8000, e as dependências já estão configuradas para essa porta.
    Certifique-se de ter o PostgreSQL e o Redis configurados corretamente.
    Os arquivos estáticos e de mídia estão configurados para o ambiente de desenvolvimento.

✔️ Tecnologias utilizadas

    Django REST Framework
    PostgreSQL
    Celery
    Redis
    Docker

<img loading="lazy" src="https://avatars.githubusercontent.com/u/88624922?v=4" width=115><br><sub>João Pedro</sub>