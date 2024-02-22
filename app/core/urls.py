from django.urls import path, include
from core import views

app_name = "core"

urlpatterns = [
    path("", views.dashboard, name="Dashboard"),
    path("download/", views.download, name="download"),
    path(
        "download_file/<str:taskid>",
        views.DownloadFileViews.as_view(),
        name="file_download",
    ),
]
