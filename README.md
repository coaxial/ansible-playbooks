# My Ansible playbooks

Playbooks have only been tested on Ubuntu 16.04, no guarantees they'll work on
other Ubuntu versions or other distributions.

## Index

Playbook | Purpose | Notes
--- | --- | --
[mainframe](mainframe/) | Configure `mainframe` | Usually requires these options: `-k`, `-K`, `--ask-vault-pass`, requirements in `requirements.yml`
[restore-vm](restore-vm/) | Migrate VMs from another host |
[create-vm](create-vm/) | Launch new, pre-prepared VMs |
[delete-vm](delete-vm/) | Delete an existing VM and its disk files |
[edms](edms/) | Setup and restore Mayan EDMS |
[deploy-docker-service](deploy-docker-service/) | Deploy a docker service from a local directory | Requires a `docker-compose.yml` file
[add-ip](add-ip/) | Add an extra IP address to an existing host |
[downloader](downloader/) | Deploy [docker-downloader](https://github.com/coaxial/docker-downloader) | Requires additional files, cf README
[mailserver](mailserver/) | Deploy mailcow + backing up to borg | Requires additional files, cf README
