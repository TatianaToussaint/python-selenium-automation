Feature: Search test
  # Enter feature description here
  
  Scenario: User can search for a product
    Given Open target main page
    When Search for coffee
   Then Verify search worked for coffee
    And Verify coffee in search result url

  Scenario: : User can search for a tea
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea
    And Verify tea in search result url

  Scenario: : User can search for a mug
    Given Open target main page
    When Search for christmas lights
    Then Verify search worked for christmas lights
    And Verify christmas+lights in search result url

  Scenario Outline: User can search a product
    Given Open target main page
    When Search for <product>
    Then Verify search worked for <expected_product>
    And Verify <expected_url> in search result url
    Examples:
    |product          |expected_product |expected_url     |
    |coffee           |coffee           |coffee           |
    |tea              |tea              |tea              |
    |mug              |mug              |mug              |
    |christmas lights |christmas lights |christmas+lights |

Scenario: : User can add a product to card
    Given Open target main page
    When Search for AirPods (3rd Generation)
    And Click on add to Cart button
    And Store product name
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image

