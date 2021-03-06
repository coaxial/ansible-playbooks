# `downloader` deployment

This playbook will deploy `downloader` as a set of docker containers on the
target host.

It requires a separate playbook because it needs to ensure some directories
exist beforehand since `docker-downloader` uses arbitrary directories for some
of the volumes.

## Variables

`downloader__scratch_path`: Physical device on which to store, extract,
and repair the downloads (ideally a different drive than the storage drive)
`downloader__media_path`: Physical device on which to store the files
`downloader__tarsnap_key_path`: Path to the tarsnap key for backing up
`downloader__tarsnap_key_dest`: Where to place the tarsnap key on the remote
host

## Files

A tarsnap key is required, place it in `files/tarsnap.key`

## Run

`$ ansible-playbooks --limit <host> playbook.yml`
