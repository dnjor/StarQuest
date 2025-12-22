from x_o import check_number, check_win


def test_check_number():
    assert check_number("o", "5") == True
    assert check_number("x", "7") == True

    assert check_number("x", "5") == False
    assert check_number("o", "5") == False

    assert check_number("x", "10") == False
    assert check_number("o", "0") == False
    assert check_number("x", "-1") == False


def test_check_win_o_wins():
    global check_win_o, check_win_x
    check_win_o = ["1", "5", "9"]
    check_win_x = ["2", "3", "4"]
    assert check_win(check_win_o, check_win_x) == True


def test_check_win_x_wins():
    global check_win_o, check_win_x
    check_win_o = ["1", "8", "9", "4"]  
    check_win_x = ["2", "3", "5", "7"]
    assert check_win(check_win_o, check_win_x) == True
