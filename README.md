# Todo bot

<p align="left">

[![Python Versions](https://img.shields.io/badge/python_versions-3.10+-blue.svg)](https://shields.io/)
[![License](https://img.shields.io/github/license/vmelfx/assistance_bot)](https://github.com/vmelfx/assistance_bot)
</p>

<p align="left">
✔️ This bot is developed only for Telegram users
</p>
<p align="left">
✔️ Database is shared for all users
</p>
<p align="left">
✔️ Periodic tasks with Celery
</p>

<br>

*Disclaimer: this project is created for personal usage. Do a fork for playing with the code*

<br>

# 🔨 Setup the project localy

> 💡 It includes 2 possible guides: for setting up it with docker  🐳 or without it.

## 🚧 Mandatory steps

Clone the project from Github

```bash
git@github.com:vmelfx/assistance_bot.git
```
<br>

## ✖️ 🐳 Without docker

### 🔧 Setup the environment

For running application locally without a tool like Docker you would need to install all dependencies by yourself.

First of all you have to install Python 3.10 and SQLite 3 on your machine since they are main infrastructure components.

More information about the installation process you can find [HERE](https://github.com/vmelfx/assistance_bot/wiki/Application-is-powerd-by)

Then you have to install Python dependencies that are used for runnig the application. For doing this I recommend using ```pipenv``` as a tool for managing your virtual environment and project dependencies (*but if you prefer using conda for example feel free to do this*).

```bash
# install pipenv
pip install pipenv

# activate the virtual environment
pipenv shell

# install dependencies from the Pipfile.lock file
pipenv sync --dev
```
### 💾 Setup the database

For working with database the alembic tool is used. To initiate a new database, run:

```bash
alembic upgrade head
```
**More alembic commands**

Generate a new migration file based on SQLAlchemy models

```bash
alembic revision --autogenerate -m "MESSAGE"
```
Upgrade database according to the last version of migrations

```bash
alembic uprade head
```
Downgrade to the specific migration version

```bash
alembic downgrade 0e43c346b90d
```
*P.S. This hash is taken from the generated file in the migrations folder*

⚠️ Do not forget that alembic saves the migration version into the database. Then, when you do crucial database updates you might need to remove the revision ID from the database.

```bash
sqlite3 db.sqlite3
> delete from alembic_version;
```

### 🏃‍♂️ Run the application

```bash
python -m src.run
```
<br>

## 🐳 Using Docker

Since developers may use different operating system the Docker system is used in order to resolve the issue: "not working on my computer"

If more specifically, the Docker compose is used for better experience.

### 🛠️ Setting up the project

For setting up the project you just need to complete only a few steps:

- Install the Docker [[download page](https://docs.docker.com/get-docker/)]
- Rung Docker containers using docker-compose:

### 🏃 Running docker containers

> ⚠️ This command should be ran in the project root folder (assistance_bot/)

```bash
docker-compose up -d
```
The `-d` means `--detach` that allows you to run the container in a background

**More Docker commands**

```bash
# Shut down docker containers
docker-compose down

# Show logs
docker-compose logs

# Show logs in a real time
docker-compose logs -f
```
<br>

## 🔧 Configure the project

The project could be configurable by using the environment variables which are retrived in `src/settings.py` file

The examle of setting up the environment variable:

```bash
# on Unix
export TELEGRAM_BOT_API_KEY=1223713432:AASDEH5ocYq2jqeqpxqasn123e0B5YrUWubKo

# on Windows
$env:TELEGRAM_BOT_API_KEY = "1223713432:AASDEH5ocYq2jqeqpxqasn123e0B5YrUWubKo";
```

Or as a preffered alternative you may use the `.env` that is automatically complete the stuff above for you if you use `pipenv` tool.

It means that you just need to complete next steps:

```bash
# create the .env file base on the .env.default file
cp .env.default .env

# activate the virtual environment & export all environment variables automatically ༼ つ ◕_◕ ༽つ━☆ﾟ.*･｡ﾟ
pipenv shell
```
<br>

## 🤔 Summary

- So now, the project is ready to be used as a Telegram bot backend.

Just go to the Telegram bot that you had created with BotFather and start working.