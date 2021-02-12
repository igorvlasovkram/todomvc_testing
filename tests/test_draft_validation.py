from todomvc_testing.model import todomvc


def test_basic_management():
    todomvc.visit()

    todomvc.add('a', 'b', 'c') \
        .should_have('a', 'b', 'c')

    todomvc.edit('b', 'b edited')

    todomvc.toggle('b edited')

    todomvc.clear_completed() \
        .should_have('a', 'c')

    todomvc.cancel_editing('c', 'c to be canceled')

    todomvc.delete('c') \
        .should_have('a')
