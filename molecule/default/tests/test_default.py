import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_prometheus_is_running(host):
    host.service("prometheus").is_running


def test_prometheus_is_enabled(host):
    host.service("prometheus").is_enabled


def test_prometheus_listen_port(host):
    host.socket("tcp://0.0.0.0:9100").is_listening
