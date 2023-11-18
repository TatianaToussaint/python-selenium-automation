# Created by User at 11/17/2023
Feature: Circle page UI tests
  # Enter feature description here

  Scenario: Confirm five benefit boxes are present
    Given Open Circle page
    When User view the main section
    Then Five benefit boxes are present
