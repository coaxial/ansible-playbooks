# Add IP playbook

Adds the IP defined in vars.yml to the target host. Only works with netplan for
now.

It will also add a new entry to your inventory file and updated the DNS server.

Updating the DNS server assumes it is a Linux machine that can run ansible
commands (pihole on a raspberry pi for instance)

## Usage

`ansible-playbook --limit <my host> playbook.yml`

## Variables

`addip__before`: a line that comes before the line to replace[0]
`addip__after`: a line that comes after the line to replace[0]
`addip__ipv4`: IPv4 address to add
`addip__hostname`: hostname for the new IP, added to DNS server
`addip__inventory_file`: full path to inventory file

[0]: this is confusing so here is an example:
```
line1 # this is the addip__before
line2 # this is the target
line3 # this is the addip__after
```
