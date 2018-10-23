Feature: Testing True Fit
  This feature is to test True fit naviation test from google

#  Scenario: verifying google logo present
#    Given I open a browser
#    When I am loading google url as "http://www.google.com"
#    Then I am making sure google logo is displayed
#    And I am closing the browser
#
#  Scenario: verifying search box is present in Google home page
#    Given I open a browser
#    When I am loading google url as "http://www.google.com"
#    Then I am making sure that search box is present
#    And I am closing the browser
#
#  Scenario: verifying search button is present in Google home page
#    Given I open a browser
#    When I am loading google url as "http://www.google.com"
#    Then I am making sure that search button is present
#    And I am closing the browser
#
  Scenario: verifying clicking search button without any input gives no search results
    Given I open a browser
    When I am loading google url as "http://www.google.com"
    And I am clicking search button without entering anything on textbox
    Then I am still on the google home page and no search results are displayed
    And I am closing the browser
#
#
#  Scenario: verifying entering something on search box and clicking search button gives the search results
#    Given I open a browser
#    When I am loading google url as "http://www.google.com"
#    And I am clicking search button by entering "True Fit" on textbox
#    Then I am making sure that I am getting the search results
#    And I am closing the browser
