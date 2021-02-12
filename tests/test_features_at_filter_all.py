from todomvc_testing.model import todomvc

"""
    Supposition:
1. Using Application Manager is irrelevant in this case.

2.Fluent PageObject is used here as improving readability and pleasant for me
tool. 

3. Using Widgets is an excessive and irrelevant complication in this case.

4. Verification of footer state is not relevant for high-level system tests.

5. Explicite verification of following below items is not needed because:
- visibility of "clear-complete" button, because I do it implicitly in
"test_clear_completed"
- invisibility of "clear-complete" button - the result of grey-box reseach
is this UI element doesn't relate with result of app operation perform, that's
why this verification doesn't match homework condition "... покрой все ОПЕРАЦИИ
на фильтре ...", at first, and this verification is not relevant for high-level
system tests, secondly.

6. In "test_complete_all" operation "toggle('b')" is added for simulation more
real situation.
"""


def test_add_one():
    todomvc.visit()

    todomvc.add('a')

    todomvc.should_have('a')\
        .should_have_items_left(1)


def test_add_few():
    todomvc.visit()

    todomvc.add('a', 'b', 'c')

    todomvc.should_have('a', 'b', 'c')\
        .should_have_items_left(3)


def test_edit_by_enter():
    todomvc.visit().add('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')\
        .should_have_items_left(3)


def test_edit_by_focus_change():
    todomvc.visit().add('a', 'b', 'c')

    todomvc.edit_by_tab('b', 'b edited')

    todomvc.should_have('a', 'b edited', 'c')\
        .should_have_items_left(3)


def test_cancel_editing():
    todomvc.visit().add('a', 'b', 'c')

    todomvc.cancel_editing('b', 'b editing')

    todomvc.should_have('a', 'b', 'c')\
        .should_have_items_left(3)


def test_complete():
    todomvc.visit().add('a', 'b', 'c')

    todomvc.toggle('b')

    todomvc.should_have_active('a', 'c')\
        .should_have_completed('b')\
        .should_have_items_left(2)


def test_activate():
    todomvc.visit()\
        .add('a', 'b', 'c')\
        .toggle_all()

    todomvc.toggle('b')

    todomvc.should_have_active('b')\
        .should_have_completed('a', 'c')\
        .should_have_items_left(1)


def test_complete_all():
    todomvc.visit()\
        .add('a', 'b', 'c')\
        .toggle('b')

    todomvc.toggle_all()

    todomvc.should_have_active()\
        .should_have_completed('a', 'b', 'c')\
        .should_have_items_left(0)


def test_clear_completed():
    todomvc.visit()\
        .add('a', 'b', 'c')\
        .toggle('a')\
        .toggle('c')

    todomvc.clear_completed()

    todomvc.should_have('b')\
        .should_have_items_left(1)


def test_activate_all():
    todomvc.visit()\
        .add('a', 'b', 'c')\
        .toggle_all()

    todomvc.toggle_all()

    todomvc.should_have_active('a', 'b', 'c')\
        .should_have_completed()\
        .should_have_items_left(3)


def test_delete_by_click_on_button_x():
    todomvc.visit()\
        .add('a', 'b', 'c')

    todomvc.delete('b')

    todomvc.should_have('a', 'c')\
        .should_have_items_left(2)


def test_delete_by_edit_to_empty_field():
    todomvc.visit()\
        .add('a', 'b', 'c')

    todomvc.edit('b', '')

    todomvc.should_have('a', 'c')\
        .should_have_items_left(2)
