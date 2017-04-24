from django.conf.urls import url

from booking import views


urlpatterns = [
    url(r'double/', views.double_book)
]
