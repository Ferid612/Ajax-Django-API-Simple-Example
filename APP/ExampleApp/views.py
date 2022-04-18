from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
@csrf_exempt 
def function_run(request):
    print("here is working.....: ")
    print(request.POST.get('input_user_name'))
    
    response = JsonResponse({'answer': "Success", })
    
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    
    return response
    