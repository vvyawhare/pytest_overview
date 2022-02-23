import pytest

@pytest.mark.xfail
def test_xfailtest():
	print("this test is xfail test")
	assert 1==1