from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.one, name='one'),
    # path('persons/', views.persons, name='persons'),
    # path('persons/<int:person_id>/', views.get_person, name='get_person'),
    # path('create_person/', views.create_person, name="create_person"),
    # path('delete_person/<int:person_id>/', views.delete_person, name='delete_person'),

]
