# mailserver playbook

This playbook will deploy a mailcow email server and hourly backups using [borg](https://borgbackup.readthedocs.io/en/stable/).

Min config is 1Ghz, 1GB RAM, 5GB disk. Recommended is 1.5GB RAM + swap.

Leverages the https://github.com/coaxial/ansible-role-mailcow Ansible role, see its README for more details and its vars.

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

Filename | Purpose | Note
---|---|---
`borgmatic/borg_ssh_key{,.pub}` | ssh keys for connecting to the remote borg repo | cf. https://github.com/coaxial/ansible-role-mailcow for customisation options
`borgmatic/passphrase` | remote borg repo passphrase
`borgmatic/known_hosts` | ssh keys for remote borg repos | cf. https://github.com/coaxial/ansible-role-mailcow for details

## Run

### Install from scratch

`$ ansible-galaxy install -r requirements.yml -f`
`$ ansible-playbooks --limit <host> install.yml [--vault-password-file .vault_pass]`

### Restore an existing installation

`$ ansible-playbooks --limit <host> restore.yml`

The following variables must be defined when restoring: `mailcow__{borg_repo_host,borg_repo_name,ssh_key_name}` because it isn't using the defaults from the `mailcow` role (unlike the `install` playbook.) `mailcow__enable_backups` is also available, but I'm not sure how much sense it makes to disable borg backups when restoring from a borg backup.
