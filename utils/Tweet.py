import os
import re
import time
from heapq import nlargest

from utils.parser import ObjectRepository


class Tweet(object):
    def __init__(self, driver, url):
        self.locator = ObjectRepository(file_path=os.path.join(os.getcwd(), "actions", "tweet_handle.csv"))
        self.retweet_count = []
        self.driver = driver
        self.likes = []
        self.content = []
        self.hashtag = []
        self.hashtag_counts = dict()
        self.driver.implicitly_wait(10)
        self.listElements=[]
        self.url = url

    def topfifty(self):
        self.driver.get(str(self.url))
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            self.listElements = self.driver.find_elements_by_css_selector(
                'div[class="ProfileTweet-actionList js-actions"]')
            print(len(self.listElements))
            if len(self.listElements) >= 50:
                break

    def get_likes(self):
        self.topfifty()
        for elem in self.listElements:
            try:
             self.likes.append(int(elem.text.split('\n')[elem.text.split('\n').index('Like')+1]))
            except Exception:
                pass
        return self.likes

    def get_retweets(self):
        self.topfifty()
        for elem in self.listElements:
            try:
             self.retweet_count.append(int(elem.text.split('\n')[elem.text.split('\n').index('Retweet')+1]))
            except Exception:
                pass
        return self.retweet_count

    def get_content(self):
        handles = self.driver.find_elements_by_css_selector(self.locator.get_value('hashtags'))
        for elem in handles:
            self.content.append(elem.text)

    def get_hashtag(self):
        self.get_content()
        for elem in self.content:
            self.hashtag.extend(re.findall(r"#(\w+)", elem))

    def word_count(self, restart=True):
        if restart:
            self.get_hashtag()
        for word in self.hashtag:
            if word in self.hashtag_counts:
                self.hashtag_counts[word] += 1
            else:
                self.hashtag_counts[word] = 1

    def get_top_n_likes(self, n):
        self.get_likes()
        Tweet.get_top_n_max_elements(self.likes, int(n))

    def get_top_n_retweets(self, n):
        self.get_retweets()
        Tweet.get_top_n_max_elements(n, self.retweet_count)

    def get_top_n_hashtags(self, n):
        self.get_hashtag()
        self.word_count(restart=True)
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