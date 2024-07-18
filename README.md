 # Administração de Hotel com Django REST Framework
<p align="center">
<img src="http://img.shields.io/static/v1?label=STATUS&message=Em%20Desenvolvimento&color=YELLOW&style=for-the-badge">
</p>

Uma API para administrar hotéis, onde usuários podem se cadastrar como hóspedes ou hoteleiros. Hoteleiros podem criar seus hotéis, quartos e editar suas reservas. Hóspedes podem fazer reservas para algum quarto do hotel.
Deploy da API: [link para o deploy se houver]

🔨 Funcionalidades:
- 1: Cadastro de usuários como hóspedes ou hoteleiros.
- 2: Hoteleiros podem criar e gerenciar seus hotéis e quartos.
- 3: Hóspedes podem fazer reservas para quartos de hotéis.
- 4: Confirmação e finalização de reservar com agendamentos
- 5: Notificação por email de usuário para cada reserva 



### 🛠️ Schema/DER:
![DER](/api/utils/deploy/DER-ENTIDADES.png)

💬 
    Algumas tabelas que não está aqui, eu reaproveite do próprio django. A tabela UserAuth é um model reescrito do User padrão do django com algumas modificações, emas ela continua sendo a responsável por autenticação e autorização. 


## 📈 Rascunho do diagrama 
![DIAGRAMA](/api/utils/deploy/schema.png)
![DIAGRAMA](/api/utils/deploy/cachec.png)

    Fiz esses rascunhos no início projeto como rascunho de ideias, o fluxo para cada usuário segue esse diagrama com seus respectivos fluxos e dados, com pequenas alterações.

    



    

- 1: Todo o processo de criação e login é feito com AuthUser, em seguida é criado seus respectivos usuários específicos (guest ou hotelier).

- 2: A permissão para fazer um CRUD em cada instancia é baseada em cada uma dessas  tabelas de usuário específicos.

- 3: O celery é usado tanto como servidor de background para tasks asincronas  que são mais demoradas e possíveis de se fazer em outro detereminado tempo, além também de ser usado para agendamento de tarefas, como: para finalizar o booking e atualizar o room (nesse caso agendada de acordo end_date do booking), com o celery-beat-schedule.

- 4: O Redis utilizei tanto pra broker e banco pro celery e também para cache em alguns endpoints  

- 5 Cada usuário tem seu endpoint de perfil com seus dados importantes: 
    - Hotelier com os dados pessoais e do hotel, como por exemplo rooms, bookings em andamento etc.

    - Hóspedes dados booking e do quarto que está hospedado, além do histórico e dados pessoais.



    

✔️ Tecnologias utilizadas

    Django REST Framework
    PostgreSQL
    Celery
    Redis
    Docker
    

<img loading="lazy" src="https://avatars.githubusercontent.com/u/88624922?v=4" width=115><br><sub>João Pedro</sub>