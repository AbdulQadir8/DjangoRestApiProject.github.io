from django.http import HttpResponse,JsonResponse
def home_page(Request):
    print("Home page requested")
    friends=[
        'ankit',
        'ravi',
        'uttam'
    ]
    return JsonResponse(friends,safe=False)