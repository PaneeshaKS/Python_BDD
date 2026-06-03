Feature: API Automation using BDD

  Scenario: Add the user
    Given establish the server connection add
    When send the request add
    Then validate the result add