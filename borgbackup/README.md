# Borgbackup

Configures a host to run regular backups (with borgmatic) to a borg repo.

Assumes data to backup is in `/mnt/ct_data/**/backup`, collects it all to `/mnt/backups`,
and puts it in a borg repo.

Place SSH keys in `files/ssh`.

Backup to remote repo:
```yaml
borg_repos:
  - name: <descriptive repo name, for borg>
    repo: <as per borg repo syntax, for borg>
    ssh:
      host_name: <server, without `user@`>
      host_hash: <host's fingerprint, for ssh, get it with `ssh-keyscan -H <hostname>`> (optional if no ssh)
      key_filename: <key file to use for ssh> (optional if no ssh)
```

# Backups

## Manually create a backup

Within host:
`$ sudo borgmatic create --verbosity 1 --stats --list`

## Mount a backup for inspection/selective restore

Within host:
> Ensure FUSE option is selected in container's options if using LXC host

`$ sudo mkdir -p /mnt/borgfs && sudo borg mount --archive latest --mount-point /mnt/borgfs [--repository <repo name as per config.yaml] && sudo bash`

## Restore backup

Within host:
`$ sudo borgmatic extract --archive latest`
