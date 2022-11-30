# jive-api-client


Authorization flow guide:

[Authorization Code Grant](https://developer.goto.com/Authentication/#section/Authorization-Flows/Authorization-Code-Grant)


## Postman Collection

There is a Postman Collection that can be used to validate setup and test changes. Import the following: (Peerlogic API
Collection)[https://www.getpostman.com/collections/c1045d02c72c56abd559]

## Running Test Cases

In pyproject.toml under `tool.pytest.ini_options` you will find `addopts = "-vv -x --lf --cov"`
These are pytest commands that we want to execute when running pytest.

1. `-x`: Will stop running tests once one fails
2. `-vv`: Will display more detail about the failed assertion
3. `--lf`: Runs from the last failed test when running pytest
4. `--cov`: outputs a percentage of covered tests.

We are using the pytest framework for unit and integration tets. In the root of your directory run:

```bash
pytest
```

Running `pytest` in the root of your directory will run the test cases written in `tests/test_api/tests.py` or any other file that starts with "test".