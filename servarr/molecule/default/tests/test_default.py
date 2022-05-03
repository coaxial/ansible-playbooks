import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_transmission_files(host):
    files = ['stats.json', 'settings.json']
    missing_files = ['dht.dat']

    for file in files:
        f = host.file('/home/debian-transmission/.config/transmission-daemon/'
                      + file)
        assert f.mode == 0o600
        assert f.user == 'debian-transmission'
        assert f.group == 'debian-transmission'

        if file == 'stats.json':
            assert f.content_string == "{}"

    for mfile in missing_files:
        mf = host.file('/home/debian-transmission/.config/transmission-daemon/'
                       + mfile)
        assert not mf.exists


def test_transmission_service(host):
    s = host.service('transmission-daemon')
    assert s.is_running


def test_firewall(host):
    i = host.iptables

    assert (
        '-A INPUT -p tcp -m tcp --dport 51413 '
        '-m conntrack --ctstate NEW,ESTABLISHED '
        '-m comment --comment "Allow Torrent traffic" -j ACCEPT'
    ) in i.rules('filter', 'INPUT')
    assert (
        '-A OUTPUT -p tcp -m tcp --sport 51413 '
        '-m conntrack --ctstate ESTABLISHED '
        '-m comment --comment "Allow Torrent traffic" -j ACCEPT'
    ) in i.rules('filter', 'OUTPUT')
