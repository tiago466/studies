
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

navegador = webdriver.Chrome()
navegador.get("https://intranet.zenatur.com.br/Login/Index?ReturnUrl=%2f")
login = navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div[2]/div/form/div[2]/div[1]/div/input')
senha = navegador.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div/div[2]/div/form/div[2]/div[2]/div/input')
btnEntrar = navegador.find_element(By.XPATH, '//*[@id="frmLogin"]/div[2]/div[4]/div/div[2]/button')
login.send_keys("dirsam")
senha.send_keys("139#c3fbb")
btnEntrar.click()
sleep(10)