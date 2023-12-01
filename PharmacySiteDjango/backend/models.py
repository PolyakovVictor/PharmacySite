from django.db import models


class Pharmacy(models.Model):
    address = models.CharField(max_length=200)
    address_url = models.CharField(max_length=2000)
    opening_hours = models.CharField(max_length=200)
    image = models.ImageField(upload_to='pharmacy_buildings', blank=True, null=True)

    def __str__(self):
        return self.address


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='medicine_images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Order(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    full_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return f"Order {self.id} - {self.medicine.name}"
