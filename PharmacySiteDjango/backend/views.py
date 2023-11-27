from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Medicine, Order, Pharmacy
from django.http import JsonResponse
from .forms import OrderForm


def homeView(request):
    query = request.GET.get('q')
    medicines = Medicine.objects.all()

    if query:
        medicines = filter_medicines_by_query(medicines, query)

    form = process_order_form(request)

    return render(request, 'backend/home.html', {'medicines': medicines, 'form': form})


def filter_medicines_by_query(medicines, query):
    return medicines.filter(name__icontains=query)


def process_order_form(request):
    if request.method == 'POST':
        print('post')
        form = OrderForm(request.POST)
        if form.is_valid():
            medicine_id = request.POST.get('medicine_id')
            medicine = Medicine.objects.get(id=medicine_id)
            order = form.save(commit=False)
            order.medicine = medicine
            order.save()
        print(form.errors)
        return redirect('home')
    else:
        form = OrderForm()
    return form


def about_page_view(request):
    return render(request, 'backend/about-us.html')


def maps_page_view(request):
    pharmacies = Pharmacy.objects.all()
    return render(request, 'backend/maps.html', {'pharmacies': pharmacies})
