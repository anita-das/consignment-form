from django.shortcuts import render

# Create your views here.
def consignment_form(request):
    return render(request, 'form/consignment_form.html', {})
