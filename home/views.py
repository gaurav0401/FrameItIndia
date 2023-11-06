from django.shortcuts import render
from django.http import HttpResponse
from .models import Images
from .forms import imageForm
from django.contrib import messages 
from django.core.paginator import Paginator
# Create your views here.


def index (request):
    if request.method=="POST":
        try:

            form=imageForm(request.POST , request.FILES)
            if form.is_valid():
                 form.save()
                 messages.success(request , "Your Post has been uploaded successfully....")
        except Exception as e:
             messages.danger(request , "Failed to upload post...try after some time...")

    form=imageForm
    image=Images.objects.all()
    paginate=Paginator(image , 12)
  
    page_no=request.GET.get('page')
    final_data=paginate.get_page(page_no)
    totalpage=final_data.paginator.num_pages

    context={'form':form , 'image':image , 'image':final_data , 'totalpagelist':[n+1 for n in range(totalpage)] , 'lastpage':totalpage }
    return render(request, "index.html" , context)



  
  