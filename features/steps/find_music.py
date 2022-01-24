from behave import *
from features.helpers.file import file_exists

@given(u'I have the command line program')
def step_impl(context):
    assert file_exists('main.py')


@when(u'I run the program with "coding"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I run the program with "coding"')


@then(u'the output should be a list of three songs')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the output should be a list of three songs')