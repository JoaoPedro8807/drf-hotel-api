#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

# Função para verificar se o PostgreSQL está pronto
wait_for_postgres() {
  while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
    echo "🟡 Waiting for Postgres Database Startup ($POSTGRES_HOST:$POSTGRES_PORT) ..."
    sleep 2
  done
  echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"
}

# Espera pelo PostgreSQL
wait_for_postgres


# Executa as migrações e coleta os arquivos estáticos
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Inicia o servidor Django


#iniciando o celery

python manage.py runserver 0.0.0.0:8000 

#comands do celery : 
celery -A project worker --pool=solo -l info (iniciar antes e separado)
celery -A project beat -l INFO
