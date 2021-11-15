from django.urls import path
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	#path('about/',views.about,name='about'),
	#path('search/',views.search_api_page,name='search_api_page')
]