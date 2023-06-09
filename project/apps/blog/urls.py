from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("pages/list/", login_required(views.PagesList.as_view()), name="pages"),
    path("pages/create/", login_required(views.PageCreate.as_view()), name="page_create"),
]
