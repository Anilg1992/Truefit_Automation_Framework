from selenium import webdriver
import unittest
import pytest
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

class TestCase(unittest.TestCase):
    def _init_(self):
        self.driver = webdriver.Firefox(executable_path="../Drivers/geckodriver.exe")
        
