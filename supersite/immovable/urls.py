from django.urls import path
from immovable.views import *
urlpatterns = [
    path('',menu),
    path('auth/',hello),
    path('clients/',clients),
    path('emp/',emp),
    path('reg/',regus),
    path('auth/adminka/',adminka),
    path('auth/actusers/',users),
    path('contr/',contr),
    path('reg/fin/',finished),
    path('registpg/',reg),
    path('registpg/user/',uscrud),
    path('app/',app),
    path('app/subdata/',sub),
    path('auth/actusers/contracts/',createcon),
    path('auth/actusers/contracts/subcon/',subcon),
    path('h/<int:id>/',h),
]
