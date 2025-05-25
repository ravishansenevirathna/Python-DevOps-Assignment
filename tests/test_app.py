import pytest
from app import create_app

@pytest.mark.print_hello
def test_hello():
    """Simple test that just prints hello"""
    print("\n=== HELLO FROM TESTS ===")
    assert True