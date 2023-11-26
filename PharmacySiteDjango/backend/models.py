from django.db import models


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    # Другие поля, например, телефон, часы работы и т.д.

    def __str__(self):
        return self.name


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
    delivery_address = models.CharField(max_length=200)

    def __str__(self):
        return f"Order {self.id} - {self.medicine.name}"
