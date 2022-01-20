db-migrate:
	alembic init alembic
	docker-compose run app alembic revision --autogenerate -m "Latest Migration"
	docker-compose run app alembic upgrade head

infra-build:
	docker-compose build

infra-up:
	docker-compose up

infra-down:
	docker-compose down

docker-logs:
	docker-compose logs -f

deps:
	python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --upgrade pip
	python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org --editable .
	python3 -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt

dev-env:
	python3 -m venv venv
	source venv/bin/activate

.PHONY: deps