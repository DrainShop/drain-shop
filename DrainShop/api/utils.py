from django.db import models

class StatusBasket(models.IntegerChoices):
    BASKET_CREATED = (1, 'Корзина создана')
    EMPTY = (2, 'Пустая')
    LOADING = (3, 'Не звершена')
    FILLED = (4, 'Наполнена')
    CHECK_OUT = (5, 'Оплаченная')


class StatusDelivery(models.IntegerChoices):
    ORDER_PROCESSED = (1, 'Заказ приянт в обработку')
    ORDER_COLLECTED_READY_SHIP = (2, 'Заказ собран и готов к отправке')
    ORDER_TRANSFERRED_TO_COURIER = (3, 'Заказ передан курьеру')
    ORDER_ON_WAY_DELIVERY_LOCATION = (4, 'Заказ находится в пути к месту доставки')
    ORDER_DELIVERED = (5, 'Заказ доставлен получателю')
    ORDER_REJECTED_CANCELED = (6, 'Заказ отклонен или отменен')
    ORDER_RETURNED_WAREHOUSE = (7, 'Заказ возвращен на склад')
    ORDER_DELIVERED_CONFIRMATION_RECEIVED = (8, 'Заказ доставлен, подтверждение получено')

class StatusOrder(models.IntegerChoices):
    CREATED_ORDER = (1, 'Заказ создан')
    ACCEPTED_ORDER = (2, 'Заказ принят')
    DELIVERED_ORDER = (3, 'Заказ доставлен')
    COMPLETED_ORDER = (4, 'Заказ завершен')
    CANCELLED_ORDER = (5, 'Заказ отменен')



# class StatusPaymentMethod(models.IntegerChoices):
#     PAYMENT_PENDING = (1, 'Ожидание оплаты')
#     PAYMENT_PROCESSING = (2, 'Обработка платежа')
#     PAYMENT_SUCCESSFUL = (3, 'Оплата прошла успешно')
#     PAYMENT_FAILED = (4, 'Оплата не удалась')
#     PAYMENT_REFUNDED = (5, 'Оплата возвращена')
#     PAYMENT_CANCELLED = (6, 'Оплата отменена')
#     PAYMENT_EXPIRED = (7, 'Оплата истекла')
#     PAYMENT_VERIFICATION_PENDING = (8, 'Ожидание верификации платежа')
#     PAYMENT_VERIFICATION_FAILED = (9, 'Не удалось верифицировать платеж')
#     PAYMENT_VERIFIED = (10, 'Платеж верифицирован')
#
#
# class PaymentMethod(models.IntegerChoices):
#     CREDIT_CARD = 1, 'Кредитная карта'
#     CASH_PAYMENT = 2, 'Наличная оплата'
