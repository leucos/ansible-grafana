import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleGetVar(Ansible, var):
    return Ansible("debug", "msg={{ %s }}" % var)["msg"]


def test_grafana_listens(host):
    bind = AnsibleGetVar(host.ansible, "grafana_http_addr")
    port = AnsibleGetVar(host.ansible, "grafana_http_port")
    sock = host.socket("tcp://{0}:{1}".format(bind, port))
    assert sock.is_listening
