# Healthchecks

Deploys a [healtchecks](https://github.com/healthchecks/healthchecks) instance for monitoring cron jobs etc.

# Prerequisites

- Ubuntu host
- Borg backup repository (cf. https://borgbackup.readthedocs.org/en/latest/quickstart.html)
- SSH keys and passphrase matching the borg repo

# Dependencies

- coaxial.base
- coaxial.mailcow
- geerlingguy.docker
- geerlingguy.pip

# Files

`files/id_rsa{,.pub}` | SSH keys to the remote borg repo
`files/known_hosts` | Avoids the unknown key message when connecting to remote repo

For more details, see the [ansible-role-healthchecks](https://github.com/coaxial/ansible-role-healthchecks) readme.

# Usage

To install:
```
$ ansible-galaxy install -r requirements.yml -f
$ ansible-playbooks --limit <host> install.yml [--vault-password-file .vault_pass]
```

To restore from the latest borg backup (run install playbook first)
```
$ ansible-galaxy install -r requirements.yml -f
$ ansible-playbooks --limit <host> restore.yml [--vault-password-file .vault_pass]
```
