# Servarr playbook

Sets up a Servarr instance with:

- nzbget
- transmission
- sonarr
- radarr

## Notes

### NZBGet

If any of these files exist at `files/nzbget`:

- nzbget.conf
- stats
- history

They will be copied over existing files on the instance. A backup of the
original will be generated. Be careful not to overwrite existing data.

`nzbget.conf` should be manually edited beforehand to make sure paths etc. match.
Another option is to not restore the config file through this playbook, and use
the GUI instead to selectively restore parts of the config as per these
instructions: https://nzbget.net/backup-and-restore-settings

Default password is `nzbget`:`tegbnz6789` and the interface is accessible at
`http://<ip>/nzbget`.

### Transmission

If any of these files exist at `files/transmission`:

- stats.json
- settings.json
- dht.dat
- blocklist-update.dat
- torrents/
- resume/
- blocklists/

They will be copied over existing files on the instance. A backup of the
original will be generated. Be careful not to overwrite existing data.

The interface is accessible at `http://<ip>/transmission` (note the absence of
trailing `/`).

### Sonarr

If any of these files exist at `files/sonarr`:

- sonarr.db
- sonarr.db-journal
- nzbdrone.db
- nzbdrone.db-journal
- config.xml

They will be copied over existing files on the instance. A backup of the
original will be generated. Be careful not to overwrite existing data.

`config.xml` should be manually edited beforehand to make sure the base URL is
set to `/sonarr`. Another option is to not restore the config this playbook by
leaving `files/sonarr` empty, and use the GUI instead to restore the config.
Make sure the base URL is set to `/sonarr` in `config.xml` beforehand.

The interface is accessible at `http://<ip>/sonarr`.

### Radarr

If any of these files exist at `files/radarr`:

- radarr.db
- config.xml

They will be copied over existing files on the instance. A backup of the
original will be generated. Be careful not to overwrite existing data.

`config.xml` should be manually edited beforehand to make sure the base URL is
set to `/radarr`. Another option is to not restore the config this playbook by
leaving `files/radarr` empty, and use the GUI instead to restore the config.
Make sure the base URL is set to `/radarr` in `config.xml` beforehand.

The interface is accessible at `http://<ip>/radarr`.
