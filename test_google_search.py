from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
import allure


@allure.title('Результатов поиска больше 5')
@allure.severity('Severity.BLOCKER')
def test_google_search():
    driver = WebDriver(executable_path='D://selenium//chromedriver.exe')
    with allure.step('Ожидаем страницу поиска'):
        driver.get('https://google.com.ua')

    with allure.step('Ищем https://www.python.org/'):
        search_input = driver.find_element_by_xpath('//input [@name="q"]')
        search_button = driver.find_element_by_xpath('//input [@name="btnK"]')
        search_input.send_keys('https://www.python.org/')
        driver.implicitly_wait(30)
        search_button.click()

