test:
	pytest --disable-pytest-warnings --ds=tests.settings --cov=drf_impersonate tests/ --cov-report=xml

install-deps:
	pip install -r requirements_test.txt
