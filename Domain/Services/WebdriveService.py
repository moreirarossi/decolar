import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import undetected_chromedriver as uc
import chromedriver_autoinstaller

ua = UserAgent(verify_ssl=False)
userAgent = ua.random
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument(f'user-agent={userAgent}')
options.add_argument("--disable-extensions"); # disabling extensions
options.add_argument("--disable-gpu"); # applicable to windows os only
options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
options.add_argument("--no-sandbox"); # Bypass OS security model
# options.add_argument('--window-size=1920,1080')
options.add_argument("--disable-blink-features")
options.add_argument('--disable-blink-features=AutomationControlled')    

def OpenWebDrive(url):
    chromedriver_autoinstaller.install()
    uc.options = options  
    driver = uc.Chrome(use_subprocess=True)
    #wait = WebDriverWait(driver,20)
    driver.get(url)
    time.sleep(5)

    return driver