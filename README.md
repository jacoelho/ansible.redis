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

All the options support a list format, for example:

    redis_bind:
      - 127.0.0.1
      - 1.2.3.4

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
