import pytest 

@pytest.mark.skip
def test_markskip():
	print("marking test as skip")
	assert 1==2