from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help= 'the base comane'
    def add_arguments(self, parser) -> None:
        parser.add_argument("--number", help="how many times")
        
    def handle(self, *args, **options):
        print(*args, **options)
        print('hi there')
        return super().handle(*args, **options)
  