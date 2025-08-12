# Authored by Daniel Bothwell


This is a simple Pytest testing suite that attempts to robustly test the API for 'https://randomuser.me/api'.

## What is included

There are many files included to run the tests. The easiest way to run the test is to run the included pytest_runner.bash
The tests live under black_box_test and performance_tests incase the user wants to invoke the tests from the CLI manually. 
Everything needed to run the tests, including test data are included in the project. 

## Installation

pip install -r requirements.txt

## Execution

From working dir:

./pytest_runner.bash
