# `unifi` deployment

This will deploy the unifi controller and backup service for it.

## Variables

`unifi__tarsnap_key_path`: Path to the tarsnap key for backing up
`unifi__tarsnap_key_dest`: Where to place the tarsnap key on the remote
host

## Files

A tarsnap key is required, place it in `files/tarsnap.key`

## Run

`$ ansible-playbooks --limit <host> playbook.yml`
