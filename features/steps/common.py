import os
from behave import given, then

base_url = os.environ.get('BASE_URL', 'https://github.com').rstrip('/')
assert base_url.startswith(('http://', 'https://')), "Protocol isn't specified"
status_url = os.environ.get('STATUS_BASE_URL', 'https://www.githubstatus.com/')
pages = {
    'home': base_url,
    'about': base_url + '/about',
    'status_page':  status_url,
}


@given("user on '{page}' page")
def user_on_page(context, page):
    context.browser.get(pages[page])


@then("set cookie '{name}' to '{value}'")
def set_cookie(context, name, value):
    context.browser.add_cookie({
        u'domain': u'.github.com',
        u'secure': True,
        u'value': value,
        'name': name,
        'path': '/'
    })
    context.browser.refresh()


@then("user is redirected to page '{page}'")
def then_user_on_page(context, page):
    assert context.browser.current_url == pages[page], "'%s' != '%s'" % (context.browser.current_url, pages[page])