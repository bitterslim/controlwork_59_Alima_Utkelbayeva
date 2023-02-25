from django.urls import path

from .views.index import index_view
from .views.guest import add_guest, update_view, delete_view

urlpatterns = [
    path('', index_view, name='index'),
    path('guests', index_view, name='index'),
    path('guest/add', add_guest, name='guest_add'),
    path('guest/<int:pk>/update', update_view, name='guest_update'),
    path('guest/<int:pk>/delete', delete_view, name='guest_delete')

]
