from selenium import webdriver
from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        
    def login(self):
        self.driver.get('https://tinder.com')
        
        sleep(3)

        fb_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_button.click()

        # save default window
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        email.send_keys(username)

        mdp = self.driver.find_element_by_xpath('//*[@id="pass"]')
        mdp.send_keys(password)

        login = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login.click()

        sleep(3)

        self.driver.switch_to_window(base_window)

        sleep(3)

        emplacement = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        emplacement.click()

        notification = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        notification.click()

    def like(self):
        like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like.click()
    
    def dislike(self):
        dislike = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike.click()
    
    def auto(self):
        while True:
            sleep(0.75)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()

    def close_popup(self):
        accueil = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        accueil.click()

    # TODO : à vérifier :'( (prendre le compte à Rayan c'est un bg)
    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
sleep(2)
bot.auto()