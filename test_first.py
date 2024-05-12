from main import add

def test_add_normal():
    assert add(1, 2) == 3

def test_add_str():
    assert add("A", "B") == "AB"