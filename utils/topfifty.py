from selenium import webdriver
import time
driver = webdriver.Chrome("/Users/deepanshu.ahuja/Documents/chromedriver")
driver.get('https://twitter.com/stepin_forum')


while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    listElements = driver.find_elements_by_css_selector('div[class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt"]')
    print(len(listElements))
    if (len(listElements) >= 50):
        break

for item in listElements:
    print(item.get_attribute("href"))

driver.close()
