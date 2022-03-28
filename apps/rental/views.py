from django.db.models import Subquery, OuterRef
from django.views.generic.list import ListView

from .models import Reservation


class ReservationListView(ListView):
    model = Reservation
    paginate_by = 20
    template_name = "rental/reservations.html"

    def get_queryset(self):
        previous_reservations = (
            Reservation.objects.filter(
                rental=OuterRef("rental"), checkin__lt=OuterRef("checkin")
            )
            .order_by("-checkin")
            .values("id")[:1]
        )
        return (
            super()
            .get_queryset()
            .order_by("id")
            .prefetch_related("rental")
            .annotate(previous_reservation=Subquery(previous_reservations))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
