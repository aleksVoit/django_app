FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBAFFERED=1

ENV PG_HOST=localhost
ENV PG_USER=user
ENV PG_PASSWORD=changeme
ENV PG_DB=quotes_db
ENV PG_PORT=5432

ENV MG_USER=oleksandrvoitushenko
ENV MG_PASS=FQUdt8a5dbCmlr83
ENV MG_CLUSTER=clusterhw8
ENV MG_DOMAIN=gaxzbkd.mongodb.net
ENV MG_DB=hw8
ENV MG_PORT=27017

ENV SECRET_KEY="django-insecure-&23_hg*zw_#6+39^jp-q*l(%l$uyd#jt5nf-t^+ala5w++2)c*"

# Создайте директорию приложения
WORKDIR /django_app

# Копируйте файл зависимостей
COPY requirements.txt /django_app

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

COPY . /django_app

# Копируйте код приложения

# Команда для запуска вашего приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
