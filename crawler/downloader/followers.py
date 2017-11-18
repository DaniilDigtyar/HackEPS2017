import time

from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from hackeps import tasks


class InstagramFollowers(object):

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(chrome_options=options)

    def find(self, username, followers):
        """ return the username's follower names """
        try:
            self._login()
            follower_names = self._scrape_followers(username, followers)
        finally:
            self.driver.quit()

        tasks.crawl_profiles('instagram', follower_names)

    def _login(self):
        """ Log in to instagram """
        # Load page
        self.driver.get(
            'https://www.instagram.com/accounts/login/?force_classic_login')

        self.driver.find_element_by_xpath(
            "//input[@id='id_username']").send_keys(
                settings.INSTAGRAM['username'])
        self.driver.find_element_by_xpath(
            "//input[@id='id_password']").send_keys(
                settings.INSTAGRAM['password'])
        self.driver.find_element_by_xpath("//input[@value='Log in']").click()

    def _scrape_followers(self, account, followers):
        """ scrape instagram followers. This task can take some minutes.. """
        # Load account page
        self.driver.get('https://instagram.com/{}/'.format(account))

        # Click the 'Followers' link
        self.driver.find_element_by_partial_link_text('followers').click()

        # Wait for the followers modal
        xpath = "//div[@class='_gs38e']"
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, xpath)))

        # Scroll to the bottom of the followers list
        scroll_down = (
            "document.getElementsByClassName('_gs38e')"
            "[0].scrollTo(0, 10000);")
        for _ in range(int(followers / 10) + 1):
            self.driver.execute_script(scroll_down)
            # Wait one second
            time.sleep(1)

        # Scrape the followers
        xpath = "//div[@class='_gs38e']//ul/div/li/div/div/div/div/a"
        followers_elems = self.driver.find_elements_by_xpath(xpath)
        return [e.text for e in followers_elems]
