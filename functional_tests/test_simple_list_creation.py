from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user_self(self):
        # Edith heard about new app for list
        # urgent tasks. She is deciding to rate her homepage
        self.browser.get(self.live_server_url)

        # She sees, that the header and page header titles the lists
        # of urgent tasks
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        # It is immediately inviting her to enter the item of list
        inputbox = self.get_item_input_box()

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
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page is updating again, and now displays the both of the elements of her list
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        # Edith is interesting, if the site will remember her list?
        # The site generated the unique URL
        # About this displaying the text with explanations

        # She is visiting the URL - her list is still there.

        # Satisfied, she goes back to sleep
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Edith starts a new list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # She notes that her list have the unique URL
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')

        # Now new visitor come to the site.

        # # We use a new session of browser to provide that any information
        # # from Edith not will pass from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the homepage. There are not any attribute of Edith's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('Use peacock feathers to make a fly', page_text)

        # Francis starts a new list with a new item
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy some milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy some milk')

        # Francis get the unique URL:
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # There are not any attributes of Edith's list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy some milk', page_text)

        # Satisfied they go back to sleep
