<h1 align="center">🤖 Kahoot Bot</h1>

<p align="center">
  <b>Массовое подключение ботов к <a href="https://kahoot.it/" target="_blank">Kahoot</a></b><br>
  <i>Автоматизация атаки по типу «бот-рейд» на викторины</i>
</p>

<p align="center">
  <a href ="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.12%2B-blue.svg" /></a>
  <a href ="https://github.com/poiko34/kahoot-bot/blob/main/LICENSE"><img src="https://img.shields.io/github/license/poiko34/kahoot-bot" /></a>
</p>

<hr>

<h2>📦 Возможности</h2>

<ul>
  <li>Подключение к игре по ID</li>
  <li>До нескольких сотен ботов</li>
  <li>Установка зависимостей автоматически</li>
  <li>Консольный интерфейс с аргументами запуска</li>
</ul>

<h2>🚀 Установка и запуск</h2>

<h4>1. Клонируй репозиторий</h4>

```bash
git clone https://github.com/poiko34/kahoot-bot.git
cd kahoot-bot
```

<h4>2. Запуск скрипта</h4>

```bash
python3 kahoot.py -i <game_id> -n <nickname> -m <amount>
```

<h4>💡 Пример:</h4>

```bash
python3 kahoot.py -i 123456 -n bot -m 50
```

Будут созданы никами:
<code>bot_1, bot_2, ..., bot_50</code>

<h2>📚 Зависимости</h2>

Все зависимости будут установлены автоматически при первом запуске.

<h2>🛠 Структура</h2>

```
├── kahoot.py         # Основной исполняемый файл
└── README.md         # Документация
```

<h2>📜 Лицензия</h2>

Проект распространяется под лицензией MIT. Свободно используй, модифицируй и улучшай.
