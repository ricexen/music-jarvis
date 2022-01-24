Feature: Find music

Scenario: Find music to code
    Given I have the command line program
    When I run the program with "coding"
    Then the output should be a list of three songs