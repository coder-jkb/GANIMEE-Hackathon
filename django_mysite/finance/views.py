from django.shortcuts import render

# Create your views here.
def index(request):
   return render(request,'finance/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def course(request):
   return render(request, 'finance/course.html')