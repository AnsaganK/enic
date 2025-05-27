from django.conf import settings


def verify_recaptcha(token):
    import requests
    data = {
        'secret': settings.RECAPTCHA_PRIVATE_KEY,
        'response': token
    }
    r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
    return r.json().get('success', False)
