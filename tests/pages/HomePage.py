from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wd
from tests.misc import ConfigData


class Homepage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.CHOSE_FILE_BTN = (By.CSS_SELECTOR, '#inputImage')
        self.TXT_INPUT = (By.NAME, 'text')
        self.CREATE_ITEM_BTN = (By.XPATH, "//button[contains(text(),'Create Item')]")
        self.EDIT_ITEM_BTN = (By.XPATH, "//body/div[@id='content']/div[1]/div[1]/ul[1]/li[last()-1]/div[1]/div[1]/div["
                                        "1]/button[1]")
        self.UPDATE_ITEM_BTN = (By.XPATH, "//button[@class='btn pull-right btn-primary']")
        self.BINDING_TEXT = (By.XPATH, "//h1[@class='ng-binding']")
        self.DELETE_LAST_ITEM_BTN = (By.XPATH, "//body/div[@id='content']/div[1]/div[1]/ul[1]/li[last()]/div[1]/div["
                                               "1]/div[1]/button[2]")
        self.CONFIRM_DELETE_BTN = (By.XPATH, "//button[contains(text(),'Yes, delete it!')]")
        self.TITLE_TXT = (By.XPATH, "//p[@class='story ng-binding']")


    def create_items(self):
        chose_file = wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.CHOSE_FILE_BTN))
        self.driver.execute_script(ConfigData.click_accion, chose_file)
        chose_file.send_keys(ConfigData.image)
        text_input = wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.TXT_INPUT))
        text_input.send_keys(ConfigData.text_input)
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.CREATE_ITEM_BTN)).click()

    def edit_another_item(self):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.EDIT_ITEM_BTN)).click()
        text_input = wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.TXT_INPUT))
        text_input.send_keys(ConfigData.edit_text)
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.UPDATE_ITEM_BTN)).click()

    def delete_last_item(self):
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.DELETE_LAST_ITEM_BTN)) \
            .click()
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.CONFIRM_DELETE_BTN)) \
            .click()

    def check_maxlenght(self):
        chose_file = wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.CHOSE_FILE_BTN))
        self.driver.execute_script("arguments[0].click();", chose_file)
        chose_file.send_keys(ConfigData.image)
        wd(self.driver, self.timeout).until(EC.element_to_be_clickable(self.TXT_INPUT)). \
            send_keys(ConfigData.maxlength + "A")

    def get_attribute_create_btn(self):
        create_item_btn = wd(self.driver, self.timeout).until(EC.visibility_of_element_located(self.CREATE_ITEM_BTN))
        disabled_attribute = create_item_btn.get_attribute("disabled")
        return disabled_attribute

    def check_listitem(self):
        list_title = ""
        list_text = wd(self.driver, self.timeout).until(EC.presence_of_all_elements_located(self.TITLE_TXT))
        for i in range(len(list_text)):
            list_title += list_text[i].text
        return list_title
