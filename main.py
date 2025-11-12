from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
options = [
    "--headless"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(options=chrome_options)

driver.get('http://github.com')
print(driver.title)

driver.quit()
