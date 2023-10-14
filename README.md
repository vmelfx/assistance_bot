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
For running application locally without a tool like Docker you would need to install all dependencies by yourself.

First of all you have to install Python 3.10 and SQLite 3 on your machine since they are main infrastructure components.

More information about the installation process you can find [HERE](https://github.com/vmelfx/assistance_bot/wiki/Application-is-powerd-by)

Then you have to install Python dependencies that are used for runnig the application. For doing this I recommend using ```pipenv``` as a tool for managing your virtual environment and project dependencies (but if you prefer using conda for example feel free to do this).

