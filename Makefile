run:
	uvicorn main:app --reload

install:
	pip install --no-cache-dir -r requirements.txt
