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


@when('I transfer ${amount} from my current account to savings account (modified)')
def execute_transfer(context, amount):
    try:
        context.curr_amount = context.current.amount()
        context.sav_amount = context.savings.amount()
        context.current.transfer(int(amount), context.savings)
        context.exception = None
    except RuntimeError as e:
        context.exception = e


@then('I should see an error message "Insufficient funds"')
def step_impl(context):
    assert context.exception.args[0] == "Insufficient funds"
    

@then('the amount in my current account should be unchanged')
def step_impl(context):
    assert context.current.amount() == context.curr_amount


@then('the amount in my savings account should be unchanged')
def step_impl(context):
    assert context.savings.amount() == context.sav_amount
