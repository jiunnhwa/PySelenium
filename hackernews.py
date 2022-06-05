from time import sleep
from xml.etree import ElementTree
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'C:\LIBS\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

def Run(url):
    driver.get(url)
    print(driver.title.encode('utf-8'))

    elems = driver.find_elements(by=By.XPATH, value="//a[@href]")
    for elem in elems:
        # print(f'{elem.text}: {elem.get_attribute("href")}\n')
        href = elem.get_attribute("href")
        lines = elem.text.splitlines()
        # What might degrowth computing look like?
        # criticaledtech.com
        # cardamomo
        # 20 minutes ago
        # hide
        # past
        # discuss

        if len(lines) != 0:
            if( "ycombinator" not in href ) :
                if ( "past" not in lines[0] ):
                    if ( "API" not in lines[0] ):
                        print(lines[0] , href) # external links only


# Newest
url = "https://news.ycombinator.com/newest"
Run(url)

driver.quit()