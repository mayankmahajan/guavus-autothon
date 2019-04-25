import re
import time

from selenium import webdriver
from heapq import nlargest


class Tweet(object):
    def __init__(self,driver):
        self.retweet_count = []
        self.driver = driver
        self.likes = []
        self.content = []
        self.hashtag = []
        self.hashtag_counts = dict()
        self.driver.implicitly_wait(10)
        self.listElements=[]

    def topfifty(self):
        self.driver.get("https://twitter.com/stepin_forum")
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            self.listElements = self.driver.find_elements_by_css_selector(
                'div[class="ProfileTweet-actionList js-actions"]')
            print(len(self.listElements))
            if len(self.listElements) >= 50:
                break

    def get_likes(self):
        for elem in self.listElements:
            try:
             self.likes.append(int(elem.text.split('\n')[elem.text.split('\n').index('Like')+1]))
            except Exception:
                pass
        return self.likes

    def get_retweets(self):
        for elem in self.listElements:
            try:
             self.retweet_count.append(int(elem.text.split('\n')[elem.text.split('\n').index('Retweet')+1]))
            except Exception:
                pass
        return self.retweet_count

    def get_content(self, locator):
        self.driver.find_elements_by_css_selector(locator)
        for elem in self.driver.find_elements_by_css_selector(locator):
            self.content.append(elem.text)

    def get_hashtag(self, locator):
        self.get_content(locator)
        for elem in self.content:
            self.hashtag.extend(re.findall(r"#(\w+)", elem))

    def word_count(self, locator=None, restart=True):
        if restart:
            self.get_hashtag(locator)
        for word in self.hashtag:
            if word in self.hashtag_counts:
                self.hashtag_counts[word] += 1
            else:
                self.hashtag_counts[word] = 1

    def get_top_n_likes(self, n, locator=None):
        if locator is not None:
            self.get_likes(locator)
        Tweet.get_top_n_max_elements(self.likes, int(n))

    def get_top_n_retweets(self, n, locator=None):
        if locator is not None:
            self.get_retweets(locator)
        Tweet.get_top_n_max_elements(n, self.retweet_count)

    def get_top_n_hashtags(self, n, locator=None):
        self.word_count(locator, restart=True)
        n_largest = nlargest(n, self.hashtag_counts, key=self.hashtag_counts.get)
        return n_largest


    @staticmethod
    def get_top_n_max_elements(elem_list, N):
        final_list = []

        for i in range(0, N):
            max1 = 0

            for j in range(len(elem_list)):
                if elem_list[j] > max1:
                    max1 = elem_list[j]

            elem_list.remove(max1)
            final_list.append(max1)

        return final_list


obj = Tweet(driver = webdriver.Chrome(executable_path="/Users/anubhav.gupta/Downloads/chromedriver"))
obj.topfifty()
obj.get_likes()
obj.get_retweets()
# obj.get_retweets('div[class="ProfileTweet-action ProfileTweet-action--retweet js-toggleState js-toggleRt"]')
# obj.get_likes('div[class="ProfileTweet-action ProfileTweet-action--favorite js-toggleState"]')
# print obj.retweet_count
# print len(obj.retweet_count)
# print obj.likes
# print len(obj.likes)
# obj.get_content('p[class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]')
# obj.get_hashtag()
# print obj.content
# print obj.hashtag
# obj.word_count('p[class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]tweet-text')
# print obj.hashtag_counts
# print obj.get_top_n_hashtags(10, 'p[class="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"]')