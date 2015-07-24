rdb
===

Copied from celery.contrib.rdb @514f23
https://github.com/celery/celery/blob/514f23e03d103b093d40f9e73a687a001aec781f/celery/contrib/rdb.py


Install
-------

::

    pip install git+https://github.com/davidszotten/rdb.git


Usage
-----

::

    with open('/tmp/rdb.log', 'w') as out:
        from rdb import Rdb; Rdb(out=out).set_trace()
