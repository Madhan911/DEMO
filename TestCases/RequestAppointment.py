import pytest
from selenium import webdriver
from PageObjects.PagetitleHome import Home
from Utilities.readProperties import readConfig


@pytest.mark.usefixtures("setup1")
class Test_Appointment(BasicTest):

    baseURL = readConfig.getApllicationURL()

    def test_homepageTitel(self, setup):

        # self.logger.info("****************Test_001_Login*************  ")
        # self.logger.info("**************** Verifying home page title *************  ")
        log = self.getLogger()
        log.info("Launching amazon website")
        self.driver.get(baseURL)
        act_title = self.driver.title

        if act_title == "Request an Appointment | Mount Sinai - New York":
            assert True
            self.driver.close()
            # self.logger.info("****************Homepage title test is passed *************  ")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            # self.logger.error("****************Homepage title test is failed *************  ")
            assert False
