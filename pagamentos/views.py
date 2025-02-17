# views.py
import json
import requests
import base64
from datetime import datetime
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment


def get_access_token():
    """Obtém o token de acesso da API da M-Pesa."""
    consumer_key = settings.MPESA_CONFIG['CONSUMER_KEY']
    consumer_secret = settings.MPESA_CONFIG['CONSUMER_SECRET']
    url = 'https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=(consumer_key, consumer_secret))
    return response.json().get('access_token')

def lipa_na_mpesa_online(request):
    """Inicia o pagamento via M-Pesa."""
    access_token = get_access_token()
    url = 'https://api.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json',
    }
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    password = base64.b64encode(
        f"{settings.MPESA_CONFIG['SHORTCODE']}{settings.MPESA_CONFIG['PASSKEY']}{timestamp}".encode()
    ).decode()
    payload = {
        'BusinessShortCode': settings.MPESA_CONFIG['SHORTCODE'],
        'Password': password,
        'Timestamp': timestamp,
        'TransactionType': 'CustomerPayBillOnline',
        'Amount': '100',  # Valor do pagamento
        'PartyA': '258841234567',  # Número do cliente
        'PartyB': settings.MPESA_CONFIG['SHORTCODE'],
        'PhoneNumber': '258841234567',  # Número do cliente
        'CallBackURL': settings.MPESA_CONFIG['CALLBACK_URL'],
        'AccountReference': 'Pagamento123',
        'TransactionDesc': 'Pagamento de Serviço',
    }
    response = requests.post(url, json=payload, headers=headers)
    return JsonResponse(response.json())


@csrf_exempt
def mpesa_callback(request):
    """Recebe a resposta da M-Pesa após o pagamento."""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            transaction_id = data.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {}).get('Item', [{}])[0].get('Value')
            amount = data.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {}).get('Item', [{}])[1].get('Value')
            phone_number = data.get('Body', {}).get('stkCallback', {}).get('CallbackMetadata', {}).get('Item', [{}])[4].get('Value')
            status = 'success' if data.get('Body', {}).get('stkCallback', {}).get('ResultCode') == 0 else 'failed'

            # Salvar o pagamento no banco de dados
            MpesaPayment.objects.create(
                phone_number=phone_number,
                amount=amount,
                transaction_id=transaction_id,
                status=status,
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'}, status=405)