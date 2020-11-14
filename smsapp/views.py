from django.http import HttpResponse
from smsapp.models import CustomerGroups, Customer
from kavenegar import *
from django.conf import settings


def my_view(request):
    if request.method == 'GET':
        uuid = request.GET.get('Uuid')
        text_sms = request.GET.get('text')
        groups = CustomerGroups.objects.filter(unique_group=uuid).first()
        customer = Customer.objects.filter(unique_id=uuid).first()
        if groups:
            id_customer = Customer.objects.filter(group_customer=groups).all()
            for i in id_customer:
                api = KavenegarAPI(settings.API_TOKEN)
                params = {'sender': settings.SENDER, 'receptor': "0" + str(i.phone_number), 'message': text_sms}
                response = api.sms_send(params)
            return HttpResponse('send message success')
        elif customer:
            api = KavenegarAPI(settings.API_TOKEN)
            params = {'sender': settings.SENDER, 'receptor': "0" + str(customer.phone_number), 'message': text_sms}
            response = api.sms_send(params)
            return HttpResponse('send message for customer')
        else:
            return HttpResponse('failed')
