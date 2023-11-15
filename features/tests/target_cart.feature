# Created by User at 11/15/2023
Feature: Cart
  # Enter feature description here

  Scenario: User can see message
    Given Open target main page
    When Click on cart icon
    Then Verify “Your cart is empty” message is shown
