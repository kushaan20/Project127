from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome("./chromedriver")

browser.get(start_url)
time.sleep(10)

def scrape():
    headers = ['name','distance','mass','radius']
    stars_data = []
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    for ul_tag in soup.find_all('th', attrs = {'class', 'stars'}):
        tr_tags = ul_tag.find_all('tr')
        temp_list = []
        for index, th_tag in enumerate(tr_tags):
            if index == 0:
                temp_list.append(th_tag.find_all('a')[0].contents[0])
            else:
                try:
                    temp_list.append(th_tag.contents[0])
                except:
                    temp_list.append('')
        stars_data.append(temp_list)

    browser.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/table/thead/tr/th[1]/a').click()
    with open('stars_code.csv','w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)

scrape()