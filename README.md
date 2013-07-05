django-contact
===================

Store messages from contact-form in database. Managable from backoffice


Installation
------------

``pip install -e git+https://github.com/tomaszroszko/django-contact.git#egg=django_contact.git``

*settings.py*

```

INSTALED_APPS = (
    ...
    'contact',
    ...
)
```

*urls.py*

```

urlpatterns = patterns('',
    ...
    url(r'^contact/', include('contact.urls')),
    ...
)
```

*run commands*

```
python manage.py syncdb
python manage.py migrate
```
