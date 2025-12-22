from guess import guess_player, choose_number, check_input


def test_guess_player():
    assert guess_player(10, 10) == "correct"
    assert guess_player(100, 50) == "low"
    assert guess_player(57, 100) == "high"

    assert guess_player(10, 5) == "low"
    assert guess_player(10, 15) == "high"
    assert guess_player(57, 57) == "correct"


def test_choose_number():
    assert choose_number(10) == False
    assert choose_number(0) == False


def test_check_input():
    assert check_input("5") == 5
    assert check_input("10") == 10
    assert check_input("0") == 0
    assert check_input("1") == 1
    assert check_input("99999") == 99999
