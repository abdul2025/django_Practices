from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world from index fun in the view.py', "number": 100}
    return render(request, 'basicApp/index.html', context_dict)

def relative(request):
    return render(request, 'basicApp/relative_url_template.html')

def other(request):
    return render(request, 'basicApp/other.html')
