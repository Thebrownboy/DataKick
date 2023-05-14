from selenium import webdriver
import time 

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd 
import numpy as np 
import pickle 

from selenium.webdriver.common.action_chains import ActionChains

seasson_date= "2016-2017"
season_link = f"https://fbref.com/en/comps/9/{seasson_date}/{seasson_date}-Premier-League-Stats"
browser= webdriver.Chrome(ChromeDriverManager().install())


browser.set_page_load_timeout(15)


try :
    browser.get(season_link)
    # just to catch the timeout error 
except:
    pass

browser.set_page_load_timeout(10)



list_ = ["#stats_standard_9 > tfoot > tr:nth-child(1)","#stats_keeper_9 > tfoot > tr:nth-child(1)","#stats_shooting_9 > tfoot > tr:nth-child(1)","#stats_passing_9 > tfoot > tr:nth-child(1)","#stats_passing_types_9 > tfoot > tr:nth-child(1)","#stats_gca_9 > tfoot > tr:nth-child(1)","#stats_defense_9 > tfoot > tr:nth-child(1)"]

dataframe={"stands":[],"keeping":[],"shooting":[],"passing":[],"passing_types":[],"goalCreation":[],"defense":[]}
teams=[]
teams_links=browser.find_elements(By.CSS_SELECTOR,f"#results{seasson_date}91_overall>tbody>tr> .left>a")
index =0

teams_names = []
teams_href = []
for i in teams_links:
    teams_names.append(i.text)
    teams_href.append(i.get_attribute("href"))

with open (f"season-{seasson_date}","wb") as fp :
    pickle.dump(teams_names,fp)
    

# print (len(teams_links),len(teams_names))
# for i,name in   zip(teams_href,teams_names) :
#     teams.append(name)
#     try:
#         browser.get(i)
#     except:
#         pass
    
#     browser.implicitly_wait(1)
#     index=0 

#     list_buttons = browser.find_elements(By.CLASS_NAME,"tooltip")
    
#     try :
#         element = browser.find_element(By.ID,"stats_standard_9")
#         # element.location_once_scrolled_into_view
#         actions = ActionChains(browser)
#         actions.move_to_element(element).perform()
#     except : 
#         pass 
#     browser.implicitly_wait(4)


#     has_conent =False 
#     try:
#         print("Iam here 1 ")
#         browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[3]/div[1]/div/ul/li[1]/span").click()
#         browser.implicitly_wait(4)
#     except: pass 
#     try: 
#         print("Iam here 2 ")

#         browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[3]/div[1]/div/ul/li[1]/span").click()
#         browser.implicitly_wait(2)
#         try : 
#             print("Iam here 3 ")

#             browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[3]/div[1]/div/ul/li[1]/div/ul/li[3]/button").click()
#             browser.implicitly_wait(1)
#             try : 
#                 print("Iam here 4 ")
#                 content =  browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[3]/div[2]/div/pre").text
#                 has_conent=True 
#                 print(content)
#             except:
#                 print("error1")
#                 pass
#         except:
#             print("error2")
#             pass
#     except: 
#             print("error2")
#             pass

    
        


#     time.sleep(2)
#     if has_conent:
#         with open(f"stand-stats2016-2017/{name}-stand-stats.csv","w") as file : 
#             file.write(content)
    
    

# #     browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[3]/div[1]/div/ul/li[1]").click()
# #     browser.implicitly_wait(1)

# #     browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[3]/div[1]/div/ul/li[1]/div/ul/li[3]/button").click()
# #     browser.implicitly_wait(1)
# #     content = browser.find_element(By.XPATH,"/html/body/div[2]/div[6]/div[3]/div[2]/div/pre").text 



    
# #     for j , k in zip(dataframe,list_):
# #         try:
# #             print(k)
# #             dataframe[j].append(str(browser.find_element(By.CSS_SELECTOR,k).text))
# #         except : 
# #             dataframe[j].append(None)
# #     index+=1 
# #     print(index)

# # for i in dataframe:
# #     print(len(dataframe[i]))

# # dataframe["team"]=teams
# # df=pd.DataFrame(dataframe)
# # df.to_csv("teams-stats1.csv")


