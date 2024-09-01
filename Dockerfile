FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBAFFERED 1

# Создайте директорию приложения
WORKDIR /django_app

# Копируйте файл зависимостей
COPY . 

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте код приложения
COPY .. .

# Команда для запуска вашего приложения
CMD ["python", "quotes/manage.py", "runserver", "0.0.0.0:8000"]
