import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.set_preference("javascript.enabled", False)
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def driver_js():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

# Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)

def test_drag_and_drop(driver_js):
    driver_js.get("https://www.globalsqa.com/demoSite/practice/droppable/photo-manager.html")

    first_photo = WebDriverWait(driver_js, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//ul[@id='gallery']//li)[1]"))
    )

    trash = WebDriverWait(driver_js, 10).until(
        EC.presence_of_element_located((By.ID, "trash"))
    )

    ActionChains(driver_js).drag_and_drop(first_photo, trash).perform()

    photos_in_trash = WebDriverWait(driver_js, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@id='trash']//ul//li"))
    )
    assert len(photos_in_trash) == 1, f"В корзине должна быть 1 фотография, а не {len(photos_in_trash)}"

    photos_in_gallery = driver_js.find_elements(By.XPATH, "//ul[@id='gallery']/li")
    assert len(photos_in_gallery) == 3, f"В галерее должно остаться 3 фотографии, а не {len(photos_in_gallery)}"
