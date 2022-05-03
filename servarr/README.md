# Servarr playbook

Sets up a Servarr instance with:

- nzbget
- transmission
- sonarr
- radarr

## Notes

### NZBGet

Use the GUI to selectively restore parts of the config as per these
instructions: https://nzbget.net/backup-and-restore-settings

Default password is `nzbget`:`tegbzn6789` and the interface is accessible at
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

`config.xml` should be manually edited beforehand to make sure the base URL is
set to `/sonarr`. Then restore the config using the GUI.

The interface is accessible at `http://<ip>/sonarr`.

### Radarr

`config.xml` should be manually edited beforehand to make sure the base URL is
set to `/sonarr`. Then restore the config using the GUI.

The interface is accessible at `http://<ip>/radarr`.
