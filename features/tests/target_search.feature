# Created by User at 11/15/2023
Feature: Search test
  # Enter feature description here

  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
    Then Verify search worked
    And Verify search result url
