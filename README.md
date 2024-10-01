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



документация создается при помощи модуля - mkdocs

пишем docstrings в модулях

устанавливаются модули mkdocs и mkdocstrings-python

создаем папку docs, c файлами документации .md, в который указаны соответствующие модули для внеснеия в док-цию
hello.md, index.md, test.md

создается файл mkdocs.yml

mkdocs --help
Commands:
  build      Build the MkDocs documentation.
  get-deps   Show required PyPI packages inferred from plugins in mkdocs.yml.
  gh-deploy  Deploy your documentation to GitHub Pages.
  new        Create a new MkDocs project.
  serve      Run the builtin development server.

используем mkdocs serve