# django_app

для обхода проверки сертификата при работе с mac изменил в  django/core/mail/backends/smtp.py

import certifi  <-- добавил

@cached_property
def ssl_context(self):
    if self.ssl_certfile or self.ssl_keyfile:
        ssl_context = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_CLIENT)
        ssl_context.load_cert_chain(self.ssl_certfile, self.ssl_keyfile)
        return ssl_context
    else:
        return ssl.create_default_context(cafile=certifi.where()) <-- добавил cafile=certifi.where()