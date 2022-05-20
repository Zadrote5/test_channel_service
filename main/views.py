from django.http import HttpResponse
from django.template import loader
from main.models import Order
from main.services.orders import Sheet


# Обработка страницы
def index(request):
    template = loader.get_template('main/index.html')
    sheet = Sheet()
    sheet.save_orders()
    context = {
        'orders': Order.objects.all()
    }
    return HttpResponse(template.render(context, request))
