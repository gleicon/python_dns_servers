import sys
import redis

A_RECORD_PREFIX = 'DNS:PASSTHRU:A:%s'

p = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=p)


def help():
    print "usage: dns_cli add|del <host> [ip if adding a new entry]"
    sys.exit()


def do_add(host, ip):
    r.set(A_RECORD_PREFIX % host, ip)


def do_del(host):
    r.delete(A_RECORD_PREFIX % host)


def main():
    args = sys.argv[1:]

    if len(args) < 2:
        help()

    cmd = args[0]

    if cmd not in ['add', 'del']:
        help()

    if cmd == 'add' and len(args) == 3:
        do_add(args[1], args[2])
    elif cmd == 'del':
        do_del(args[1])
    else:
        help()


if __name__ == '__main__':
    main()
