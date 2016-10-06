import os
from behave import given

base_url = os.environ.get('BASE_URL', 'http://linuxhub.ru').rstrip('/')
assert base_url.startswith(('http://', 'https://')), "Protocol isn't specified"
pages = {
    'home': base_url,
    'links': base_url + '/links.php'
}


@given("user on '{page}' page")
def step_impl(context, page):
    context.browser.get(pages[page])
