import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_nzbget_history(host):
    f = host.file('/mnt/downloads/nzb/data/queue/history')

    assert f.mode == 0o644
    assert f.user == 'nzbget'
    assert f.group == 'nzbget'
    assert f.contains('nzbget diskstate file version 62\n3644')


def test_nzbget_stats(host):
    f = host.file('/mnt/downloads/nzb/data/queue/stats')

    assert f.mode == 0o644
    assert f.user == 'nzbget'
    assert f.group == 'nzbget'
    assert f.contains('news.example.org')


def test_nzbget_config(host):
    f = host.file('/etc/nzbget.conf')

    assert f.mode == 0o644
    assert f.user == 'nzbget'
    assert f.group == 'nzbget'
    assert f.contains('# Test conf file')


def test_nzbget_service(host):
    assert host.service('nzbget').is_running


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
    assert host.service('transmission-daemon').is_running


def test_sonarr_config(host):
    files = ['sonarr.db', 'config.xml']

    for file in files:
        f = host.file('/var/lib/sonarr/' + file)

        assert f.mode == 0o644
        assert f.user == 'sonarr'
        assert f.group == 'sonarr'


def test_sonarr_service(host):
    assert host.service('sonarr').is_running


def test_radarr_config(host):
    files = ['radarr.db', 'config.xml']

    for file in files:
        f = host.file('/var/lib/radarr/' + file)

        assert f.mode == 0o644
        assert f.user == 'radarr'


def test_radarr_service(host):
    assert host.service('radarr').is_running
