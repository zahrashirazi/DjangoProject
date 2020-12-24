import requests
from django.test import TestCase

# Create your tests here.
slug = 'test'
data = {
    'username': '09020021211',
    'password': '1646',
    'to': str('09122725221'),
    'from': '30008666021211',
    'text': "Pleas Click The Link Below to Activate Your Login: \n {}".format(
        '/user/activate' + slug),
}
respond = requests.post(url='https://rest.payamak-panel.com/api/SendSMS/SendSMS', data=data).json()
print(respond)
