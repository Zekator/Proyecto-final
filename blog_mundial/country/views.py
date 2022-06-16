from django.shortcuts import render
from country.models import Country


# Create your views here.


def country_list(request):
    countries = Country.objects.all()

    context_dict = {
        'countries': countries
    }

    return render(
        request=request,
        context=context_dict,
        template_name="country_list.html"
    )

def country_add(request):
    return render(request, 'country_form.html')