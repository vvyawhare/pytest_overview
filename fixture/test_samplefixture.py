import pytest

@pytest.fixture()
def samplefixure():
	print("sample fixture")

def test_samplefixture(samplefixure):
	print("testing sample fixure")

def test_samplefixture1(samplefixure):
	print("testing sample fixure1")