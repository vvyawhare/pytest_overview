import pytest 

@pytest.mark.parametrize("first,second",[(1,2),(3,4)])
def test_parameter(first,second):
	print(first)
	print(second)
