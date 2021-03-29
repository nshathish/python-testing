install:
	pip install --upgrade pip && pip install -r requirements.txt

test:
	python3 -m pytest -vv --cov=hello test/test_hello.py

lint:
	pylint --disable=R,C main/hello.py

all: install lint test
