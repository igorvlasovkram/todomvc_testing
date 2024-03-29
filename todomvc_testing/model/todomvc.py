from selene import have
from selene.support.shared import browser

from todomvc_testing.helpers.allure.report import step


class TodoMvc:
    def __init__(self):
        self._todo_list = browser.all('#todo-list>li')

    @step
    def visit(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        browser.should(have.js_returned(
            True,
            "return $._data($('#clear-completed').get(0), 'events')"
            ".hasOwnProperty('click')"
            "&&"
            "Object.keys(require.s.contexts._.defined).length === 39"))
        return self

    @step
    def add(self, *todos: str):
        for todo in todos:
            browser.element('#new-todo').type(todo).press_enter()
        return self

    @step
    def should_have(self, *todos: str):
        self._todo_list.should(have.exact_texts(*todos))
        return self

    @step
    def should_have_items_left(self, amount: int):
        browser.element('#todo-count>strong') \
            .should(have.exact_text(str(amount)))
        return self

    @step
    def should_have_empty_list(self):
        self._todo_list.should(have.size(0))
        return self

    @step
    def should_have_completed(self, *todos: str):
        self._todo_list.filtered_by(have.css_class('completed'))\
            .should(have.exact_texts(*todos))
        return self

    @step
    def should_have_active(self, *todos: str):
        self._todo_list.filtered_by(have.no.css_class('completed'))\
            .should(have.exact_texts(*todos))
        return self

    def _start_editing(self, todo: str, new_text):
        self._todo_list.element_by(have.exact_text(todo)).double_click()
        return self._todo_list.element_by(have.css_class('editing')) \
            .element('.edit').with_(set_value_by_js=True).set_value(new_text)

    @step
    def edit(self, todo: str, new_text):
        self._start_editing(todo, new_text).press_enter()
        return self

    @step
    def cancel_editing(self, todo: str, new_text):
        self._start_editing(todo, new_text).press_escape()
        return self

    @step
    def edit_by_tab(self, todo: str, new_text):
        self._start_editing(todo, new_text).press_tab()
        return self

    @step
    def toggle(self, todo: str):
        self._todo_list.element_by(have.exact_text(todo))\
            .element('.toggle').click()
        return self

    @step
    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    @step
    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    @step
    def delete(self, todo: str):
        self._todo_list.element_by(have.exact_text(todo)).hover()\
            .element('.destroy').click()
        return self
