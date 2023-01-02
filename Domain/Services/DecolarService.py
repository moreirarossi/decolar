import uuid
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from Domain.Model.Config import Config
from Domain.Services.PageService import GetPages
from Domain.Services.WebDriverService import WebDriver

def FindClassIn( target: webdriver, classList ):
    try:
        result = target
        for itemClassList in classList:
            result = result.find_element(By.CLASS_NAME,itemClassList)
        return result
    except:
        print("e")

class DecolarConfig(Config):
    Url = 'https://www.decolar.com'
    Route = '/shop/flights/results/roundtrip'
    Route2 = '/0/0/NA/NA/NA/NA/NA?from=SB&di=3-0'
    xPathMaisBarato = '//*[@id="flights-container"]/div/div[3]/div/div[2]/div/div[4]/app-root/app-common/new-sorting-tabs/div/tab-component[2]/div/span[1]'
    xPathRecomendado = '//*[@id="flights-container"]/div/div[3]/div/div[2]/div/div[4]/app-root/app-common/new-sorting-tabs/div/tab-component[1]/div/span[1]/p'
    xPathMaisRapido = '//*[@id="flights-container"]/div/div[3]/div/div[2]/div/div[4]/app-root/app-common/new-sorting-tabs/div/tab-component[3]/div/span[1]'

def wait_element(driver, by: str, value: str, secs: float):
    waitSec = 0
    while waitSec < secs:
        try:
            object = driver.find_element(by,value)
            return object
        except:
            time.sleep(1)
            waitSec += 1
    raise 

class SingleProcess:
    def __init__(self, params) -> None:
        self.params = params
        self.config = DecolarConfig()
        self.temp_folder = str(uuid.uuid4())

    def Start(self):
        (
            airportFrom,
            airporTo,
            dateGo,
            dateBack,
            travelers
        ) = self.params.split(",")
        url = ''
        url += self.config.Url + self.config.Route
        if airportFrom:
            url += f"/{airportFrom}"
        if airporTo:
            url += f"/{airporTo}"
        if dateGo:
            url += f"/{dateGo}"
        if dateBack:
            url += f"/{dateBack}"
        if travelers:
            url += f"/{travelers}"
        self.url = url + self.config.Route2
        driver = WebDriver(self.url).OpenWebDriver()
        self.cookies = {x["name"]: x["value"] for x in driver.get_cookies()}        
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        # mais barato
        objectPriceOptions = wait_element(driver,By.XPATH,self.config.xPathMaisBarato,30)
        if (objectPriceOptions):
            objectPriceOptions.click()

                



        time.sleep(5)
          

        ### Find button +/- 3 days
        # objectTarget = driver.find_element(By.ID,'toolbox-tabs-position')
        # objectTarget = objectTarget.find_element(By.CLASS_NAME,'results-cluster-container -skeleton -show')
        # objectTarget = FindClassIn(objectTarget,['results-cluster-container -skeleton -show'
        #                                         ,'eva-3-tabs'
        #                                         ,'tabs-nav-corners-container'
        #                                         ,'tabs-container'
        #                                         ,'tabs-nav -flex'
        #                                         ,'tabs-nav-item calendarPricesMatrix'
        #                                         ])
        # objectTarget.click()

        # ### Find price
        # objectTarget = driver.find_element(By.ID,'toolbox-tabs-position')
        # #objectTarget = objectTarget.find_element(By.CLASS_NAME,'results-cluster-container -skeleton -show')
        # objectTarget = objectTarget.find_element(By.CLASS_NAME,'tabs-container')
        
        # objectTarget = FindClassIn(objectTarget,['results-cluster-container -skeleton -show'
        #                                         ,'eva-3-tabs'
        #                                         ,'tabs-nav-corners-container'
        #                                         ,'tabs-container'
        #                                         ,'tabs-nav -flex'
        #                                         ,'tabs-nav-item calendarPricesMatrix'
        #                                         ])

        # containerSorting = object2Class.find_elements(By.CLASS_NAME,'container-sorting-tabs -eva-3-mb-lg')
        # for itemContainerSorting in containerSorting:
        #     driver.switch_to.default_content()
        #     driver.switch_to.frame(itemContainerSorting)
        #     driver.implicitly_wait(delayTime)

        # #     listPrices = driver.find_elements(By.CLASS_NAME,"price")
        # #     for itemPrices in listPrices:
        # #         driver.switch_to.default_content()
        # #         driver.switch_to.frame(itemPrices)
        # #         driver.implicitly_wait(delayTime)

        # # listar todos os preços e salvar para primeira fase

        # time.sleep(5)
        return 1




