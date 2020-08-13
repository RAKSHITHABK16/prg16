from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

from django.core.files.storage import FileSystemStorage

#uploading and displaying the uploaded image
def img_upld(request):
    return render(request,"img_upld.html")

def img_display(request):
    file_url=False
    if request.method=="POST" and request.FILES:
        image=request.FILES['sam']
        print(image)
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)
                
    return render(request,"img_display.html",context={'file_url':file_url})
