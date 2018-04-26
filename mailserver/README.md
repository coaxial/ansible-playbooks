# mailserver playbook

This playbook will deploy a mailcow email server.

Min config is 1Ghz, 1GB RAM, 5GB disk. Recommended is 1.5GB RAM + swap.

## Prerequisites

- Up and running Ubuntu host
- Docker
- A borg backup repository (cf. https://borgbackup.readthedocs.org/en/latest/quickstart.html)
- SSH keys and passphrase matching the borg repo

## Dependencies

- coaxial.base
- coaxial.mailcow
- geerlingguy.docker
- geerlingguy.pip

## Files

Filename | Purpose
--- | ---
mailcow.conf | Mailcow config file, cf. https://mailcow.github.io/mailcow-dockerized-docs/install/
borgmatic/backup_rsa{,.pub} | ssh keys for connecting to the remote borg repo
borgmatic/passphrase | remote borg repo passphrase

## Run

### Install from scratch

`$ ansible-galaxy install -r requirements.yml -f`
`$ ansible-playbooks --limit <host> install.yml [--vault-password-file .vault_pass]`

### Restore an existing installation (WIP)

`$ ansible-playbooks --limit <host> restore.yml`
