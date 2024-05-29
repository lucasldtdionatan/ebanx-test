run-project:
	uvicorn src.main:app --reload

run-test:
	pytest --cov=src tests/ --cov-report term-missing