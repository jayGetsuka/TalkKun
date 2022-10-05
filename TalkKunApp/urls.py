
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.Login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.Logout, name="logout"),
    path('detail/<int:id>', views.detail),
    path('addQ/', views.addQ, name="addQ"),
    path('QuestionMe/', views.QuestionMe, name="Qme"),
    path('answer/', views.answer, name="ans"),
    path('QuestionMe/detailForme/<int:id>', views.detailForme),
    path('editQ', views.editQ, name="editQ"),
    path('QuestionMe/deleteQ/<int:id>', views.deleteQ, name="deleteQ"),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)