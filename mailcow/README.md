# `mailcow` deployment

This playbook will deploy a mailcow email server.

Min config is 1Ghz, 1GB RAM, 5GB disk. Recommended is 1.5GB RAM + swap.

## Prerequisites

- Up and running Ubuntu host
- Docker
- A borg backup repository (cf. https://borgbackup.readthedocs.org/en/latest/quickstart.html)
- SSH keys and passphrase matching the borg repo

## Variables

N/A

## Files

Filename | Purpose
--- | ---
timesyncd.conf | Configure timedatectl
mailcow.conf | Mailcow config file, cf. https://mailcow.github.io/mailcow-dockerized-docs/install/
borgmatic/config.yaml | borgmatic configuration, cf. https://torsion.org/borgmatic/
borgmatic/backup_rsa{,.pub} | ssh keys for connecting to the remote borg repo
borgmatic/config.yaml | borgmatic configuration file
borgmatic/passphrase | remote borg repo passphrase
borgmatic/.jobber | jobber file (cf. https://dshearer.github.io/jobber/doc/v1.3/#jobfile)

## Run

### Install from scratch

`$ ansible-playbooks --limit <host> install.yml [--vault-password-file .vault_pass]`

### Restore an existing installation (WIP)

`$ ansible-playbooks --limit <host> restore.yml`
