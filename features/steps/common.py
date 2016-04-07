from behave import given


pages = {
    'home': 'http://linuxhub.ru'
}


@given("user on '{page}' page")
def step_impl(context, page):
    context.browser.get(pages[page])
