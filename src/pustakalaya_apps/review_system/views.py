from django.shortcuts import render,HttpResponse
from .forms import ReviewForm
from django.http import JsonResponse
from .models import Review
from django.contrib.auth.models import User
import datetime
# Create your views here.


def review_system_view(request):
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
                p = Review()
                p.post = data
                p.content_type = content_type
                p.content_id = content_id
                p.user = request.user
                p.save()
                return JsonResponse({'response': data, "content_id": content_id, "content_type": content_type,"pk_value":p.pk })
            else:
                return JsonResponse({'response':data,"content_id":content_id,"content_type":content_type})
        else:
            return JsonResponse({'response':"user_not_logged_in","content_id":content_id,"content_type":content_type})

        return JsonResponse({'response': data,"content_id":content_id,"content_type":content_type})
    else:
        form = ReviewForm()
    return JsonResponse({'response':'Review system'})


def delete(request):
    print("We are in delete section\n")
    if request.method == "POST":
        pk_value =request.POST["input_pk"]
        query = Review.objects.get(pk=pk_value)
        query.delete()
        return HttpResponse("Deleted!")
    else:
        return HttpResponse("Error when deleting!")


def edit(request):

    if request.method == "POST":
        data = request.POST["input"]
        content_id = request.POST["content_id"]
        content_type = request.POST["content_type"]
        pk_val = request.POST["pk_val"]

        if request.user.is_authenticated:

            if data is not None and content_type is not None and content_id is not None:

                p = Review.objects.get(pk=pk_val,content_type=content_type,content_id=content_id)
                p.post = data
                p.updated = datetime.datetime.now()
                p.save()

                return JsonResponse({'response': data, "content_id": content_id, "content_type": content_type,"pk_value":p.pk })
            else:
                return JsonResponse({'response':data,"content_id":content_id,"content_type":content_type})
        else:
            return JsonResponse({'response':"user_not_logged_in","content_id":content_id,"content_type":content_type})

        return JsonResponse({'response': data,"content_id":content_id,"content_type":content_type})

    else:
        form = ReviewForm()
    #return HttpResponse( 'Hellow world')
    return JsonResponse({'response':'Review system'})


