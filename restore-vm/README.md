# Restore VM

Use this playbook to migrate VMs from one host to another. The files must all
be available locally (XML machine definition + hard drives.)

# Requirements

the VMs' xml definition files and the VMs' disks must be locally available.
They will be copied over the network (slow) to the new host.

# Usage

Edit the file `vm_list.yml` (see `vm_list.yml.example` for inspiration.)

/!\ When running the playbbok, the XML files will be modified to match the disk
location on the target host. /!\

`copy_disks` is set to true by default, and will transfer the disk images from
the local host to the target host. If the files are already there or have been
copied via other (more efficient) means, it can be set to false to drastically
speedup execution.

Typically:
```
ansible-playbook --limit mainframe playbook.yml --extra-vars 'copy_disks=false'
```

# Limitations

If a VM with the same name already exists on the target host, the task will
fail and the VM's settings won't be changed.

XML definition files are modified in place. This is not ideal, there is
probably a way to edit the XML within the `lookup` operation in the `virt`
module.

The autostart task is not idempotent and will always show as changed.
