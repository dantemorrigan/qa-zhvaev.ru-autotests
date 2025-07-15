import requests
from bs4 import BeautifulSoup

def test_main_page_status():
    response = requests.get("https://zhvaev.ru")
    assert response.status_code == 200

def test_title_contains_name():
    response = requests.get("https://zhvaev.ru")
    soup = BeautifulSoup(response.text, "html.parser")
    assert "Никита Жваев" in soup.title.string

def test_page_contains_expected_text():
    response = requests.get("https://zhvaev.ru")
    assert "👋 Никита Жваев" in response.text

def test_images_are_accessible():
    response = requests.get("https://zhvaev.ru")
    soup = BeautifulSoup(response.text, "html.parser")
    images = soup.find_all("img")

    for img in images:
        src = img.get("src")
        if not src:
            continue

        # убираем ./ если есть
        if src.startswith("./"):
            src = src.replace("./", "/")

        # если путь относительный — добавляем домен
        if not src.startswith("http"):
            src = "https://zhvaev.ru" + src

        img_response = requests.get(src)
        assert img_response.status_code == 200, f"Image {src} is not accessible"
