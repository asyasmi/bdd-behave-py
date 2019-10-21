import os
from behave import given

base_url = os.environ.get('BASE_URL', 'https://github.com').rstrip('/')
assert base_url.startswith(('http://', 'https://')), "Protocol isn't specified"
pages = {
    'home': base_url,
    'about': base_url + '/about'
}


@given("user on '{page}' page")
def user_on_page(context, page):
    context.browser.get(pages[page])
