# Znc playbook

Install and configure ZNC, the IRC bouncer

# Usage

- `make` will install the dependencies listed in `dependencies.yml`, prompt for the encryption password if `.vault_pass` is missing, and run the playbook against the default hosts (i.e. znc)
- `make limit=host1,host2` will run the playbook on host1 and host2 only instead of the default hosts (i.e. znc)
- `make editvars` will prompt for the encryption password if `.vault_pass` is missing and edit the encrypted variables file at `vars/enc_vars.yml`
