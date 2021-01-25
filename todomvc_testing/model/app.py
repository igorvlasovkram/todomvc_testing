from selene import have, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss

todo_list = ss('#todo-list>li')


def visit():
    browser.open('https://todomvc4tasj.herokuapp.com/')
    browser.wait_to(have.js_returned
        (True, 'return Object.keys(require.s.contexts._.defined).length === 39'))


def add(*todos: str):
    for todo in todos:
        s('#new-todo').type(todo).press_enter()


def should_have(*todos: str):
    todo_list.should(have.exact_texts(*todos))


def edit(todo: str, new_text):
    start_editing(todo, new_text).press_enter()


def cancel_editing(todo: str, new_text):
    start_editing(todo, new_text).press_escape()


def start_editing(todo: str, new_text):
    todo_list.element_by(have.exact_text(todo)).double_click()
    return todo_list.element_by(have.css_class('editing')).element('.edit') \
        .perform(command.js.set_value(new_text))


def toggle(todo: str):
    todo_list.element_by(have.exact_text(todo)) \
        .element('.toggle').click()


def clear_completed():
    s('#clear-completed').click()


def delete(todo: str):
    todo_list.element_by(have.exact_text(todo)).hover() \
        .element('.destroy').click()
