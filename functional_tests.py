from selenium import webdriver
import unittest

class NewVisitorsTest(unittest.TestCase):
    '''Test of the new visitor'''

    def setUp(self):
        '''Installation'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''Deinstallation'''
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith heard about new app for list
        # urgent tasks. She is deciding to rate her homepage
        self.browser.get('http://localhost:8000')

        # She sees, that the header and page header titles the lists
        # of urgent tasks
        self.assertIn('To-Do', self.browser.title)
        self.fail('To finish the test')

        # It is immediately inviting her to enter the item of list

        # She enters in the text field "Buy peacock feathers" (her hobby is
        # fly knitting)

        # When she is pressing enter, the page is updating, and now the page
        # contains "1: Buy peacock feathers" like item of the list

        # The text field still inviting her to add one more item
        # She enters "To do the peacock feather fly"
        # (Edith is very methodical)

        # The page is updating again, and now displays the both of the elements of her list

        # Edith is interesting, if the site will remember her list?
        # The site generated the unique URL
        # About this displaying the text with explanations

        # She is visiting the URL - her list is still there.

        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
