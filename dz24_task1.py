from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument()

driver = webdriver.Chrome()
driver_path = 'путь/к/вашему/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://kurs.kz/')


time.sleep(2)


usd_cours = driver.find_element('//div[@class="block-currency__table"]//td[contains(text(), "USD")]/following-sibling::td[1]')


usd_cours_text = usd_cours.text


print(f'Курс доллара США: {usd_cours_text}')

