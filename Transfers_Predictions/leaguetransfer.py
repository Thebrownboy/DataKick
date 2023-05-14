from selenium import webdriver
import time 

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd 
import numpy as np 

season_link = "https://www.transfermarkt.com/premier-league/transfers/wettbewerb/GB1/plus/?saison_id=2017&s_w=s&leihe=0&intern=0&intern=1"
browser= webdriver.Chrome(ChromeDriverManager().install())


browser.set_page_load_timeout(15)


try :
    browser.get(season_link)
    # just to catch the timeout error 
except:
    pass

browser.set_page_load_timeout(10)

time.sleep(5)     



data_frame={"team":[],"Goalkeeper":[],"Right-Back":[],"Left-Back":[],"Centre-Back":[],"DefensiveMidfield":[],"RightWinger":[],
            "LeftWinger":[],"CentralMidfield":[],"Centre-Forward":[],"AttackingMidfield":[],"LeftMidfield":[],"SecondStriker":[]}

for i in range (20):
    GK,RB,LB,CB,DMF,RW,LW,CMF,CF,AMF,LMF,SS=0,0,0,0,0,0,0,0,0,0,0,0
    try :
        team_name=browser.find_element(By.XPATH,f"/html/body/div[2]/main/div[2]/div[1]/div[{4+i}]/h2").text
        data_frame["team"].append(team_name)
        trs= browser.find_elements(By.CSS_SELECTOR,f"#main > main > div:nth-child(6) > div.large-8.columns > div:nth-child({4+i}) > div:nth-child(2) > table > tbody > tr")
        for j in range(len(trs)):
            td=browser.find_element(By.CSS_SELECTOR,f"#main > main > div:nth-child(6) > div.large-8.columns > div:nth-child({4+i}) > div:nth-child(2) > table > tbody > tr:nth-child({j+1}) > td.pos-transfer-cell").text
            if "Goalkeeper" in td:
                GK+=1
            elif "Right-Back"in td :
                RB+=1
            elif "Left-Back" in td :
                LB+=1
            elif "Centre-Back" in td :
                CB+=1
            elif "Defensive Midfield" in td :
                DMF+1
            elif "Right Winger" in td :
                RW+=1
            elif "Left Winger" in td : 
                LW+=1
            elif "Central Midfield" in td :
                CMF+=1
            elif "Centre-Forward" in td :
                CF+=1
            elif "Attacking Midfield" in td :
                AMF+=1 
            elif "Left Midfield" in td : 
                LMF+=1 
            elif "Second Striker":
                SS+=1
            else :
                print(td)
        
        data_frame["Goalkeeper"].append(GK)
        data_frame["Right-Back"].append(RB)
        data_frame["Left-Back"].append(LB)
        data_frame["Centre-Back"].append(CF)
        data_frame["DefensiveMidfield"].append(DMF)
        data_frame["RightWinger"].append(RW)
        data_frame["LeftWinger"].append(LW)
        data_frame["CentralMidfield"].append(CMF)
        data_frame["Centre-Forward"].append(CF)
        data_frame["AttackingMidfield"].append(AMF)
        data_frame["LeftMidfield"].append(LMF)
        data_frame["SecondStriker"].append(SS)
        
    except Exception as e  :
        print(e)


    


# data_frame={"team":[],"Goalkeeper":[],"Right-Back":[],"Left-Back":[],"Centre-Back":[],"DefensiveMidfield":[],"RightWinger":[],
#             "LeftWinger":[],"CentralMidfield":[],"Centre-Forward":[],"AttackingMidfield":[]}

# # df = pd.DataFrame(transfer_data)

# # df.to_csv("trans-temp.csv")

pd.DataFrame(data_frame).to_csv("transfers-2017-2018.csv")

