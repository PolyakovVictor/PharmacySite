document.getElementById('orderForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Отменяет стандартное действие формы

    // Получаем значения из полей формы
    var deliveryAddress = document.getElementById('deliveryAddress').value;
    var pharmacy = document.getElementById('pharmacySelect').value;
    var contactName = document.getElementById('contactName').value;
    var contactPhone = document.getElementById('contactPhone').value;

    // TODO: Отправка данных на сервер или другая обработка заказа здесь

    // Закрытие модального окна
    $('#orderModal').modal('hide');

    // Очистка полей формы
    document.getElementById('deliveryAddress').value = '';
    document.getElementById('pharmacySelect').value = '';
    document.getElementById('contactName').value = '';
    document.getElementById('contactPhone').value = '';
});