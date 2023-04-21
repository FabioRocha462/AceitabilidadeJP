from django.urls import path

from . views import CreateView,ListView, FoodDeleteView, ClassroomCreateView, SchoolDetailView, ClassroomDetailView, Classroom_FoodDetailView, graphic

app_name = "Myapp"

urlpatterns = [
    path("create/", CreateView.as_view(), name="create"),
    path("delete/<uuid:uuid>/", FoodDeleteView.as_view(), name="delete"),
    path("list/", ListView.as_view(), name = "list"),
    path("classroom_create/", ClassroomCreateView.as_view(), name = "classroom_create"),
    path("school_detail/<uuid:uuid>/", SchoolDetailView.as_view(), name = "school_detail"),
    path("classroom_detail/<uuid:uuid>/", ClassroomDetailView.as_view(),name = "classroom_detail"),
    path("classroom_food_detail/<int:pk>/", Classroom_FoodDetailView.as_view(), name = "classroom_food_detail"),
    path("graphic/<int:id>/",graphic, name = "graphic"),
]