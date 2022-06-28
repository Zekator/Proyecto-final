from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.shortcuts import render


from country.models import Country
from country.forms import CountryForm


# Create your views here.


def country_list(request):
    countries = Country.objects.all()

    context_dict = {
        'countries': countries
    }

    return render(
        request=request,
        context=context_dict,
        template_name="country/country_list.html"
    )

@login_required
def country_form(request):
    if request.method == 'POST':
        country_form = CountryForm(request.POST)
        if country_form.is_valid():
            data = country_form.cleaned_data
            countries.save()

            countries = Country.objects.all()
            context_dict = {
                'countries': countries
            }
            return render(
                request=request,
                context=context_dict,
                template_name="country/country_list.html"
            )

    country_form = CountryForm(request.POST)
    context_dict = {
        'country_form': country_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='country/country_form.html'
    )


@login_required
def update_country(request, pk: int):
    country = Country.objects.get(pk=pk)

    if request.method == 'POST':
        country_form = CountryForm(request.POST)
        if country_form.is_valid():
            data = country_form.cleaned_data
            country.country_name = data['country_name']
            country.save()

            countries = Country.objects.all()
            context_dict = {
                'countries': countries
            }
            return render(
                request=request,
                context=context_dict,
                template_name="country/country_list.html"
            )

        country_form = CountryForm(model_to_dict(country))
        context_dict = {
            'countries': countries,
            'country_form': country_form,
        }
        return render(
            request=request,
            context=context_dict,
            template_name='country/country_form.html'
        )


@login_required
def delete_country(request, pk: int):
    country = Country.objects.get(pk=pk)
    if request.method == 'POST':
        country.delete()

        country = Country.objects.all()
        context_dict = {
            'countries': countries
        }
        return render(
            request=request,
            context=context_dict,
            template_name="country/country_list.html"
        )

    context_dict = {
        'countries': countries
    }
    return render(
        request=request,
        context=context_dict,
        template_name='country/country_confirm_delete.html',
    )