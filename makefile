build:
	docker build --force-rm $(options) -t new-website-tutorial:latest .
build-prod:
	$(make) build options='--target roduction'

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)

compose-manage-py:
	docker-compose run --rm $(options) website python3 manage.py $(cmd)