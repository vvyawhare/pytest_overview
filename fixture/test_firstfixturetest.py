#test about function based fixture , why do we need scope based fixtures

import pytest
import json
import logging

@pytest.fixture()
def read_config():
    with open("app.json") as f:
        config = json.load(f)
        logging.info("Read config")
    return config

def test1(read_config):
    logging.info("Test function 1")
    assert read_config == {"test":"fixture test"}

def test2(read_config):
    logging.info("Test function 2")
    assert read_config == {"test":"fixture test"}
