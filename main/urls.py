from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from form import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
    path("results/", views.results, name="results"),
    path("plot/", views.plot_matplotlib_graph, name="plot"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
