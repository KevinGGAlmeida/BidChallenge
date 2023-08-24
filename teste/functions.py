from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def Accept_cookie(driver):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
        driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

    except Exception as error:
        raise Exception(f"Ocorreu o ERRO: {error}")
    

def TimeLeft(driver):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"time-left")))
        return driver.find_element(By.ID,"time-left").text.replace(" seconds","")

    except Exception as error:
        raise Exception(f"Ocorreu o ERRO: {error}")
    

def GettingValue(driver):
    
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"auction-price")))
        return driver.find_element(By.ID,"auction-price").text

    except Exception as error:
        raise Exception(f"Ocorreu o ERRO: {error}")
      


def InsertingValue(driver,value):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"ending-soonest-bid")))
        driver.find_element(By.ID,"ending-soonest-bid").send_keys(value)

    except Exception as error:
        raise Exception(f"Ocorreu o ERRO: {error}")


def Button(driver):
    try:
        WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"auctionQuickBid")))
        driver.find_element(By.ID,"auctionQuickBid").click()

    except Exception as error:
        raise Exception(f"Ocorreu o ERRO: {error}")     


def Confirm(driver):
    try:
        driver.execute_script('document.querySelector(`[onclick="bidPlaced()"]`).click()')
        
    except Exception as error:
        raise Exception(f"Ocorreu o ERRO: {error}")     