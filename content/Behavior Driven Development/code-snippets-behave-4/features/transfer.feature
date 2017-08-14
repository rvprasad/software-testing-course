Feature: Transfer money between accounts
  To manage my money efficiently
  As a bank client
  I want to transfer funds between accts

  Scenario: Transfer money with sufficient funds
    Given my current account has $200
    And my savings account has $1000
    When I transfer $100 from my current account to savings account
    Then I should have $100 in my current account
    And I should have $1100 in my savings account

  Scenario: Transfer money with insufficient funds
    Given my current account has $200
    And my savings account has $1000
    When I transfer $500 from my current account to savings account (modified)
    Then I should see an error message "Insufficient funds"
    And the amount in my savings account should be unchanged
    And the amount in my current account should be unchanged
