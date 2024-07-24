"""
URL configuration for DjangoLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from django.conf import settings
from core.views import IndexView, GameCreateView, GameDeleteView, GameView, GameEditView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('game-delete/<int:pk>/', GameDeleteView.as_view(), name='game-delete'),
    path('game-create/', GameCreateView.as_view(), name="game-create"),
    path('game-info/<int:pk>/', GameView.as_view(), name="game-info"),
    path('game-edit/<int:pk>/', GameEditView.as_view(), name="game-edit"),
    path("__debug__/", include("debug_toolbar.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
