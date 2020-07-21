from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls import re_path
from django.views.static import serve


from beautybox.views import beautyboxes_list, recipients_list, beautybox_detail, recipient_detail
urlpatterns = [
    path('product-sets/', beautyboxes_list, name='beutyboxes_list'),
    path('product-sets/<int:id>/', beautybox_detail, name='beautybox_detail'),

    path('recipients/', recipients_list, name='recipients_list'),
    path('recipients/<int:id>/', recipient_detail, name='recipient_detail'),
]