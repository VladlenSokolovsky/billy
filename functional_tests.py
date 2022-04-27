from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorsTest(unittest.TestCase):
    """Test of the new visitor"""

    def setUp(self):
        """Installation"""
        self.browser = webdriver.Firefox()

    def tearDown(self):
        """Deinstallation"""
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about new app for list
        # urgent tasks. She is deciding to rate her homepage
        self.browser.get('http://localhost:8000')

        # She sees, that the header and page header titles the lists
        # of urgent tasks
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(by='h1').text
        self.assertIn('To-Do', header_text)

        # It is immediately inviting her to enter the item of list
        inputbox = self.browser.find_element('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She enters in the text field "Buy peacock feathers" (her hobby is
        # fly knitting)
        inputbox.send_keys('Buy peacock feathers')

        # When she is pressing enter, the page is updating, and now the page
        # contains "1: Buy peacock feathers" like item of the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element('id_new_item')
        rows = self.browser.find_elements(by='tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # The text field still inviting her to add one more item
        # She enters "To do the peacock feather fly"
        # (Edith is very methodical)
        self.fail('Finish the test')
        # The page is updating again, and now displays the both of the elements of her list

        # Edith is interesting, if the site will remember her list?
        # The site generated the unique URL
        # About this displaying the text with explanations

        # She is visiting the URL - her list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
