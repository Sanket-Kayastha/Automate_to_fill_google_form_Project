import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"}
response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/", headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup)

href = []
# for link in soup.find_all('a'):
#     total_link = link.get('href')
#     href.append(total_link)
# location_link = href[9:25:2]
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a") 
# print(all_link_elements)
for link in all_link_elements:
    link = [link["href"]]
    href.append(link)
#print(f"\n After having been cleaned up, the {len(href)} link now look like this: \n")


All_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in All_address_elements]
# print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
# print(all_addresses)
# for address in All_address_elements:
#     text = address.get_text().replace(",|").strip()
#     print(text)
    

all_price_elements = soup.select(".PropertyCardWrapper span")
all_price = [price.get_text().strip("+/mo+ 1bd") for price in all_price_elements]


chromeoptions=webdriver.ChromeOptions()
chromeoptions.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chromeoptions)
driver.maximize_window() 
driver.implicitly_wait(10)

driver.get(url="https://forms.gle/E9AV2LXfkrDvHhBv7")

for n in range(len(all_addresses)):
    question1 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question1.clear()

    question1.send_keys(all_addresses[n])

    question2 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question2.clear()

    question2.send_keys(all_price[n])

    question3 = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    question3.clear()

    question3.send_keys(href[n])

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    send_another_response = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    send_another_response.click()