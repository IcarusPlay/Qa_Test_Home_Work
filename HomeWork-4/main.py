import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


# Задание 1: Проверка изменения текста кнопки
def test_button_text_changes(driver):
    driver.get("http://uitestingplayground.com/textinput")

    # Вводим текст в поле
    input_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("ITCH")

    # Нажимаем синюю кнопку
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    # Проверяем что текст кнопки изменился на "ITCH"
    updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH")
    )
    assert updated_button, "Текст кнопки не изменился на 'ITCH'"


# Задание 2: Проверка загрузки изображений
def test_third_image_alt(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждём пока все 4 изображения загрузятся (у последнего появится атрибут src)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//img[@src and @alt='award']"))
    )

    # Берём третье изображение (индекс 2)
    images = driver.find_elements(By.XPATH, "//div[@id='image-container']//img")
    third_image_alt = images[2].get_attribute("alt")

    assert third_image_alt == "award", f"Ожидали 'award', получили '{third_image_alt}'"
