Feature: Add user API
    @smoke
    Scenario Outline: Check the user is added to the server?
    Given Form the dataset for the post request
    When establish the connection with the database by providing <firstname>, <lastname>, <age>
    Then verify the given result
        Examples:
        | firstname | lastname | age |
        | John  | Deere | 25 |
        | Jane  | Doe   | 30 |
        | Alice | Smith | 28 |


