# taskserver

Installs a taskserver on the target and restore the latest backup.

Will also gather files required to configure the client at `client_files/`.

To test the server without changing the local config (remember to disable NAT reflection if required):
```
$ docker run -it --rm -v `pwd`/configure-client:/test-client:ro -v `pwd`/client_files:/client_certs:ro alpine sh -c /test-client
```

To disable backups and/or restoring from latest backup, use `td__enable_backups` and `td__restore_latest_backup`.
