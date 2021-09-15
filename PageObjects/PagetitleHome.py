class Home:
    text_by_name_xpath = "//input[@type='text'][@class='form-control']"
    dropdown_by_specialty_xpath = "//select[@name='select'][@aria-label='maaspecialityselectlabel']"
    btn_by_specialty_xpath = "//div[@class='button-div hidden-xs']"

    def __init__(self, driver):
        self.driver = driver

    def by_Specialty(self, specialty):
        self.driver.find_element_by_xpath(self.dropdown_by_specialty_xpath).clear()
        self.driver.find_element_by_xpath(self.dropdown_by_specialty_xpath).sendkeys(specialty)

    def next_Button(self):
        self.driver.find_element_by_xpath(self.btn_by_specialty_xpath).click()
