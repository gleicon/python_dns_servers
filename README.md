Python, DNS and Redis


About
=====
Simple servers to deliver customized DNS data. These servers rely on Redis as storage backend. 
If the data isn't on redis, they will use the configured DNS to resolve and answer back.
These servers can be used to intercept queries, test devices that have no accessible resolv.conf, etc
There are two versions with gevent or twisted. Make sure the user you run these daemons can bind to port 53.


cli
===
There is a CLI to ease inserting new hosts

    python dns_cli.py add host ip
    python dns_cli.py del host


gevent version
==============
python gevent_dns.py

twisted version
===============
python tx_dns.tac


test and usage
==============

$ sudo python gevent_dns.py

$ dig google.com
$ dig @127.0.0.1 google.com
$ python dns_cli.py add google.com 127.0.0.1
$ dig @127.0.0.1 google.com

