from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("chromedriver.exe")
browser.get(start_url)
time.sleep(10)
def Scrap():
    headers = ["Star_name", "Distance", "Mass", "Radius"] 
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser") 
        for ul in soup.find_all("ul",attrs={"class",'expoplanet'}):
            li = ul.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapdata.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(planet_data)
Scrap()