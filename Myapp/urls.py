from django.urls import path

from . views import CreateView,ListView, FoodDeleteView, ClassroomCreateView, SchoolDetailView, ClassroomDetailView, Classroom_FoodDetailView, graphic, FoodDetail,graphicFood, foodForSchool,graphicFood_for_School

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
    path("food_detail/<uuid:uuid>/", FoodDetail.as_view(), name = "food_detail"),
    path("graphic_food/<str:uuid>/", graphicFood, name="graphic_food"),
    path("food_for_school/<str:uuid_school>/<str:uuid_food>/", foodForSchool, name="food_for_school"),
    path("graphicfood_for_school/<str:uuid_school>/<str:uuid_food>/",graphicFood_for_School, name="graphicfood_for_school"),
]