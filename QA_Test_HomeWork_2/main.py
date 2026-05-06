import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()


def test_payment_section_screenshot(driver):
    payment_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rec1921734713"))
    )

    driver.execute_script("arguments[0].scrollIntoView();", payment_section)
    sleep(2)  # ждём пока элемент полностью отрисуется

    result = payment_section.screenshot(r"C:\Users\bogda\PythonProject\QA_Test_HomeWork\QA_Test_HomeWork_2\payment_methods.png")
    print(f"Скриншот сохранён: {result}")
