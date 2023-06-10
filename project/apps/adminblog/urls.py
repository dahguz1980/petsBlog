from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("pages/list/", login_required(views.PagesList.as_view()), name="pages"),
    path("pages/create/", login_required(views.PageCreate.as_view()), name="page_create"),
    path("pages/preview/<int:pk>", login_required(views.PageDetail.as_view()), name="page_preview"),
    path("pages/update/<int:pk>", login_required(views.PageUpdate.as_view()), name="page_update"),
    path("pages/delete/<int:pk>", login_required(views.PageDelete.as_view()), name="page_delete"),
    path("pages/publish/<int:page_id>/<str:new_status>", login_required(views.PagePublish.as_view()), name="page_publish"),
]
