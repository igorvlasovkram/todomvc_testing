from todomvc_testing.model import todomvc


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
