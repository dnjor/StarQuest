from question_answer import check_input, check_ready, checking_answers_multiple_choice


def test_check_input():
    assert check_input("hello") == "hello"
    assert check_input("hello world") == "hello world"


def test_check_ready():
    assert check_ready("ready") == "ready"
    assert check_ready("ReAdy") == "ready"


def test_checking_answers_multiple_choice():
    data_question = {
        "question": "What is the capital of France?",
        "correct_answer": "Paris",
        "incorrect_answers": ["London", "Berlin", "Madrid"]}
    assert checking_answers_multiple_choice(data_question) == ("paris", ["London", "Berlin", "Madrid", "paris"])
