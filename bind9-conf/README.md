# bind9-conf

Configuration for Bind9, run against machine hosting the docker container data.

## Vars

```yaml
# Zone file definition
bind9_zones:
  - name: <zone name>
    email: <contact email, s/@/\./>
    template: <filename for the zone in templates/>
    filename: <zonefile name on remote>
    ip: <bind server IP>
    records:
      - name: <record name>
        type: <record type>
        ip: <record IP>
# Allowed hosts
bind9_acls:
  - 10.0.0.0/24
  - 1.2.3.4/32
# DNS forwarders
bind9_forwarders:
  - 10.20.30.40
  - 10.20.30.41
# Config files location
bind9_conf_dir_path: /mnt/nas/bind9/config
```
