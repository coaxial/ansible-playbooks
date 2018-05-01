# Healthchecks

Deploys a [healtchecks](https://github.com/healthchecks/healthchecks) instance for monitoring cron jobs etc

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

TBD

# Usage

```
$ ansible-galaxy install -r requirements.yml -f
$ ansible-playbooks --limit <host> install.yml [--vault-password-file .vault_pass]
```
