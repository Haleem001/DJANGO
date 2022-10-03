from django.urls import path


from . import views



urlpatterns = [
    path('people/', views.person_list),
    path('person/<int:pk>', views.person_detail),

]

