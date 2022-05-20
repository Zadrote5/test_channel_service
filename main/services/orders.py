from datetime import date, datetime

import gspread
import requests
from bs4 import BeautifulSoup
from channelService.settings import env
from main.models import Order


class Sheet:
    def __init__(self):
        gc = gspread.service_account(filename='key.json')
        self.sheet = gc.open_by_url(env('SHEET')).get_worksheet(0).get_all_values()

    # Метод получения текущего курса доллара
    @staticmethod
    def _get_curs():
        today = date.today()
        request = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={today.strftime("%d/%m/%Y")}')
        soup = BeautifulSoup(request.text, 'html.parser')
        curs = soup.find('valute', id='R01235').find('value').get_text()
        return float(curs.replace(',', '.'))

    # Метод получения значений таблицы
    def get_body(self):
        self.sheet.pop(0)
        curs = self._get_curs()
        for row in self.sheet:
            row.append(round((int(row[2]) * curs), 2))
        return self.sheet

    # Метод созранения данных в базу
    def save_orders(self):
        orders_sheet_ids = []
        for order in self.get_body():
            orders_sheet_ids.append(order[1])

            order_model = Order.objects.filter(sheet_id=order[1]).first()
            if order_model is not None:
                order_model.price_dollars = order[2]
                order_model.delivery_date = datetime.strptime(order[3], "%d.%m.%Y")
                order_model.price_rub = order[4]
                order_model.save()
            else:
                Order.objects.create(sheet_id=order[1],
                                     price_dollars=int(order[2]),
                                     delivery_date=datetime.strptime(order[3], "%d.%m.%Y"),
                                     price_rub=float(order[4]))

        deleted_orders = Order.objects.exclude(sheet_id__in=orders_sheet_ids)
        for order in deleted_orders:
            order.delete()