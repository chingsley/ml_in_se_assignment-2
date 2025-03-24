STRENGTH:

- It covers a good number of the test cases
- It correctly tests internal server error by mocking database failures
- It handles test isolation better by clearing all mocks at the end of the test suit
- Sets up jsonwebtoken clearly for the test

WEAKNESS:

- Failed to setup test database seed (Failed to pickup the context from the package.json)
- It doesn't configure the environment varialbe for the test cases correlcty
- Without using enough context from the package.json, the texts are pretty generic.
- Also fails to test for invalid question id's, like providing a number instead of string
