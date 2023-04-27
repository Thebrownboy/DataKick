from selenium import webdriver
import time 

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd 
import numpy as np 

season_link = "https://fbref.com/en/comps/9/2017-2018/schedule/2017-2018-Premier-League-Scores-and-Fixtures"
browser= webdriver.Chrome(ChromeDriverManager().install())


browser.set_page_load_timeout(15)


try :
    browser.get(season_link)
    # just to catch the timeout error 
except:
    pass

browser.set_page_load_timeout(10)

match_reports_links=browser.find_elements(By.CSS_SELECTOR,"td[data-stat='match_report']>a")

match_reports_links_lst=[]

for i in range(len(match_reports_links)):
    match_reports_links_lst.append(match_reports_links[i].get_attribute("href"))


data_frame={"date":[],"home":[],"away":[],"possessionhome":[],"possessionaway":[],"passeshome":[],"passesaway":[]
            ,"saveshome":[],"savesaway":[],"crosseshome":[],"crossesaway":[],"toucheshome":[],"touchesaway":[],"tackleshome":[],"tacklesaway":[],"interceptionhome":[],
            "interceptionaway":[],"aerialshome":[],"aerialsaway":[],"clearnacehome":[],"clearnaceaway":[]}
print(len(match_reports_links_lst))
index =1
for match_item_link in match_reports_links_lst:
    try:
        browser.get(match_item_link)
    except:
        pass
    try:
        date = browser.find_element(By.CSS_SELECTOR,".scorebox_meta>div>span").get_attribute("data-venue-date")
        data_frame["date"].append(date)
        
    except:
        data_frame["date"].append(None)
    
    try : 
        home=browser.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[2]/div[1]/div[1]/strong/a').text
        data_frame["home"].append(home)
        

    except:
        data_frame["home"].append(None)