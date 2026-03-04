from django.urls import path
from .views import (
    member_list,
    member_create,
    member_detail,
    update_member,
    member_delete
)

urlpatterns = [
    path('members/', member_list),
    path('members/create/', member_create),
    path('members/<int:pk>/', member_detail),
    path('members/<int:pk>/update/', update_member),
    path('members/<int:pk>/delete/', member_delete),
]
