Feature: Target.com

  Scenario: User opens sign in form from header
    Given logged out user opens target.com
    When user clicks Sign In in header
    And user clicks Sign In from right side navigation menu
    Then Sign In form is opened

  Scenario: User adds a product to cart
    Given user opens target.com
    When user searches for "apple airpods"
    And user clicks on first product
    And user clicks Add to Cart button
    Then product is added to cart successfully

  Scenario: User logs in with valid credentials
    Given user opens target.com
    When user clicks Sign In in header
    And user clicks Sign In from side navigation
    And user inputs email "akhmadsaitov.0420@gmail.com"
    And user inputs password "123Qwerty."
    And user clicks Sign In button
    Then user is logged in and Sign In form disappears


