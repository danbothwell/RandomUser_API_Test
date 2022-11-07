#!/bin/sh

pytest -v --disable-warnings ./performance_tests/api_performance_test.py
pytest -v --disable-warnings ./black_box_tests/api_functionality_test.py