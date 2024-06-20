from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from blog.models import Blog
from newsletter.forms import NewsletterForm, ClientForm, MessageForm
from newsletter.models import Newsletter, Client, Message, Log


class NewsletterListView(LoginRequiredMixin, ListView):
    '''Класс всех рассылок.'''
    model = Newsletter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class NewsletterDetailView(DetailView):
    '''Класс просмотра рассылки.'''
    model = Newsletter


class NewsletterCreateView(LoginRequiredMixin, CreateView):
    '''Класс создания новой рассылки.'''
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    '''Класс редактирования рассылки.'''
    model = Newsletter
    form_class = NewsletterForm
    success_url = reverse_lazy('newsletter:newsletter_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner or self.request.user.is_superuser:
            return NewsletterForm
        else:
            return self.get_form_class()


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    '''Класс удаления рассылки.'''
    model = Newsletter
    success_url = reverse_lazy('newsletter:newsletter_list')


class ClientListView(ListView):
    '''Класс всех клиентов сервиса.'''
    model = Client


class ClientCreateView(LoginRequiredMixin, CreateView):
    '''Класс создания нового клиента сервиса.'''
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client_list')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    '''Класс редактирования клиента сервиса.'''
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('newsletter:client_list')


class ClientDeleteView(DeleteView):
    '''Класс удаления клиента сервиса.'''
    model = Client
    success_url = reverse_lazy('newsletter:client_list')


class MessageListView(ListView):
    '''Класс всех сообщений рассылок.'''
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    '''Класс создания нового сообщения рассылки.'''
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:message_list')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    '''Класс редактирования сообщения рассылки.'''
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('newsletter:message_list')


class MessageDeleteView(DeleteView):
    '''Класс удаления сообщения рассылки.'''
    model = Message
    success_url = reverse_lazy('newsletter:message_list')


class IndexView(TemplateView):
    template_name = 'newsletter/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_list'] = Blog.objects.all()[:3]
        context['object_list'] = Newsletter.objects.all()

        unique_clients_count = Client.objects.all().values('email').distinct().count()
        context['unique_clients_count'] = unique_clients_count

        active_newsletter_count = Newsletter.objects.filter(is_active=True).count()
        context['active_newsletter_count'] = active_newsletter_count
        return context


def contacts(request):
    context = {
        'title': 'Контакты',
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} ({phone}, {email}): {message}")

    return render(request, 'newsletter/contacts.html', context)


class LogListView(ListView):
    model = Log
    success_url = reverse_lazy('newsletter:newsletter_list')
