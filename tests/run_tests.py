#!/usr/bin/env python3
"""
Test runner
"""
import pytest
import sys

if __name__ == "__main__":
    # Run tests with verbose output
    result = pytest.main(["-v", "tests/"])
    sys.exit(result)
