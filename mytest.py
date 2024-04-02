
def test_func(func_name):
    func = func_name
    tests = [
        ([], None),
        ([1], None),
        ([100, 3], None),
        ([3, 1, 6, 5, 2, 4], 4),
        ([38, 42, 33, 71, 3, 21, 77, 99, 59, 63], 71),
        ([22, 100, 12, 41, 85, 79, 92, 79, 92, 89, 72, 34, 89, 44, 10], 89),
        ([-5, -47, -38, -34, 34], -34),
    ]

    for (test_input, correct_answer) in tests:
        result = func(test_input)
        assert result == correct_answer, f"result ({result}) not equal correct ({correct_answer})"

