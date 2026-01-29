from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, FormView, ListView,
                                  TemplateView, UpdateView)

from .forms import AirportRouteForm, SearchLastReachableNodeForm
from .models import AirportRoute


class HomeView(TemplateView):
    template_name = "airports/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "total_airports": AirportRoute.objects.count(),
                "longest_duration_airport": AirportRoute.get_airport_with_longest_duration(),
                "shortest_duration_airport": AirportRoute.get_airport_with_shortest_duration(),
                "recent_airports": AirportRoute.objects.order_by("-created_at")[:5],
            }
        )
        return context


class AirportCreateView(CreateView):
    model = AirportRoute
    form_class = AirportRouteForm
    template_name = "airports/add_airport.html"
    success_url = reverse_lazy("airport_list")

    def form_valid(self, form):
        airport = form.save()
        messages.success(
            self.request, f"Airport route {airport.airport_code} added successfully!"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add Airport Route"
        return context


class AirportListView(ListView):
    model = AirportRoute
    template_name = "airports/airport_list.html"
    context_object_name = "airports"
    ordering = ["airport_code"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Airport Routes List"
        return context


class AirportUpdateView(UpdateView):
    model = AirportRoute
    form_class = AirportRouteForm
    template_name = "airports/edit_airport.html"
    success_url = reverse_lazy("airport_list")

    def form_valid(self, form):
        airport = form.save()
        messages.success(
            self.request, f"Airport route {airport.airport_code} updated successfully!"
        )
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Edit Airport Route: {self.object.airport_code}"
        return context


class AirportDeleteView(DeleteView):
    model = AirportRoute
    template_name = "airports/delete_airport.html"
    success_url = reverse_lazy("airport_list")
    context_object_name = "airport"

    def delete(self, request, *args, **kwargs):
        airport = self.get_object()
        airport_code = airport.airport_code
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f"Airport route {airport_code} deleted successfully!")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Delete Airport Route: {self.object.airport_code}"
        return context


class SearchLastReachableNodeView(FormView):
    template_name = "airports/search_last_reachable.html"
    form_class = SearchLastReachableNodeForm

    def form_valid(self, form):
        airport = form.cleaned_data["airport"]
        direction = form.cleaned_data["direction"]
        last_reachable = airport.get_last_reachable_node(direction)
        messages.success(
            self.request,
            f"Successfully found the last reachable node starting from "
            f"{airport.airport_code} going {direction}!",
        )
        context = self.get_context_data(
            form=form,
            last_reachable=last_reachable,
            starting_airport=airport,
            direction_taken=direction.capitalize(),
            title="Find Last Reachable Node",
        )
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        kwargs.setdefault("title", "Find Last Reachable Node")
        return super().get_context_data(**kwargs)


class LongestDurationAirportView(TemplateView):
    template_name = "airports/longest_duration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "airport": AirportRoute.get_airport_with_longest_duration(),
                "title": "Airport with Longest Duration",
            }
        )
        return context


class ShortestDurationAirportView(TemplateView):
    template_name = "airports/shortest_duration.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "airport": AirportRoute.get_airport_with_shortest_duration(),
                "title": "Airport with Shortest Duration",
            }
        )
        return context
