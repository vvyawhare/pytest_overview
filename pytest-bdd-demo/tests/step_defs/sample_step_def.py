"""DuckDuckGo Web Browsing feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)


scenarios('../features/sample.feature')



@given('the DuckDuckGo home page is displayed')
def the_duckduckgo_home_page_is_displayed():
    print("given step")

@when('the user searches for "panda"')
def the_user_searches_for_panda():
    print("when step")


@then(parsers.parse('results are shown for {panda}'))
def results_are_shown_for_panda(panda):
    print("then step")
    print(panda)
