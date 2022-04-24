from django.core.paginator import Paginator

from payments.models import Appointment


def index(request):
    items = Appointment.objects.all()

    p = Paginator(items, 20)

    # Return item starting at the 2nd page, you get page number from query string
    page = p.page(2)

    #Make the context object
    context = {'item': page}