from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Favourite
from django.contrib.auth.models import User
import datetime
# Create your views here.


def favourite_collection_view(request):
    # 1. Send the ajax request. not submit request.
    # 2. grab the data here.
    # 3. set the review for the requested doc with respective user
    # 4. return the ajax response.
    if request.method == "POST":
        data = request.POST["input"]
        content_id = request.POST["content_id"]
        content_type = request.POST["content_type"]

        if request.user.is_authenticated:
            if data is not None and content_type is not None and content_id is not None:
                p = Favourite()
                p.favourite_item_type = content_type
                p.favourite_item_id = content_id
                p.user = request.user
                p.save()
                return JsonResponse({'response': data, "content_id": content_id, "content_type": content_type,"pk_value":p.pk})
            else:
                return JsonResponse({'response':data,"content_id":content_id,"content_type":content_type})
        else:
            return JsonResponse({'response':"user_not_logged_in","content_id":content_id,"content_type":content_type})

        return JsonResponse({'response': data,"content_id":content_id,"content_type":content_type})

    return JsonResponse({'response':'Favourite Collection'})


def remove(request):

    if request.method == "POST":
        data = request.POST["input"]
        content_id = request.POST["content_id"]
        content_type = request.POST["content_type"]

        if request.user.is_authenticated:

            if data is not None and content_type is not None and content_id is not None:

                p = Favourite.objects.get(favourite_item_type=content_type,favourite_item_id=content_id,user= request.user)
                p.delete()

                return JsonResponse({'response': data, "content_id": content_id, "content_type": content_type,"pk_value":p.pk })
            else:
                return JsonResponse({'response':data,"content_id":content_id,"content_type":content_type})
        else:
            return JsonResponse({'response':"user_not_logged_in","content_id":content_id,"content_type":content_type})

        return JsonResponse({'response': data,"content_id":content_id,"content_type":content_type})

    return JsonResponse({'response':'Favourite Delete'})


