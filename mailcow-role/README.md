# `mailcow` role

This playbook will setup and mailcow email server and regular borg backups.
Backups are saved to `/var/mailcow_backup` and removed once handled by borg.

Min config is 1Ghz, 1GB RAM, 5GB disk. Recommended is 1.5GB RAM + swap.

## Prerequisites

- Up and running Ubuntu host
- Docker
- A borg backup repository (cf. https://borgbackup.readthedocs.org/en/latest/quickstart.html)
- SSH keys and passphrase matching the borg repo

## Variables

N/A

## Files

Filename | Purpose | Note
--- | ---
`timesyncd.conf` | Configure timedatectl | Optional (sane defaults included with this role)
`mailcow.conf` | Mailcow config file, cf. https://mailcow.github.io/mailcow-dockerized-docs/install/
`borgmatic/config.yaml` | borgmatic configuration, cf. https://torsion.org/borgmatic/
`borgmatic/backup_rsa{,.pub}` | ssh keys for connecting to the remote borg repo
`borgmatic/config.yaml` | borgmatic configuration file
`borgmatic/passphrase` | remote borg repo passphrase
`borgmatic/.jobber` | jobber file (cf. https://dshearer.github.io/jobber/doc/v1.3/#jobfile)

## Usage

Minimal playbook:

```yaml
---
- hosts: all
  become: true
  gather_facts: true

  roles:
    - coaxial.mailcow
```
