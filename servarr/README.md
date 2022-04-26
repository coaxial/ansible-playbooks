# Servarr playbook

Sets up a Servarr instance with:

- nzbget
- transmission
- sonarr
- radarr

## Notes

### nzbget

If `files/nzbget/history` and/or `files/nzbget/stats` are present when running
this role, they will be copied over to the instance and will erase existing
files. A backup of the original files will be generated. Be careful not to
overwrite existing data.

Config must be restored manually, through the GUI (Settings > System > Restore
Settings)

Default password is `nzbget`:`tegbnz6789` and the interface is accessible at
`http://<ip>/nzbget`.

### transmission

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
