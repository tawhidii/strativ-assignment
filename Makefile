migrate:
	docker compose exec web python manage.py migrate
collectstatic:
	docker compose exec web python manage.py collectstatic --noinput
createsuperuser:
	docker compose exec web python manage.py createsuperuser
seed:
	docker compose exec web python manage.py seed_data district.json

.PHONY: migrate collectstatic createsuperuser seed