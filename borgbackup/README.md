# Borgbackup

Configures a host to run regular backups (with borgmatic) to a borg repo.

Assumes data to backup is in `/mnt/ct_data/**/backup` and puts it in the borg
repos specified in the `borg_repos` Ansible variable.

Place SSH keys in `files/ssh`. Assumes these keys are already in the
`.ssh/authorized_hosts` of remote repos.

`borg repos` Ansible variable format (`make editvars`)
```yaml
borg_repos:
  - name: <descriptive repo name, for borg>
    repo: <as per borg repo syntax, for borg>
    ssh: # optional if no ssh
      hostname: <server hostname, without `user@`>
      key_filename: <key file to use for ssh>
```
## Considerations for LXC container

The local repo dirs must be accessible rw by `root` within the container which maps to UID 100000 GID 100000 outside the container by default.

The playbook tests for rw access to any local repos. If that assertion fails,
either remap UID/GID (see https://archive.is/VtPzV) or `chown -R 100000:100000`
the directory outside the container.

## Notifications

The variable `borgmatic_hooks` contains optional hooks to ping services like Healthchecks and warn if there has been no checkins.

Format as per the value for `hooks:` in the config file, see https://github.com/borgmatic-collective/borgmatic/blob/418ebc8843ef503d45d4d6af4cec62ea21fde001/docs/how-to/monitor-your-backups.md (v1.7.7 because that's what Debian 12 provides.)

## Backups

### Create repos

> Will create all repos listed in config.yaml if they don't already exist.

Within host:
`$ borgmatic init --encryption repokey`

### Manually create a backup

Within host:
`$ sudo borgmatic create --verbosity 1 --stats --list`

### Mount a backup for inspection/selective restore

Within host:
> Ensure FUSE option is selected in container's options if using LXC host.

> Prefer local repos to remote ones if available, it's faster.

`$ sudo mkdir -p /mnt/borgfs && sudo borgmatic mount --archive latest --mount-point /mnt/borgfs [--repository <repo name as per config.yaml] && sudo bash`

### Restore backup

> Prefer local repos to remote ones if available, it's faster.

Within host:
`$ sudo borgmatic extract --archive latest`
