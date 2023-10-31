
install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main test_*.py

format:	
	black *.py
	nbqa black *.ipynb 

lint:
	nbqa ruff *.ipynb
	ruff check *.py
		
all: install lint test format
