# Restore VM

Use this playbook to migrate VMs from one host to another. The files must all
be available locally (XML machine definition + hard drives.)

# Usage

Edit the file `vm_list.yml` (see `vm_list.yml.example` for inspiration.)

/!\ When running the playbbok, the XML files will be modified to match the disk
location on the target host. /!\

# Limitations

If a VM with the same name already exists on the target host, the task will
fail and the VM's settings won't be changed.

XML definition files are modified in place. This is not ideal, there is
probably a way to edit the XML within the `lookup` operation in the `virt`
module.
