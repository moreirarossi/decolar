import time
import undetected_chromedriver as uc
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

class WebDriver:
    def __init__(self,url) -> None:
        self.url = url
        ua = UserAgent(verify_ssl=False)
        userAgent = ua.random
        self.options = Options()
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument(f'user-agent={userAgent}')
        self.options.add_argument("--disable-extensions"); # disabling extensions
        self.options.add_argument("--disable-gpu"); # applicable to windows os only
        self.options.add_argument("--disable-dev-shm-usage"); # overcome limited resource problems
        self.options.add_argument("--no-sandbox"); # Bypass OS security model
        self.options.add_argument('--window-size=1920,1080')
        self.options.add_argument("--disable-blink-features")
        self.options.add_argument('--disable-blink-features=AutomationControlled')  

    def OpenWebDriver(self):
        chromedriver_autoinstaller.install()
        uc.options = self.options  
        driver = uc.Chrome(use_subprocess=True)
        # wait = WebDriverWait(driver,20)
        driver.get(self.url)

        return driver
