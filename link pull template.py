from selenium import webdriver #import selenium webdriver
import time #imports time module
import pickle
#from selenium.webdriver.remote.webelement import WebElement
#from selenium.common.exceptions import StaleElementReferenceException


driver = webdriver.Chrome(executable_path='C:/Users/benti/PhantomJS/ChromeDriver/chromedriver')
time.sleep(3)
driver.get("https://www.metacritic.com/game/switch/the-legend-of-zelda-breath-of-the-wild/critic-reviews")

links = driver.find_elements_by_tag_name('a.external') #pulls all elements with the a.external tag - outbound links

reviews = []

for link in links:
    reviews.append(link.get_attribute('href'))
#    print(link.get_attribute('href'))
    
#print(reviews)
#print(len(reviews))

sr = set(reviews)
for link in reviews:
    sr.add(link)



lr = list(sr)
print(lr) 

with open('BOTWlist','wb') as zelda:
    pickle.dump(lr, zelda)
driver.close() 

#    
#print(sr)
#print(len(sr))
#print(sr)