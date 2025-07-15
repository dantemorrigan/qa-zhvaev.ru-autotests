
# 🧪 Автотесты для сайта-визитки zhvaev.ru

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

## Postman тесты

Ниже — результаты запуска базовых тестов в Postman:
<img width="1058" height="789" alt="1" src="https://github.com/user-attachments/assets/7ef9ee65-4ee0-433b-a0c7-e9137f13642f" />
<img width="1058" height="789" alt="2" src="https://github.com/user-attachments/assets/1a7e0e25-3c73-45e0-965b-70c70b2e622e" />
<img width="1059" height="789" alt="3" src="https://github.com/user-attachments/assets/af914aa6-3abd-4d12-8f49-7f993c3fe5bd" />
<img width="1009" height="309" alt="4" src="https://github.com/user-attachments/assets/94f0282d-5163-4ea5-97e9-6c1d39f9b20c" />

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

