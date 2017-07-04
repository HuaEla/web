from django.shortcuts import render,redirect,get_object_or_404
from . import models
from .forms import messageForm


# Create your views here.
def messageview(request):
    messagelist1=models.messageModel.objects.all().order_by('-created_time')
    form = messageForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            messageModel=form.save()
            messageModel.save()
            messagelist2=models.messageModel.objects.all().order_by('-created_time')
            form = messageForm()
            return render(request, 'message/message.html', context={'messagelist': messagelist2, 'form': form})
        else:
            form = messageForm()
    return render(request,'message/message.html',context={'messagelist':messagelist1,'form':form})