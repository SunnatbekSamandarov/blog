from django.shortcuts import render
from .forms import PostForm
# Create your views here.
def index(request):
    form = PostForm()
    if request.POST:
        forms = PostForm(request.POST or None)
        if forms.is_valid():
            forms.save()
    ctx = {
        'forms':form
    }
    return render(request,'index.html',ctx)
