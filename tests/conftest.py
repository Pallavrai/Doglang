"""Pytest configuration and fixtures"""
import sys
import os
from io import StringIO
from contextlib import contextmanager


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from doglang.main import Interpreter


@pytest.fixture
def capture_output():
    """Fixture to capture stdout from DogLang code execution"""
    @contextmanager
    def _capture():
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            yield sys.stdout
        finally:
            sys.stdout = old_stdout
    
    def _run_and_capture(code):
        with _capture() as output:
            Interpreter(code)
            return output.getvalue().strip()
    
    return _run_and_capture


@pytest.fixture
def run_code(capture_output):
    """Fixture that returns a function to run code and capture output"""
    return capture_output


@pytest.fixture
def expect_error():
    """Fixture to test that code raises expected errors"""
    def _expect_error(code, error_message=None):
        if error_message:
            return pytest.raises(Exception, match=error_message)
        return pytest.raises(Exception)
    return _expect_error



def pytest_configure(config):
   
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "bug: marks tests for specific bug fixes"
    )
    config.addinivalue_line(
        "markers", "symbol_table: marks tests related to symbol table isolation"
    )