from behave import given, when, then
from src import impl


@given('a network')
def create_network(context):
    context.network1 = impl.Network()
    context.name2person = {}


@given('with {name} as a person')
def create_person(context, name):
    tmp1 = context.network1.create_person()
    context.network1.add_person_property(tmp1, 'name', name)
    context.name2person[name] = tmp1


@given('with {name1} and {name2} as friends')
def create_friendship(context, name1, name2):
    tmp1 = context.name2person[name1]
    tmp2 = context.name2person[name2]
    context.network1.add_relation(tmp1, tmp2)
    context.network1.add_relation_property(tmp1, tmp2, 'friend', True)


@given('with {name1} and {name2} as past friends')
def remove_friendship(context, name1, name2):
    tmp1 = context.name2person[name1]
    tmp2 = context.name2person[name2]
    context.network1.add_relation(tmp1, tmp2)
    context.network1.add_relation_property(tmp1, tmp2, 'friend', False)


@when('we query for friends of friends of {name}')
def query_fof(context, name):
    try:
        context.result = context.network1.friends_of_friends(name)
    except RuntimeError as e:
        context.exception = e


@then('we get an empty list of people')
def verify_result(context):
    assert context.result == []


@then('we get {name1} and {name2} as friends of friends')
def fof_exist(context, name1, name2):
    assert set(context.result) == set([context.network1.get_person(name1),
                                       context.network1.get_person(name2)])


@then('we get an error message saying "There is no person named Tom"')
def step_impl(context):
    assert isinstance(context.exception, RuntimeError)


@then('we get {name} as friends of friends')
def step_impl(context, name):
    assert set([context.network1.get_person(name)]) == set(context.result)
