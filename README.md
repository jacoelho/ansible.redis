jacoelho.redis
=========

An ansible role that installs redis-server on Ubuntu.

Tested on ubuntu 14.04 (Trusty)

Role Variables
--------------

Each redis configuration is mapped to a variable (see `defaults/main.yml`)

To pin a specific redis version:

    redis_version: ""

Configure listening address and port:

    redis_port: "6379"
    redis_bind: "0.0.0.0"

All options support a list format, for example:

    redis_bind:
      - 127.0.0.1
      - 1.2.3.4

Configuring redis sentinel:

    redis_sentinel_enable: true
    redis_sentinel_monitor:
      - master 127.0.0.1 6379 2
    redis_sentinel_down_after_milliseconds:
      - master 60000
    redis_sentinel_failover_timeout:
      - master 180000
    redis_parallel_syncs:
      - master 1

If you want to run only redis sentinel:

      redis_enable: false

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: jacoelho.redis, redis_bind: "0.0.0.0" }

License
-------

BSD

Author Information
------------------

This role was created in 2015 by [José Coelho](https://github.com/jacoelho)
