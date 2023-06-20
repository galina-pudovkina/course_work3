from utils import load_operations, select_data, sort_data, create_operations



def test_load_operations():
    data = load_operations('operations.json')
    assert isinstance(data, list)


def test_select_data(test_data):
    data = select_data(test_data)
    assert len(data) == 5


def test_sort_data(test_data):
    assert sort_data(test_data)[2]['id'] == 142264268


def test_create_operations(test_data):
    data = create_operations(test_data)
    assert data[0] == ('\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб. \n')
