# Swarm Node

This is to configure a VM that will be a Docker Swarm node within Portainer.

## `/var/lib/docker` partition/disk

Use a separate partition or disk for `var/lib/docker` so that the bootdisk
doesn't get full from all the docker images and volumes.

```
$ parted /dev/<disk> mklabel gpt
$ parted -a opt /dev/<disk> mkpart primary ext4 0% 100%
$ mkfs.ext4 -L dockerdata /dev/<disk>1
$ echo 'LABEL=dockerdata /var/lib/docker ext4 defaults 0 2' >> /etc/fstab
```

## `eth1`

Configured with the cloud-init image, static IP.
