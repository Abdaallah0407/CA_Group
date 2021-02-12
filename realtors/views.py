from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Realtor


def realtor(request, realtor_id):

    realtor = get_object_or_404(Realtor, pk=realtor_id)

    context = {
        'realtor': realtor
    }

    return render(request, 'realtors/realtor.html', context)
