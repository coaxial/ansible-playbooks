# `mainframe` configuration

## Pre-requisites/assumptions

- Ubuntu >= 16.04 (default install options, guided LVM, openssh server packages)
- an unprivileged user (assumes `ansible`, specify with `-u` if different)

## Run the playbook

```
# Install roles dependencies
ansible-galaxy install -r requirements.yml -f
# Run playbook
ansible-playbook -i <machine's ip>, playbook.yml --ask-pass --ask-sudo-pass --ask-vault-pass [--remote-user=<unprivileged username>]
```
