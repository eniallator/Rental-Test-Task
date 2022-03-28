from django.views.generic.list import ListView

from .models import Reservation


class ReservationListView(ListView):
    model = Reservation
    paginate_by = 20
    template_name = "rental/reservations.html"

    def get_queryset(self):
        return super().get_queryset().order_by("id")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
