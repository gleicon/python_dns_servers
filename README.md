Python, DNS and Redis

Simple servers to deliver customized DNS data. These servers rely on Redis as storage backend.

Both of them rely on google's dns as fallback

gevent version
==============
gevent_dns.py

to create a new domain:
    set IP:name ip_addr
    set TXT:name txtfield

twisted version
===============
tx_dns.py

create a new domain SET: 
    domain.tld ip_addr
