import unittest
import pytest

from Utility.TestCase import TestCase
from selenium import webdriver
import os
from selenium.common.exceptions import *
import Utility.CustomLogger as cl
import logging
import time
from behave import *

class Defination():
    log = cl.customLogger(logging.DEBUG)
    def _init_(self):
        self.driver = None
    def __del__(self):
        self.driver.quit()
    @Given("I open a browser")
    def I_pen_a_browser(self):
        self.driver = webdriver.Firefox(
            executable_path="../True_Fit_Automation_Framework/Drivers/geckodriver.exe")

    @When("I am loading google page")
    def I_am_loading_google_page(self):
        self.driver.get("http://www.google.com")

    @When("I am loading google url as \"{url}\"")
    def I_am_loading_google_url_as(self, url):
        self.driver.get(url)

    @Then("I am making sure google logo is displayed")
    def I_am_making_sure_google_logo_is_displayed(self):
        try:
            self.driver.find_element_by_xpath("//img[@id='hplogo']")
        except NoSuchElementException:
            self.screenShot("I_am_making_sure_google_logo_is_displayed")
            return False
    @Then("I am making sure that search box is present")
    def I_am_making_sure_that_search_box_is_present(self):
        try:
            self.driver.find_element_by_id("lst-ib")
        except NoSuchElementException:
            self.screenShot("I_am_making_sure_that_search_box_is_present")
            return False

    @Then("I am making sure that search button is present")
    def I_am_making_sure_that_search_button_is_present(self):
        try:
            self.driver.find_element_by_name("btnK")
        except NoSuchElementException:
            self.screenShot("I am making sure that search button is present")
            return False

    @When("I am clicking search button without entering anything on textbox")
    def I_am_clicking_search_button_without_entering_anything_on_textbox(self):
        print("User clicking search button in page")
        self.driver.find_element_by_xpath("//*[@class='A8SBwf']//div[@class='FPdoLc VlcLAe']//input[1]").click()
        print("User click search button in page and nothing happened")
    @Then("I am still on the google home page and no search results are displayed")
    def I_am_still_on_the_google_home_page_and_no_search_results_are_displayed(self):
        try:
            self.driver.find_element_by_name("btnI")
        except NoSuchElementException:
            self.screenShot("I am still on the google home page and no search results are displayed")
            return False

    @When("I am clicking search button by entering \"{input}\" on textbox")
    def I_am_clicking_search_button_by_entering(self, input):
        self.driver.find_element_by_xpath("//*[@title='Search']").send_keys(input)
        self.driver.find_element_by_xpath("//*[@class='A8SBwf']//div[@class='FPdoLc VlcLAe']//input[1]").click()

    @Then("I am making sure that I am getting the search results")
    def I_am_making_sure_that_I_am_getting_the_search_results(self):
        try:
            self.driver.find_elements_by_xpath("//a[contains(@href,'truefit')]")
        except NoSuchElementException:
            self.screenShot("I am making sure that I am getting the search results")
            return False


    @Then("I am closing the browser")
    def I_am_closing_the_browser(self):
        print("User closing the browser")
        self.driver.close()


    def screenShot(self, resultMessage):
        fileName = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshots/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)
        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("Screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occurred when taking screenshot")

