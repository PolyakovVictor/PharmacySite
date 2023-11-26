from django.http import HttpResponse
from django.shortcuts import render
from .models import Medicine


def homeView(request):
    medicines = Medicine.objects.all()
    return render(request, 'backend/home.html', {'medicines': medicines})


def order_medicine(request):
    if request.method == 'POST':
        # Обработка заказа лекарства
        # Ваш код обработки заказа здесь
        return HttpResponse("Order placed successfully!")  # Или любой другой ответ

    return HttpResponse("Invalid request method")
