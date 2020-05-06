from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chromedriver = 'C:/Users/rory/AppData/Local/Programs/Python/Python38/Lib/site-packages/selenium/common/chromedriver'


class TwitterBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password   
        self.bot = webdriver.Chrome()

    def login(self):  
        bot = self.bot
        bot.get("http://twitter.com/")
        time.sleep(3)
        email = bot.find_element_by_name("session[username_or_email]")
        password = bot.find_element_by_name("session[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)
    
    def search_hashtag(self,hashtag):
        bot = self.bot
        bot.get('https://twitter.com/search?q='+ hashtag +'&src=typed_query')
        time.sleep(2)
        for i in range(1,10):
            bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)
            tweets = bot.find_elements_by_id('tweet')
         #   links = [elem.get_attribute('data-permalink-path') for elem in tweets]
  
    def Go_Home(self):
        bot = self.bot
        bot.get('https://twitter.com/home')
        time.sleep(3)
        
  


ed = TwitterBot("Enter Email Here","Enter Password Here")
ed.login()
ed.search_hashtag('Enter Hashtag Here')
ed.Go_Home()