from r_p_s import check_input

def test_check_input():
    assert check_input("Rock") == "Rock"
    assert check_input("Paper") == "Paper"
    assert check_input("Scissors") == "Scissors"
