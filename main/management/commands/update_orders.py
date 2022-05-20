from django.core.management import BaseCommand
from main.services.orders import Sheet


class Command(BaseCommand):
    def handle(self, *args, **options):
        sheet = Sheet()
        sheet.save_orders()
        print('Заказы успешно обновлены')
