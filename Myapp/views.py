from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
import matplotlib.pyplot as plt
from django.http import FileResponse

#My imports
from . models import Classroom_Food, Food, Classroom,School 
from . forms import Classroom_Food_Form, ClassroomForm
# Create your views here.


class CreateView(CreateView):

    model = Classroom_Food
    form_class = Classroom_Food_Form
    template_name = 'Myapp/create.html'
    success_url = reverse_lazy("Myapp:create")

    def form_valid(self, form):
        messages.success(self.request, "The task was created successfully.")
        return super(CreateView,self).form_valid(form)


class FoodDeleteView(LoginRequiredMixin, DeleteView):
    model = Food
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'food'
    success_url = reverse_lazy('Myapp:list')

    def form_valid(self, form):
        messages.success(self.request, "The task was food successfully.")
        return super(FoodDeleteView,self).form_valid(form)



class ListView(LoginRequiredMixin, ListView):
    model = Food
    context_object_name = 'food_list'
    def get_queryset(self):
        queryset = super().get_queryset().all().order_by("name")
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form_filter"] = self.filterset.form
    #     return context

class ClassroomCreateView(LoginRequiredMixin, CreateView):

    model = Classroom
    form_class = ClassroomForm
    template_name = 'Myapp/classroom_create.html'
    success_url = reverse_lazy("Myapp:classroom_create")

    def form_valid(self, form):
        messages.success(self.request, "The task was created successfully.")
        return super(ClassroomCreateView,self).form_valid(form)

class SchoolDetailView(LoginRequiredMixin, DetailView):

    model = School
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'school'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        school = School.objects.get(uuid = self.kwargs.get("uuid"))
        context['classroom'] = Classroom.objects.filter(school = school).order_by('name')
        return context

class ClassroomDetailView(LoginRequiredMixin, DetailView):

    model = Classroom
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'classroom'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        classroom = Classroom.objects.get(uuid = self.kwargs.get("uuid"))
        classroom_food = Classroom_Food.objects.filter(classroom = classroom)
        context['classroom_food'] = classroom_food
        return context
    
class Classroom_FoodDetailView(LoginRequiredMixin, DetailView):

    model = Classroom_Food
    slug_url_kwarg = 'id'
    slug_field = 'id'
    context_object_name = 'classroom_food'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get("pk")
        context['id'] = id
        return context


@login_required
def graphic(request, id):

    labels = ["like", "dislike"]
    classroom_food = Classroom_Food.objects.get(id = id)
    liked = classroom_food.liked
    dislike = classroom_food.disliked
    values = [liked, dislike]
    fig, ax = plt.subplots()
    ax.pie(values,labels=labels,autopct='%1.1f%%', shadow=True,startangle=90)
    ax.axis('equal')
    plt.savefig("bargraph.png")
    return FileResponse(open("bargraph.png", "rb"), content_type="image/png")



