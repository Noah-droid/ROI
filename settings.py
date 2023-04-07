# ussd_service/settings.py
INSTALLED_APPS = [
    ...
    'ussd',
    'subscription',
]

MIDDLEWARE = [
    ...
    'ussd.middleware.UssdMiddleware',
]

USSD_DEFAULT_SESSION_CONFIG = {
    'expiry': 300,
    'storage': 'ussd.storage.session.DatabaseUssdSession',
}

USSD_PROVIDERS = {
    'africastalking': {
        'backend': 'ussd.providers.africastalking.AfricasTalkingProvider',
        'config': {
            'username': 'YOUR_USERNAME',
            'api_key': 'YOUR_API_KEY',
            'shortcode': 'YOUR_SHORTCODE',
            'callback_url': 'https://your-domain.com/ussd_subscription/',
        },
    },
}
