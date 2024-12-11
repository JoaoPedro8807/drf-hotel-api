FROM python:3.11.3-alpine3.18
LABEL maintainer="joaogood@outlook.com"

# Define variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install redis
RUN apk update && apk add redis

# Copia os diretórios
COPY api /api
COPY scripts /scripts

# Define o diretório de trabalho 
WORKDIR /api

# Expõe a porta 8000 e 6379 (porta padrão do Redis)
EXPOSE 8000 6379

# Instala dependências e configura o ambiente
RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /api/requirements.txt && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R root:root /venv && \
  chown -R root:root /data/web/static && \
  chown -R root:root /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts

# Atualiza o PATH
ENV PATH="/scripts:/venv/bin:$PATH"

ENTRYPOINT ["sh", "-c", "python manage.py makemigrations --noinput && python manage.py migrate --noinput && python manage.py runserver 0.0.0.0:8000"]

# Define o comando padrão
#CMD ["commands.sh"]
