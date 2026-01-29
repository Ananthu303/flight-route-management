from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("airports/", views.AirportListView.as_view(), name="airport_list"),
    path("airports/add/", views.AirportCreateView.as_view(), name="add_airport"),
    path("airports/edit/<int:pk>/", views.AirportUpdateView.as_view(), name="edit_airport"),
    path("airports/delete/<int:pk>/", views.AirportDeleteView.as_view(), name="delete_airport"),

    path("search/last-reachable/", views.SearchLastReachableNodeView.as_view(), name="search_last_reachable"),
    path("airports/longest-duration/", views.LongestDurationAirportView.as_view(), name="longest_duration"),
    path("airports/shortest-duration/", views.ShortestDurationAirportView.as_view(), name="shortest_duration"),
]
