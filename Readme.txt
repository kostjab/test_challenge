Tests for REST API.

Files:
test.py - contain all test cases
endpoints.py - contain information about endpoint
src - contain source code for tests

Test cases:
1. Case name: test_create_get_change_user
Create user (POST) -> Get user (GET) -> Change username (PATCH)
-> Get user (GET)

2. Case name: test_create_user_with_same_data
Create user (POST) -> Create user with same username (POST)
-> Create user with same email (POST) -> Create user with same email and username (POST)

3. Case name: test_create_user_with_different_password_length
Create user with 32 chars password (POST) -> Create user with with 65 chars password (POST)
-> Create user with with 3 chars password (POST)

4. Case name: test_create_user_with_wrong_content_type
Create user with bad "Content-Type" header value (POST)

Requarments:
Python 3.6
PyTest
Module "requests"

Start:test
To start test suite, just execute "pytest test.py"