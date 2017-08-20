# New VM

Launch a new Ubuntu 16.04 VM on the target host. The VMs are all created after
a template that is cloned to change the relevant things (network MAC, UUID,
etc.)

The playbook will prompt for the amount of CPU cores, nominal, and burst memory
allocation.

Once the playbook completes, it will show the new VM's MAC address. I couldn't
find a way to extract its IP so the MAC is there to help look it up in the DHCP
server's lease table.

See comments in the playbook for details as well.

## Variables

Name | Default value | Notes
--- | --- | ---
`vm_base_name` | ubuntu-16.04_base | name for the template VM that will be
cloned (every VM will be based on this one)
`vm_disk_template` | ubuntu-16.04_base.qcow2 | name for the base VM disk file
`local_base_disk_dir` | ../../base-vms | where to find the `vm_disk_template`
file locally
`remote_base_disk_dir` | /media/storage/vms | where to store the disk images on
the target host
