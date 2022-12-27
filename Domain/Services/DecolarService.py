import uuid
from Domain.Model.Config import Config
from Domain.Services.PageService import GetPages
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from Domain.Services.WebdriveService import OpenWebDrive


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

class SingleProcess:
    def __init__(self, config) -> None:
        self.config = config
        self.temp_folder = str(uuid.uuid4())

    def Start(self):
        (
            airportFrom,
            airporTo,
            dateGo,
            dateBack,
            travelers
        ) = self.config.split(",")
        _guid = uuid.uuid4()
        url = ''
        url += DecolarConfig.Url + DecolarConfig.Route
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
        self.url = url + DecolarConfig.Route2
        driver = OpenWebDrive(self.url)
        self.cookies = {x["name"]: x["value"] for x in driver.get_cookies()}        
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")    

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

        ### Find price
        objectTarget = driver.find_element(By.ID,'toolbox-tabs-position')
        objectTarget = objectTarget.find_element(By.XPATH,'//*[@id="flights-container"]/div/div[3]/div/div[2]/div/div[4]/app-root/app-common/new-sorting-tabs/div')
        objectTarget = objectTarget.find_element(By.XPATH, '//*[@id="flights-container"]/div/div[3]/div/div[2]/div/div[4]/app-root/app-common/new-sorting-tabs/div/tab-component[2]')
        objectTarget.click()

        objectPrive = objectTarget.find_element(By.XPATH,'//*[@id="clusters"]/span[1]/div/span/cluster/div/div/div[2]/fare/span/span/fare-details-items')

        objectPrive = objectPrive.find_element(By.XPATH,'//*[@id="clusters"]/span[1]/div/span/cluster/div/div/div[2]/fare/span/span/fare-details-items/div/item-fare/p/span/flights-price/span/flights-price-element/span/span/em/span[2]')

        print(objectPrive)

        # listar todos os preços e salvar para primeira fase

        return 1




