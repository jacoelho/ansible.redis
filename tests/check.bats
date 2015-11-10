#!/usr/bin/env bats

@test "redis-server is installed and is in the PATH" {
  command -v redis-server
}

@test "should have redis-server running" {
  [ "$(ps aux | grep redis-server | grep -v grep)" ]
}

@test "redis should be listening for connections" {
  [ "$(netstat -an |grep 0.0.0.0:6379)" ]
}

@test "should have an redis-server default file" {
  [ -e "/etc/default/redis-server" ]
}

@test "should have an redis-server config file" {
  [ -e "/etc/redis/redis.conf" ]
}
