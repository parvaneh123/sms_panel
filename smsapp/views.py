from django.http import HttpResponse
from smsapp.models import CustomerGroups, Customer
from kavenegar import *


def my_view(request):
    if request.method == 'GET':
        uuid = request.GET.get('Uuid')
        text_sms = request.GET.get('text')
        groups = CustomerGroups.objects.filter(unique_group=uuid).first()
        customer = Customer.objects.filter(unique_id=uuid).first()
        if groups:
            id_customer = Customer.objects.filter(group_customer=groups).all()
            for i in id_customer:
                api = KavenegarAPI(
                    '7456493166424C494576574B6B61594861696A4E5A664E756F7346312B4B417138437A716E4F7A4C304D413D')
                params = {'sender': '1000596446', 'receptor': "0" + str(i.phone_number), 'message': text_sms}
                response = api.sms_send(params)
            return HttpResponse('send message success')
        elif customer:
            api = KavenegarAPI(
                '7456493166424C494576574B6B61594861696A4E5A664E756F7346312B4B417138437A716E4F7A4C304D413D')
            params = {'sender': '1000596446', 'receptor': "0" + str(customer.phone_number), 'message': text_sms}
            response = api.sms_send(params)
            return HttpResponse('send message for customer')
        else:
            return HttpResponse('failed')
