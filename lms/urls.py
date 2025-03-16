from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path("courses/", views.show_courses, name="courses"),
    path("account/", views.show_account, name="account"),
    path("cart/", views.cart, name="cart"),
    path("instructor/<int:id>/", views.get_instructor, name="instructor"),
    path("register", views.register_view, name="register"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
