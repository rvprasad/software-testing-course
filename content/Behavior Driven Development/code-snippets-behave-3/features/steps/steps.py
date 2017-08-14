from behave import given, when, then, step
from src import account



@given('my current account has ${amount}')
def current_account_setup(context, amount):
    context.current = account.Account(int(amount))


@step('My savings account has ${amount}')
def savings_account_setup(context, amount):
    context.savings = account.Account(int(amount))


@when('I transfer ${amount} from my current account to savings account')
def execute_transfer(context, amount):
    context.current.transfer(int(amount), context.savings)


@then('I should have ${amount} in my current account')
def verify_current_account(context, amount):
    assert context.current.amount() == int(amount)


@step('I should have ${amount} in my savings account')
def verify_savings_account(context, amount):
    assert context.savings.amount() == int(amount)

