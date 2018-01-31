

def test_fake():
	assert {x for x in range(7)} == {0, 1, 2, 3, 4, 5, 6}

def test_nothing():
	assert 1 == 1
