![.github/workflows/foodgram_workflow.yml](https://github.com/luydmila-davletova/foodgram-project-react/actions/workflows/foodgram_workflow.yaml/badge.svg)
# «FOODGRAM».
 ### Описание
Foodgram- это веб-приложение, где вы можете делиться своими рецептами и просматривать рецепты других пользователей,
а так же добавлять их в избранное и корзину покупок.

[Ссылка на развернутый проект](http://158.160.14.79/signin)

Суперюзер:

- login: user@ya.ru
- password: user
 ### Технологии
 Python 3.8, DRF 3.12, JWT + Djoser
### Запуск проекта 
 - Склонируйте репозиторий.
 ```bash
 git clone https://github.com/luydmila-davletova/foodgram-project-react
 ```
 - Установите и активируйте виртуальное окружение:
 ```bash
 py -3.8 -m venv venv
 venv/Scripts/activate
 python -m pip install --upgrade pip
 ```
 - Установите зависимости из файла requirements.txt
 ```bash
 pip install -r requirements.txt
 ```
- Создайте .env файл со следующим содержанием:
 ```bash
SECRET_KEY = 'твой ключ'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=нужно_придумать_пароль
DB_HOST=db
DB_PORT=5432
 ```
- Установите докер:
- [Инструкция для Линукс (для других ОС инструкция в документации)](https://docs.docker.com/desktop/install/mac-install/):
 ```bash

sudo apt update && sudo apt upgrade -y && sudo apt install curl -y
sudo curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh && sudo rm get-docker.sh
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo systemctl start docker.service && sudo systemctl enable docker.service
 ```
Из папок frontend и backend нужно собрать образы и запушить на DockerHub:
```bash
docker login
 ```
```bash
cd backend
 ```
```bash
docker build -t davletova1/foodgram_backend:latest .
 ```
```bash
docker push davletova1/foodgram_backend:latest
 ```
Сборка закончена, можно взлетать!
```bash
docker-compose up -d --build
 ```
Далее нужно выполнить миграции, собрать статику и создать суперюзера:
```bash
docker-compose exec backend python manage.py makemigrations
 ```
```bash
docker-compose exec backend python manage.py migrate --noinput
 ```
```bash
docker-compose exec backend python manage.py createsuperuser
 ```
```bash
docker-compose exec backend python manage.py collectstatic --no-input
 ```
Наполнить БД :
```bash
docker-compose exec backend python manage.py import_inr
docker-compose exec backend python manage.py import_tags
 ```
Проект запущен и готов к работе!

### Документация доступна после запуска проекта по адресу:
http://127.0.0.1/api/docs/

Разработка backend : [Давлетова Людмила](https://github.com/luydmila-davletova)

