Feature: Transfer money between accounts
    To manage my money efficiently
    As a bank client
    I want to transfer funds between accts
    
    Scenario Outline: Transfer money with sufficient funds
            Given my current account has $<init1>
            And my savings account has $<init2>
            When I transfer $<withdraw> from my current account to savings account
            Then I should have $<balance1> in my current account
            And I should have $<balance2> in my savings account
            
        Examples: T
            | init1 |   init2   | withdraw  | balance1  | balance2  |
            | 200   | 1000      | 100       | 100       | 1100      |
            | 400   | 3000      | 200       | 200       | 3200      |
    
