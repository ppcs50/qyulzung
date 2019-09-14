from django.urls import include, path
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    path("contact", views.contact, name="contact"),
    path("about", views.about, name="about"),
    path("<user>/step1", views.step1, name="step1"),
    path("<user>/step2", views.step2, name="step2"),
    path("<user>/step3", views.step3, name="step3"),
    path("<user>/step4", views.step4, name="step4"),
    path("<user>/result", views.result, name="result"),
    path("<user>/result/comment", views.comment, name="comment"),
    path("<user>/journal", views.journal, name="journal"),
    path("delete/<int:arg1>", views.delete, name="delete"),
    path("<arg1>/journal/<int:arg2>", views.journals, name="journals"),
    path("<arg1>/journal/<int:arg2>/post", views.post, name="post"),
    path("<arg1>/journal/<int:arg2>/unpost", views.unpost, name="unpost"),
    path("board/", views.board, name="board"),
]