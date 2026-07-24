install:
	pip install -e .

test:
	pytest

lint:
	ruff check .

format:
	black .

run:
	python src/main.py