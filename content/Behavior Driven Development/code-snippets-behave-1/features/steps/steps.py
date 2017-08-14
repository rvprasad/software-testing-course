from behave import given, when, then, step
from src import account


@given('my current account has $200')
def current_account_setup(context):
    context.current = account.Account(200)


@step('My savings account has $1000')
def savings_account_setup(context):
    context.savings = account.Account(1000)


@when('I transfer $100 from my current account to savings account')
def execute_transfer(context):
    context.current.transfer(100, context.savings)


@then('I should have $100 in my current account')
def verify_current_account(context):
    assert context.current.amount() == 100


@step('I should have $1100 in my savings account')
def verify_savings_account(context):
    assert context.savings.amount() == 1100

