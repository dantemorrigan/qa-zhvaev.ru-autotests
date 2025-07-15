
# 🧪 Автотесты для сайта zhvaev.ru

## Описание

Этот проект — набор простых автотестов для одностраничного сайта-портфолио [zhvaev.ru](https://zhvaev.ru), написанных на Python с использованием pytest, requests и BeautifulSoup4.

**Цель** — продемонстрировать базовые навыки автоматизированного тестирования frontend'а через HTTP-уровень без использования Selenium.

## 📂 Структура проекта

* requirements.txt
* README.md
* tests/
  * test\_main\_page.py

## ✅ Что проверяют тесты?

* Статус-код главной страницы (`200 OK`)
* Заголовок страницы содержит имя "Никита Жваев"
* Ожидаемый текст (приветствие) присутствует на странице
* Все изображения доступны и корректно загружаются

## 🚀 Как запустить?

1. Клонируйте репозиторий

```bash
git clone https://github.com/<твой-юзернейм>/qa-zhvaev-portfolio.git
cd qa-zhvaev-portfolio
```

2. Активируйте виртуальное окружение (по желанию)

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости

```bash
pip install -r requirements.txt
```

4. Запустите тесты

```bash
pytest tests/
```

## 🛠 Стек технологий

* Python 3.13+
* Pytest
* Requests
* BeautifulSoup4

## 📌 Автор

Никита Жваев
[zhvaev.ru](https://zhvaev.ru)

