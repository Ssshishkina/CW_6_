from django import forms
from django.forms import DateTimeInput
from newsletter.models import Client, Newsletter, Message


class StyleFormMixin:
    '''Класс стилизации формы.'''
    def __init__(self, *args, **kwargs):
        '''Функция стилизации формы'''
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, forms.ModelForm):
    '''Форма заполнения при создании/редактировании Клиента сервиса.'''
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('owner',)


class NewsletterForm(StyleFormMixin, forms.ModelForm):
    '''Форма заполнения при создании/редактировании Рассылки.'''
    class Meta:
        model = Newsletter
        fields = '__all__'
        exclude = ('date_next', 'owner')

        widgets = {
            'start_date': DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС', 'type': 'datetime-local'}),
            'end_date': DateTimeInput(attrs={'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС', 'type': 'datetime-local'}),
        }


class MessageForm(StyleFormMixin, forms.ModelForm):
    '''Форма заполнения при создании/редактировании
    Сообщения для рассылки.'''
    class Meta:
        model = Message
        fields = '__all__'
