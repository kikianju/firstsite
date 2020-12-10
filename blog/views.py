from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == 'POST':
        print("request log" + str(request))
        username = request.method.POST.get('username');
        password = request.method.POST.get('password');

    return render(request, 'addresses/login.html')