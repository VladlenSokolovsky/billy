from selenium.common.exceptions import WebDriverException
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    """Test of the new visitor"""

    def setUp(self):
        """Installation"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Deinstallation"""
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about new app for list
        # urgent tasks. She is deciding to rate her homepage
        self.browser.get(self.live_server_url)

        # She sees, that the header and page header titles the lists
        # of urgent tasks
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # It is immediately inviting her to enter the item of list
        inputbox = self.browser.find_element_by_id('id_new_item')

        # She enters in the text field "Buy peacock feathers" (her hobby is
        # fly knitting)
        inputbox.send_keys('Buy peacock feathers')
        # inputbox.send_keys('Use peacock feathers to make a fly')

        # When she is pressing enter, the page is updating, and now the page
        # contains "1: Buy peacock feathers" like item of the list
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # The text field still inviting her to add one more item
        # She enters "To do the peacock feather fly"
        # (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page is updating again, and now displays the both of the elements of her list
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        # Edith is interesting, if the site will remember her list?
        # The site generated the unique URL
        # About this displaying the text with explanations

        # She is visiting the URL - her list is still there.

        # Satisfied, she goes back to sleep
        self.fail('Finish the test')