import datetime
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
options.binary_location = r'D:\TOOLS\FirefoxPortable\App\firefox64\firefox.exe'

DRIVER_PATH = r'C:\LIBS\geckodriver-v0.31.0-win64\geckodriver.exe'
driver = webdriver.Firefox(executable_path=DRIVER_PATH, options=options)

def Run(url):
    driver.get(url)
    sleep(5) # delay
    print("title:", driver.title.encode('utf-8'))

    #elems = driver.find_elements(by=By.XPATH, value="//div/h3/a[contains(@href,'job')]")
    elems = driver.find_elements(by=By.XPATH, value="//a[contains(@data-automation-id,'jobTitle')]" )
    print("Len: ", len(elems))
    for elem in elems:
        print(f'{elem.text}: {elem.get_attribute("href")}\n')




# Jobs
url = "https://thales.wd3.myworkdayjobs.com/en-US/Careers/jobs?utm_medium=referral&utm_source=thalesgroup&utm_campaign=pagecandidats&utm_content=link_UK&locationCountry=80938777cac5440fab50d729f9634969"
Run(url)


driver.quit()