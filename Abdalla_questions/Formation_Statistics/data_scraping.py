from selenium import webdriver
import time 

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd 
import numpy as np 

season_link = "https://fbref.com/en/comps/9/2021-2022/2021-2022-Premier-League-Stats"
browser= webdriver.Chrome(ChromeDriverManager().install())


browser.set_page_load_timeout(15)


try :
    browser.get(season_link)
    # just to catch the timeout error 
except:
    pass

browser.set_page_load_timeout(15)



teams=[]
teams_links=browser.find_elements(By.CSS_SELECTOR,"#results2021-202291_overall>tbody>tr> .left>a")
index =0

teams_names = []
teams_href = []
for i in teams_links:
    teams_names.append(i.text)
    teams_href.append(i.get_attribute("href"))

print(teams_names)
for i ,j in zip (teams_href,teams_names) : 
    browser.get(i)
    try : 
        browser.find_element(By.XPATH , "/html/body/div[2]/div[6]/div[7]/div[1]/div/ul/li[3]/span").click()
    except:
        pass 

    browser.implicitly_wait(5)

    browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[7]/div[1]/div/ul/li[1]/span").click()
    print("yes")


    browser.implicitly_wait(1)
    browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[7]/div[1]/div/ul/li[1]/div/ul/li[3]/button").click()
    print("Yes")
    browser.implicitly_wait(1)

    content = browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[7]/div[2]/div/pre").text

    with open(f"{j}2.csv","w") as file : 
        file.write(content)



