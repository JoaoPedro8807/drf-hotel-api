 # Administração de Hotel com Django REST Framework
 
#  🚀 https://hotel-api-ugz3zongra-rj.a.run.app/api/schema/swagger-ui

Uma API para administrar hotéis, onde usuários podem se cadastrar como hóspedes ou hoteleiros. Hoteleiros podem criar seus hotéis com seus respectivos quartos personalizado e visualizar reserva feitas e quartos ocupados em seu hotel. Hóspedes procurarar por quarto ou por hotel, podem fazer reservas para algum quarto do hotel, editar sua reserva.
Deploy da API:

🔨 Funcionalidades:
- 1: Cadastro de usuários como hóspedes ou hoteleiros.
- 2: Hoteleiros podem criar e gerenciar seus hotéis e quartos.
- 3: Hóspedes podem fazer reservas para quartos de hotéis.
- 4: Confirmação e finalização de reservar com agendamentos
- 5: Notificação por email de usuário para cada reserva 


### 🛠️ DOCS SWAGGER :
![DER](/api/utils/deploy/print-docs.png)


### 🛠️ Schema/DER:
![DER](/api/utils/deploy/DER-ENTIDADES.png)

💬 
    Algumas tabelas que não está aqui, eu reaproveite do próprio django. A tabela UserAuth é um model reescrito do User padrão do django com algumas modificações, emas ela continua sendo a responsável por autenticação e autorização. 


## 📈 Rascunho do diagrama 
![DIAGRAMA](/api/utils/deploy/schema.png)


    Fiz esses rascunhos no início projeto como rascunho de ideias, o fluxo para cada usuário segue esse diagrama com seus respectivos fluxos e dados, com pequenas alterações.



 
    E esse sistema de cache, em todos os endpoints de list, esse cache serve a mesma lógica.
    
![DIAGRAMA](/api/utils/deploy/cachec.png)    

    

- 1: Todo o processo de criação e login é feito com AuthUser, em seguida é criado seus respectivos usuários específicos (guest ou hotelier).

- 2: A permissão para fazer um CRUD em cada instancia é baseada em cada uma dessas  tabelas de usuário específicos.

- 3: O celery é usado tanto como servidor de background para tasks asincronas  que são mais demoradas e possíveis de se fazer em outro detereminado tempo, além também de ser usado para agendamento de tarefas, como: para finalizar o booking e atualizar o room (nesse caso agendada de acordo end_date do booking), com o celery-beat-schedule.

- 4: O Redis utilizei tanto pra broker e banco pro celery e também para cache em alguns endpoints  

- 5 Cada usuário tem seu endpoint de perfil com seus dados importantes: 
    - Hotelier com os dados pessoais e do hotel, como por exemplo rooms, bookings em andamento etc.

    - Hóspedes dados booking e do quarto que está hospedado, além do histórico e dados pessoais.


# Deploy da API no GCP:   https://hotel-api-ugz3zongra-rj.a.run.app/


## Docs swagger: https://hotel-api-ugz3zongra-rj.a.run.app/api/schema/swagger-ui


## Video com um pouco do funcionamento da API : https://www.youtube.com/watch?v=biL52SBehxw


    

✔️ Tecnologias utilizadas

    Django REST Framework
    PostgreSQL
    Celery
    Redis
    Docker
    

<img loading="lazy" src="https://avatars.githubusercontent.com/u/88624922?v=4" width=115><br><sub>João Pedro</sub>
