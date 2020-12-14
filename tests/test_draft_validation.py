from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_basic_management():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.wait_to(have.js_returned
                    (True, 'return Object.keys(require.s.contexts._.defined).length === 39'))

    s('#new-todo').type('a').press_enter()
    s('#new-todo').type('b').press_enter()
    s('#new-todo').type('c').press_enter()
    ss('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    ss('#todo-list>li').element_by(have.exact_text('b')).double_click()
    ss('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
        .type(' edited').press_enter()

    ss('#todo-list>li').element_by(have.exact_text('b edited'))\
        .element('.toggle').click()

    s('#clear-completed').click()
    ss('#todo-list>li').should(have.exact_texts('a', 'c'))

    ss('#todo-list>li').element_by(have.exact_text('c')).double_click()
    ss('#todo-list>li').element_by(have.css_class('editing')).element('.edit')\
        .type(' to be canceled').press_escape()

    ss('#todo-list>li').element_by(have.exact_text('c')).hover()\
        .element('.destroy').click()
    ss('#todo-list>li').should(have.exact_texts('a'))
