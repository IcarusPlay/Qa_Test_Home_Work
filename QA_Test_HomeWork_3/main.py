import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    yield driver
    driver.quit()


def test_logo_is_displayed(driver):
    logo = driver.find_element(By.XPATH, "//*[@id='rec785980025']//img")
    assert logo.is_displayed(), "Логотип ITCareerHub не отображается"


def test_nav_links_are_displayed(driver):
    links = ["Программы", "Способы оплаты", "О нас", "Контакты", "Отзывы", "Блог"]
    for link_text in links:
        element = driver.find_element(By.XPATH, f"//*[text()='{link_text}']")
        assert element.is_displayed(), f"Ссылка '{link_text}' не отображается"


def test_language_buttons_are_displayed(driver):
    ru_btn = driver.find_element(By.XPATH, "//*[text()='ru']")
    de_btn = driver.find_element(By.XPATH, "//*[text()='de']")
    assert ru_btn.is_displayed(), "Кнопка языка 'ru' не отображается"
    assert de_btn.is_displayed(), "Кнопка языка 'de' не отображается"


def test_callback_popup(driver):
    # Кликаем по разделу "Контакты"
    contacts = driver.find_element(By.XPATH, "//*[text()='Контакты']")
    contacts.click()
    sleep(2)

    # Кликаем по кнопке "Обратный звонок"
    callback_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[text()='Обратный звонок']"))
    )
    callback_btn.click()

    # Проверяем текст во всплывающем окне
    popup_text = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Запишитесь на бесплатную карьерную консультацию')]"))
    )
    assert popup_text.is_displayed(), "Текст в всплывающем окне не отображается"