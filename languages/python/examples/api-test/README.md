# API Test

End-to-end (HTTP-to-database) REST API testing example

## Dependencies

```
python --version # should be 3.6
```

```
pip install virtualenv
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

Libraries:

```
requests
pytest
kazoo
```

Environment variables:

```
BACKEND_SECRET
```

## How to run tests

Running all tests:

```
bin/test
```

Running a single test file:

```
bin/test test/ads/test_public.py
```

Running a single test function:

```
bin/test test/ads/test_public.py -k "test_no_default"
```

Running two test functions:

```
bin/test test/ads/test_public.py -k "test_setup or test_no_default"
```

Running a test with debug printouts of the full HTTP response bodies:

```
LOG_RESPONSE=1 bin/test test/superscription/test_api.py
```

Running test against a development service/API running locally:

```
ADS_URL=http://localhost:8080 ADS_INTERNAL_URL=http://localhost:8081 bin/test test/ads/test_internal.py test/ads/test_public.py
```

## Test Framework

We use the [pytest](https://docs.pytest.org/en/latest) framework. You can install it with `conda install pytest` or `pip install pytest`.

## Resources

* [pytest docs](https://docs.pytest.org/en/latest/contents.html#toc)
