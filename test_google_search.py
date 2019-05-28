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
'''
    def check_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//div [@class = "g"]')
        return len(inner_search_results) > 5

    with allure.step('Ожидаем что колличество результатов теста будет больше 5'):
        WebDriver(driver, 5, 0.5).until(check_results_count)

    with allure.step('Переходим по ссылке первого результата'):
        search_results = driver.find_element_by_xpath('//div [@class = "g"]')
        link = search_results[0].find_element_by_xpath('//a/h3')
        link.click()

    driver.switch_to.window(driver.window_handles[1])
    with allure.step('Проверим корректность Title страницы'):
        assert driver.title == 'Тут должен быть заголовок который будет присутствовать на открываемой нами страничке, мы проверяем наличие на страничке этого заголовка'
'''