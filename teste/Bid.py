from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
from functions import Accept_cookie,TimeLeft,GettingValue,InsertingValue,Confirm,Button
from time import sleep



class Bid:
    
    def __init__(self,site):
        self.site = site
        self.chrome_options = Options()
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def Launch(self):
        self.driver.get(self.site)

    def Screenshot(self):
        self.driver.save_screenshot("Finish.jpg")


    def Biding(self):
        Accept_cookie(self.driver)
        while True:
            self.time = TimeLeft(self.driver)
            if self.time == "0":
                sleep(0.75)
                InsertingValue(self.driver,float(GettingValue(self.driver)) + float(5))
                Confirm(self.driver)
                sleep(2)
                return False
            

try:
    Run = Bid("https://developer.automationanywhere.com/challenges/automationanywherelabs-auctionsniper.html?_ga=2.47274208.691472818.1692660483-1844817410.1692326924&_gl=1*1inzipm*_ga*MTg0NDgxNzQxMC4xNjkyMzI2OTI0*_ga_DG1BTLENXK*MTY5MjY2MDQ4My4yLjAuMTY5MjY2MDQ4OS41NC4wLjA.#")
    Run.Launch()
    Run.Biding()
    Run.Screenshot()

except:
    Run.Screenshot()



