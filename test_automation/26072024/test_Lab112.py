# Fixture-concept of python
# use fixtures to do multiple tasks.similar to pre and post condition.

import pytest
@pytest.fixture()
def is_married():
    return True
def test_i_need_confirm(is_married):
    assert is_married == True
    print("You are married")

