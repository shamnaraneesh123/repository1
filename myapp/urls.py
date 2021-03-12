
from django.urls import path,include
from . import views

urlpatterns = [
   path('user1',views.testfun,name='user1'),
   path('test2',views.test2fun,name='test2'),
   path('test3',views.test3fun,name='test3'),
   path('test4',views.test4fun,name='test4')
]
