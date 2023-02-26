import unittest
import coverage
import pytest

def test_case_one():
    actual_x, result_x = 1, 1
    assert actual_x == result_x, "Should be 1"

def test_case_two():
    actual_y, result_y = 2, 2
    assert actual_y == result_y, "Should be 2"

def test_case_three():
    actual_z, result_z = 3, 3
    assert actual_z == result_z, "Should be 3"

def test_case_four():
    actual_f, result_f = 4, 4
    assert actual_f == result_f, "Should be 4"     
