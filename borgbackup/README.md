# Borgbackup

Configures a host to run regular backups (with borgmatic) to a borg repo.

Assumes data to backup is in `/data/**/backup`, collects it all to `/backup`,
and puts it in a borg repo.

Place SSH keys in `files/ssh`.
