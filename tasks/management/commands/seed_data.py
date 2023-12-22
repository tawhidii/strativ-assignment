import json
from django.core.management.base import BaseCommand
from tasks.models import District


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("json_file", type=str)

    def handle(self, *args, **options):
        with open(options["json_file"]) as f:
            data_list = json.load(f)
            districts = []
            for d in data_list["districts"]:
                districts.append(
                    District(
                        name=d["name"],
                        bn_name=d["bn_name"],
                        lat=float(d["lat"]),
                        lon=float(d["long"]),
                    )
                )
            District.objects.bulk_create(districts)
