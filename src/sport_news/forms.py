from django import forms
from sport_news.models import City, Sport_type
class FindForm_city(forms.Form):
    city = forms.ModelChoiceField(
        queryset=City.objects.all(), to_field_name='slug',
        required=False, label='Город', empty_label='Город не выбран',
        widget=forms.Select(attrs={'class': 'form-control'}))
class FindForm_st(forms.Form):
    sport_type = forms.ModelChoiceField(
        queryset=Sport_type.objects.all(), to_field_name='slug',
        required=False, label='Вид спорта', empty_label='Виды спорта',
        widget=forms.Select(attrs={'class': 'form-control'}))