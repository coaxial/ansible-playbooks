# Znc playbook

Install and configure ZNC, the IRC bouncer

# Usage

- `make` will install the dependencies listed in `dependencies.yml`, prompt for the encryption password if `.vault_pass` is missing, and run the playbook against the default hosts (i.e. znc)
- `make limit=host1,host2` will run the playbook on host1 and host2 only instead of the default hosts (i.e. znc)
- `make editvars` will prompt for the encryption password if `.vault_pass` is missing and edit the encrypted variables file at `vars/enc_vars.yml`

Configure users in the `znc__users` variable and then connect to ZNC using that user's certificate for passwordless auth.

# Registering new cert with Libera

To register a new certificate fingerprint (after a fresh install on ZNC for intance), `/msg NickServ identify <nick> <password>` and then `/msg NickServ cert add`.

# Sample `znc__users`

```yaml
znc__users:
  - username: 1972_bob_dylan
    nick: bd
    password: "secret"
    salt: "salty"
    # get fingerprint with `openssl x509 -fingerprint -noout -in /path/to/cert.pem | cut -f2 -d '=' | tr -d ':' | tr '[:upper:]' '[:
    pubkey: "ffffffffffffffffffffffffffffffffffffffff"
    networks:
      - name: libera
        altnick: snakeprime # optional, defaults to nick + '_'
        clientcert: "~/.irssi/certs/user.pem" # optional
        encoding: UTF-8 # optional, defaults to UTF-8
        ident: THE snake # optional, defaults to nick
        nick: snake
        realname: Snako # optional, defaults to nick
        sasl: true # optional, default is false
        server: "irc.libera.chat +7000"
```
