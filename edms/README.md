# EDMS playbook

This playbook installs Mayan EDMS on an Ubuntu machine.

It also sets nightly up backups using tarsnap, and uses postgres instead of sqlite.

## Targets

Any host in the `edms` group

## Minimum configuration

- 64bit multicore CPU, >= 1Ghz
- 2 GB RAM

## Updating Mayan EDMS

The `mayan_target_version` in the `vars.yml` file defines which version to
install when the playbook is run. Pending a playbook to update Mayan, follow
these instructions:
https://mayan.readthedocs.io/en/latest/releases/2.7.html#using-pip


## Restoring a backup

/!\ This playbook will drop the current databse, any data that hasn't been
backed up will be lost /!\

Use the [restore-backup.yml](./restore-backup.yml) playbook.

> That playbook assumes that it is restoring to the same version of Mayan EDMS.
> If that is no the case, run the playbook with --extra-vars "upgrade=true" to
> migrate the database after it has been restored.
