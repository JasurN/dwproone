from django.contrib.auth.models import User

from sales.models import Customer, Box, Contract


def create_user():
    return User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')


def create_customers(number_customers, name):
    for counter_id in range(number_customers):
        Customer.objects.create(
            name=f'{name} {counter_id}'
        )


def create_boxes(count):
    customer = Customer.objects.create(
        name=f'Box customer'
    )
    for boxes_id in range(count):
        Box.objects.create(length=300,
                           width=400,
                           height=500,
                           configuration='SSSSS',
                           customer_id=customer.id,
                           dimension='300x400x500')


def create_contract(count):
    customer = Customer.objects.create(
        name=f'Contract customer'
    )
    for contract_id in range(count):
        Contract.objects.create(customer_id=customer.id,
                                contract_number=f'DPC LB 19050{contract_id}')
