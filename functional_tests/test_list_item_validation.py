from .base import FunctionalTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_item(self):

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item"
        ))
        self.browser.find_element(By.ID, 'id_new_item').send_keys('Buy milk')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)

        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, '.has-error').text,
            "You can't have an empty list item"
        ))

        self.browser.find_element(By.ID, 'id_new_item').send_keys('Green tea')
        self.browser.find_element(By.ID, 'id_new_item').send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Green tee')
