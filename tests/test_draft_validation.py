from todomvc_testing.model import app


def test_basic_management():
    app.visit()

    app.add('a', 'b', 'c')
    app.should_have('a', 'b', 'c')

    app.edit('b', 'b edited')

    app.toggle('b edited')

    app.clear_completed()
    app.should_have('a', 'c')

    app.cancel_editing('c', 'c to be canceled')

    app.delete('c')
    app.should_have('a')
