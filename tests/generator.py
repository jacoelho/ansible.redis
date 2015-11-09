#!/usr/bin/env python

import yaml

ignore = ['redis_version',
          'redis_conf',
          'redis_sentinel_conf',
          'redis_repository',
          'redis_repository_key',
          'redis_user',
          'redis_soft_limit',
          'redis_sentinel_master_ip',
          'redis_sentinel_master_port']

with open("defaults/main.yml", 'r') as stream:
    configs = yaml.load(stream)

target = open('templates/redis.conf.j2', 'w')

target.write("# This file is managed by Ansible, all changes will be lost.\n")
for k, v in configs.iteritems():
    if k in ignore:
        continue

    if k.startswith("redis_sentinel"):
        continue

    keyword = k.replace("redis_", "")
    keyword = keyword.replace("_", "-")

    target.write("{{% if {0} is defined and {0}|string|length > 0 %}}\n".format(k))
    target.write("{{% if {0} is not string and {0} is not number %}}\n".format(k))
    target.write("{{% for item in {0} %}}\n".format(k))
    target.write("{0} {{{{ item }}}}\n".format(keyword))
    target.write("{% endfor %}\n")
    target.write("{% else %}\n")
    target.write("{0} {{{{ {1} }}}}\n".format(keyword, k))
    target.write("{% endif %}\n")
    target.write("{% endif %}\n")
target.close()

target = open('templates/sentinel.conf.j2', 'w')
target.write("# This file is managed by Ansible, all changes will be lost.\n")
target.write("{% if redis_sentinel_master_ip is defined and redis_sentinel_master_ip|string|length > 0 %}\n")


### monitor 1st
monitor = configs.pop("redis_sentinel_monitor")
k = "redis_sentinel_monitor"
keyword = k.replace("redis_sentinel_", "")
keyword = keyword.replace("_", "-")

target.write("{{% if {0} is defined and {0}|string|length > 0 %}}\n".format(k))
target.write("{{% if {0} is not string and {0} is not number %}}\n".format(k))
target.write("{{% for item in {0} %}}\n".format(k))
target.write("sentinel {0} {{{{ item }}}}\n".format(keyword))
target.write("{% endfor %}\n")
target.write("{% else %}\n")
target.write("sentinel {0} {{{{ {1} }}}}\n".format(keyword, k))
target.write("{% endif %}\n")
target.write("{% endif %}\n")

for k, v in configs.iteritems():
    if k in ignore:
        continue

    if not k.startswith("redis_sentinel"):
        continue

    keyword = k.replace("redis_sentinel_", "")
    keyword = keyword.replace("_", "-")

    target.write("{{% if {0} is defined and {0}|string|length > 0 %}}\n".format(k))

    if keyword in ['dir', 'port', 'logfile', 'daemonize']:
        target.write("{0} {{{{ {1} }}}}\n".format(keyword, k))
    else:
        target.write("{{% if {0} is not string and {0} is not number %}}\n".format(k))
        target.write("{{% for item in {0} %}}\n".format(k))
        target.write("sentinel {0} {{{{ item }}}}\n".format(keyword))
        target.write("{% endfor %}\n")
        target.write("{% else %}\n")
        target.write("sentinel {0} {{{{ {1} }}}}\n".format(keyword, k))
        target.write("{% endif %}\n")
    target.write("{% endif %}\n")
target.write("{% endif %}\n")
target.close()
