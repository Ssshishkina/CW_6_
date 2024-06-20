from django.urls import path
from newsletter.apps import NewsletterConfig
from newsletter.views import (IndexView, ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView,
                              MessageListView, MessageCreateView, MessageUpdateView, MessageDeleteView,
                              NewsletterListView, NewsletterDetailView, NewsletterCreateView, NewsletterUpdateView,
                              NewsletterDeleteView, contacts)
from users.views import toogle_activity

app_name = NewsletterConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),

    path('client/', ClientListView.as_view(), name='client_list'),
    path('client/create/', ClientCreateView.as_view(), name='create_client'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),

    path('message/', MessageListView.as_view(), name='message_list'),
    path('message/create/', MessageCreateView.as_view(), name='create_message'),
    path('message/update/<int:pk>/', MessageUpdateView.as_view(), name='update_message'),
    path('message/delete/<int:pk>/', MessageDeleteView.as_view(), name='delete_message'),

    path('mail/', NewsletterListView.as_view(), name='newsletter_list'),
    path('mail/view/<int:pk>/', NewsletterDetailView.as_view(), name='view_mail'),
    path('mail/create/', NewsletterCreateView.as_view(), name='create_mail'),
    path('mail/update/<int:pk>/', NewsletterUpdateView.as_view(), name='update_mail'),
    path('mail/delete/<int:pk>/', NewsletterDeleteView.as_view(), name='delete_mail'),
    path('mail/activity/<int:pk>/', toogle_activity, name='toogle_activity'),
]
