from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

REVIEWS_CONTAINER = (
    ".di536pa.atm_ks_zryt35.atm_mk_h2mmj6.atm_26_1hbpp16"
    ".atm_vy_auwlz6.atm_j3_auwlz6.atm_iy_1osqo2v.atm_9s_1txwivl"
    ".atm_ar_1bp4okc.atm_70_1i7rd3n.atm_6a_1hl1osj.atm_6c_1hl1osj"
    ".atm_y_1bbsqr7.atm_16_kb7nvz.atm_12_1hrf63d.atm_1c_m2duij"
    ".atm_ks_15vqwwr__1yj3dog.atm_kd_glywfm_pfnrn2.atm_vy_1osqo2v__oggzyc"
    ".atm_5j_1hl1osj__oggzyc.atm_1c_w5iguh__p88qr9.atm_j3_6tyhld__oggzyc.dclclpo"
)

REVIEW_ITEM = ".ll4r2nl.atm_kd_pg2kvz_1bqn0at"


def strip_reviews_link(link: str) -> str:
    url = urlparse(link)
    if "airbnb" not in url.netloc or "/rooms/" not in url.path:
        return None

    return f"{url.scheme}://{url.netloc}{url.path}/reviews"


def get_reviews(review_link: str):
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    service = webdriver.firefox.service.Service(executable_path=GECKODRIVER_PATH)
    driver = webdriver.Firefox(options=options, service=service)
    container = None

    try:
        driver.get(review_link)
        container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, REVIEWS_CONTAINER))
        )
        time.sleep(3)
        container = container.get_attribute("innerHTML")
        soup = BeautifulSoup(container, "html.parser")
        review_elements = soup.select(REVIEW_ITEM)[:16]
        reviews = [review.text for review in review_elements]

        return reviews

    finally:
        driver.quit()
