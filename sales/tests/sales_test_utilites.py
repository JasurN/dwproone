from django.contrib.auth.models import User


def create_number_model_instance(model, number_customers, name):
    for counter_id in range(number_customers):
        model.objects.create(
            name=f'{name} {counter_id}'
        )


def create_user():
    return User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')
