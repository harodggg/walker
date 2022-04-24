#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from enum import Enum, unique
import time
# 1 kjfkdlz@gmail.com
# 2 tiansheng849@gmail.com
# 3 guoshengsa@gmail.com
# 4 h49657753@gmail.com
# 5 haroldtianshengss@gmail.com
# 6 hdarodgakjdf@gmail.com
# 7 kgjkajkfjd@gmail.com
# 8 ahkdjfkaljdf@gmail.com
# 9 harolgace1@gmail.com
# 10 haroldsheng123@gmail.com
# 11 haroldtianasheng@gmail.com
# 12 harodggg@gmail.com
# default user = /Users/g/Library/Application Support/Google/Chrome/Default


# Profile 14
# if 

cath_web = "https://walken.io/cathletes/"
compe = "https://walken.io/competitions"
# https://walken.io/competitions/disciplines


def click_got_it(driver):
    for i in range(10):
        try:
            got_it_button = driver.find_element_by_xpath(
            "/html/body/div/div[1]/div/div/div/button")
            print("已找到got_it")
            got_it_button.click()
            break
        except:
            time.sleep(2)
            print("加载还未完成")
            if driver.current_url == "https://walken.io/signin":
                return 0 


user_data = '/Users/g/Library/Application Support/Google/Chrome/'

Strength = 0.5

Stamina = 0.8

Speed = 0.1 


Energy = 0

Level = ""

@unique
class Property(Enum):
    Strength = 0 
    Stamina = 1 
    Speed = 2

# find max property value by  Strength, Stamina Speed. 
def max_value_property(strength,stamina,speed):
    if strength > stamina:
        if strength > speed:
            return Property.Strength
        else:
            return Property.Speed
    elif stamina > speed:
        return Property.Stamina
    else:
        return Property.Speed

def select_user(user):
    option = webdriver.ChromeOptions()
    #option.add_argument('--headless')

    option.add_argument("--user-data-dir=" + user_data)
    option.add_argument(
    "--profile-directory="+ user)
    return option


#option = select_user("Profile 13")
#driver = webdriver.Chrome(chrome_options=option)
#driver.get(cath_web)
#click_got_it()
#time.sleep(10)

#cath_name = ""

# cath_name_span = driver.find_elements_by_xpath(
#             "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[4]/span")
# for c in cath_name_span:
#     cath_name = c.text + cath_name
# print(cath_name)
# print("加载完成")



#cath_name = ""

#for c in cath_name_span:
#    cath_name = c.text + cath_name
#print(cath_name)


# enery_span = driver.find_elements_by_xpath(
#     "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[5]/div[2]/div/span[1]")
# for e in enery_span:
#     Energy = e.text

# Energy = Energy[0]
# print(Energy)

#driver.get(cath_web + cath_name.lower())
#driver.get(cath_web + cath_name.lower())
# /html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/span[1]

#time.sleep(5)

#enery_span = driver.find_element_by_xpath(
#    "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div/div/span[1]")
#for e in enery_span:
#    Energy = e.text 
#print(Energy)


# time.sleep(10)
# level_span = driver.find_elements_by_xpath(
#     "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div[1]/div/span")
# print(level_span)
# for l in level_span:
#     Level = l.text + Level
# Level = Level[-1]
# print(Level)

def get_proprety(driver):
    strength_span = driver.find_elements_by_xpath(
        "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div[3]/div[1]/div/div[1]/div[2]/div[2]/div/span[1]"
    )
    for s in strength_span:
        Strength = s.text
    print(Strength)

    stamina_span = driver.find_elements_by_xpath(
        "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div[3]/div[2]/div/div[1]/div[2]/div[2]/div/span[1]")
    for s in stamina_span:
        Stamina = s.text
    print(Stamina)

    speed_span = driver.find_elements_by_xpath(
        "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div[3]/div[3]/div/div[1]/div[2]/div[2]/div/span[1]")
    for s in speed_span:
        Speed = s.text
    print(Speed)

# get_proprety()

# max_value = max_value_property(Strength, Stamina, Speed)
# print(max_value)

# driver.get(compe)
# time.sleep(10)
def wallet_login(driver):
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button[1]").click()
    except:
        driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/button[1]").click()
    finally:
        print("钱包登入成功")



def start_compe(driver,Level,Energy,max_value):
    for i in range(int(Energy)):
        if int(Energy) == 0:
            break
        print(Energy)
        wallet_login(driver)

        select_level_btn = None
        for i in range(3):
            try:   
                
                if int(Level) == 1 or int(Level) == 0 : 
                    select_level_btn = driver.find_element_by_xpath(
                        "/html/body/div/div[2]/main/div[1]/div/div/div/div/div[1]/div")
                else:
                    select_level_btn = driver.find_element_by_xpath(
                    "/html/body/div/div[2]/main/div[1]/div/div/div/div/div[2]/div/div")
                break
            except:
                time.sleep(2)

                print("加载失败")
        select_level = ActionChains(driver)
        select_level.click(select_level_btn)
        select_level.perform()

        # if int(Level) == 0 or int(Level)== 1:
        #     btn = driver.find_element_by_xpath(
        #         "/html/body/div/div[2]/main/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]")
        #     ActionChains(driver).click(btn).perform()

        # else: 
        #     btn = driver.find_element_by_xpath(
        #         "/html/body/div/div[2]/main/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]")
        #     ActionChains(driver).click(btn).perform()

        select_compe(max_value,driver)
        btn = driver.find_element_by_xpath(
            "/html/body/div/div[1]/div/div/div/div/div[2]/div[1]")
        ActionChains(driver).click(btn).perform()

        btn = driver.find_element_by_xpath(
            "/html/body/div/div[1]/div/div/div/div/div[2]/button")
        btn.click()
        
        time.sleep(10)
        if int(Energy) == 0:
            break
        driver.get("https://walken.io/competitions")
        time.sleep(5)

def select_compe(pro,driver):
    time.sleep(2)
    if pro == Property.Speed:
        btn = driver.find_element_by_xpath(
            "/html/body/div/div[2]/main/div[1]/div/div/div/div[2]/div[1]/div/div/div[1]")
        ActionChains(driver).click(btn).perform()
    elif pro == Property.Strength:
        btn = driver.find_element_by_xpath(
            "/html/body/div/div[2]/main/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]")
        ActionChains(driver).click(btn).perform()
    else:
        btn = driver.find_element_by_xpath(
            "/html/body/div/div[2]/main/div[1]/div/div/div/div[2]/div[3]/div/div/div[1]")
        ActionChains(driver).click(btn).perform()
        

#select_compe(max_value)        
# start_compe()

# time.sleep(50)
# driver.quit()

#time.sleep(10)
#got_it_button = driver.find_element_by_xpath("/html/body/div/div[1]/div/div/div/button")
#got_it_button.click()



class Walker:
    def __init__(self, user):
        self.driver = webdriver.Chrome(chrome_options=select_user(user))
    
    def login(self):
        print("登入")
    
    def comepition(self):
        print("比赛")

    def upgrade_grade(self):
        print("分数")

class W(webdriver.Chrome):
    def __init__(self, chrome_options=None):
        super(W,self).__init__(chrome_options=chrome_options)


def start_work(user):

    Strength = 0.5
    Stamina = 0.8
    Speed = 0.1
    Energy = 0
    Level = ""

    option = select_user(user)
    driver = webdriver.Chrome("/Users/g/chromedriver",chrome_options=option)
    driver.get(cath_web)
    got_it_status = click_got_it(driver)
    time.sleep(10)
    if got_it_status == 0:
        return 0
    cath_name = ""
    cath_name_span = driver.find_elements_by_xpath(
        "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[4]/span")
    for c in cath_name_span:
        cath_name = c.text + cath_name
    print(cath_name)
    print("加载完成")

    enery_span = driver.find_elements_by_xpath(
        "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[5]/div[2]/div/span[1]")


    for e in enery_span:
        Energy = e.text
    try:
        Energy = Energy[0]

    except:
        print("Energy出现问题")
        Energy = "3"
    
    print("Energy:" + Energy)


    driver.get(cath_web + cath_name.lower())

    time.sleep(10)


    level_span = driver.find_elements_by_xpath(
        "/html/body/div/div[2]/main/div[1]/div/div/div[2]/div[1]/div[3]/div/div/div[1]/div/span")
    for l in level_span:
        Level = l.text + Level
    try:
        Level = Level[-1]
    except:
        Level = "2"
    print("Level:" + Level)

    get_proprety(driver)


    max_value = max_value_property(Strength, Stamina, Speed)
    print(max_value)

    driver.get(compe)
    time.sleep(10)

    
    start_compe(driver,Level,Energy,max_value)


    time.sleep(5)
    driver.quit()



for i in range(1,20):
    if i == 2 or i == 5 or i == 6 or i == 7 or i == 8 or i == 19: 
        continue
    try:
        start_work("Profile " + str(i))
    except:
        print("失败" + str(i))

