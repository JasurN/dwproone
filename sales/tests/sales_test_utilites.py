from datetime import datetime, timedelta
from django.contrib.auth.models import User

from sales.models import Customer, Box, Contract, Order


def create_user():
    return User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')


def create_customers(count):
    customers = []
    last_order = Customer.objects.last()
    customer_id = 1
    if last_order:
        customer_id = last_order.id + 1
    for counter_id in range(count):
        customers.append(
            Customer.objects.create(name=f'Customer {customer_id}', short_name=f'customer{customer_id}')
        )
        customer_id += 1
    return customers


def create_boxes(count):
    boxes = []
    customers = create_customers(count)
    for counter_id in range(count):
        boxes.append(
            Box.objects.create(length=300,
                               width=400,
                               height=500,
                               configuration='SSSSS',
                               customer_id=customers[counter_id].id,
                               dimension='300x400x500')
        )
    return boxes


def create_contract(count):
    contracts = []
    customers = create_customers(count)
    for counter_id in range(count):
        contracts.append(
            Contract.objects.create(customer_id=customers[counter_id].id,
                                    contract_number=f'DPC LB 19050{counter_id}')
        )
    return contracts


def create_order(count):
    orders = []
    contracts = create_contract(count)
    boxes = create_boxes(count)
    for i in range(count):
        orders.append(
            Order.objects.create(contract_id=contracts[i].id,
                                 box_id=boxes[i].id,
                                 order_date=datetime.now() - timedelta(5),
                                 ship_date=datetime.now() + timedelta(10),
                                 quantity=1000,
                                 remaining=1000,
                                 delivered=0)
        )
