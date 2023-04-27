from selenium import webdriver
import time 

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd 
import numpy as np 



def web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--verbose")
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument("--window-size=1920, 1200")
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    return drive

season_link = "https://fbref.com/en/comps/12/2019-2020/schedule/2019-2020-La-Liga-Scores-and-Fixtures"
browser= web_driver()


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

    try : 
        away=browser.find_element(By.XPATH,'/html/body/div[2]/div[5]/div[2]/div[2]/div[1]/strong/a').text
        data_frame["away"].append(away)
        
    except:
        data_frame["away"].append(None)

    try:
        possessionhome=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[1]/table/tbody/tr[3]/td[1]/div/div[1]").text
        
        data_frame["possessionhome"].append(possessionhome)
       
    except:
        data_frame["possessionhome"].append(None)
    try:
        possessionaway=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[1]/table/tbody/tr[3]/td[2]/div/div[1]").text
        
        data_frame['possessionaway'].append(possessionaway)
        
    except:
        data_frame["possessionaway"].append(None)

    try :
        passeshome=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[1]/table/tbody/tr[5]/td[1]/div/div[1]").text
        
        data_frame["passeshome"].append(passeshome)

    except:
        data_frame["passeshome"].append(None)

    try:
        passesaway=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[1]/table/tbody/tr[5]/td[2]/div/div[1]").text
        
        data_frame["passesaway"].append(passesaway)
    except:
        data_frame["passesaway"].append(None)
    
    try:
        saveshome=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[1]/table/tbody/tr[9]/td[1]/div/div[1]").text
        data_frame["saveshome"].append(saveshome)
        
    except:
        data_frame["saveshome"].append(None)


    try:
        savesaway=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[1]/table/tbody/tr[9]/td[2]/div/div[1]").text
        data_frame["savesaway"].append(saveshome)
        
    except:
        data_frame["savesaway"].append(None)

    try : 
        crosseshome = browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[1]/div[10]").text
        
        data_frame["crosseshome"].append(crosseshome)

    except:
        data_frame["crosseshome"].append(None)

    try : 
        crossesaway= browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[1]/div[12]").text
        
        data_frame["crossesaway"].append(crossesaway)

    except:
        data_frame["crossesaway"].append(None)
    
    try : 
        toucheshome=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[1]/div[13]").text
        
        data_frame["toucheshome"].append(toucheshome)

    except:
        data_frame["toucheshome"].append(None)
    
    try:
        touchesaway=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[1]/div[15]").text
        
        data_frame["touchesaway"].append(touchesaway)
    
    except:
        data_frame["touchesaway"].append(touchesaway)

    try:
        tackleshome = browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[4]").text
        
        data_frame["tackleshome"].append(tackleshome)
    except:
        data_frame["tackleshome"].append(None)

    try : 
        tacklesaway= browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[6]").text
        
        data_frame["tacklesaway"].append(tacklesaway)
    except:
        data_frame["tacklesaway"].append(None)
    

    try:
        interceptionhome=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[7]").text
        
        data_frame["interceptionhome"].append(interceptionhome)

    except:
        data_frame["interceptionhome"].append(None) 

    try:
        interceptionaway=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[9]").text
        
        data_frame["interceptionaway"].append(interceptionaway) 
    except:
        data_frame['interceptionaway'].append(None)     

    try:
        aerialshome=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[10]").text
        
        data_frame["aerialshome"].append(aerialshome)
    except:
        data_frame["aerialshome"].append(None)

    try:
        aerialsaway=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[12]").text
        
        data_frame["aerialsaway"].append(aerialsaway)
    except:
        data_frame["aerialsaway"].append(None)

    try:
        clearnacehome=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[13]").text
        
        data_frame["clearnacehome"].append(clearnacehome)

    except:
        data_frame["clearnacehome"].append(clearnacehome)


    try:
        clearnaceaway=browser.find_element(By.XPATH,"/html/body/div[2]/div[5]/div[7]/div[2]/div[2]/div[15]").text
        
        data_frame["clearnaceaway"].append(clearnaceaway)

    except:
        data_frame["clearnaceaway"].append(None)

    print(index)
    index+=1
df=pd.DataFrame(data_frame)

    
df.to_csv("temp2.csv")