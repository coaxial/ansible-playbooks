limit ?= edms
verbosity ?=
.PHONY: all install_reqs playbook_run clean limit_info editvars decrypt_var

all: limit_info playbook_run

limit_info:
	@echo 'Running against: $(limit)'

install_reqs:
	@echo 'Fetching dependencies...'
	@if [ -s requirements.yml ]; then \
		ansible-galaxy install -r requirements.yml --force; \
	fi

.vault_pass:
	@# ask user for vault pass and save it with mode 0600, unless it's already saved.
	@stty -echo; \
	read -p ".vault_pass missing, enter vault password: " vpwd; \
	stty echo; \
	echo $$vpwd > .vault_pass; \
	chmod 600 .vault_pass; \
	echo

vars/vars.yml: .vault_pass
	@ansible-vault create vars/vars.yml --vault-password-file .vault_pass

editvars: vars/vars.yml
	@ansible-vault edit vars/vars.yml --vault-password-file .vault_pass

playbook_run: .vault_pass install_reqs
	@ansible-playbook --limit $(limit) playbook.yml --vault-password-file .vault_pass $(verbosity)
	@- rm -f playbook.retry

clean:
	@-rm -f .vault_pass

decrypt_var:
	@yq read vars.yml $(var) | ansible-vault decrypt --vault-password-file .vault_pass

list-backups:
	@# Decrypt the key, save it to a ramdisk, list backups, and delete key
	@sudo umount /tmp/tarsnap-key 2>/dev/null;\
	rmdir /tmp/tarsnap-key 2>/dev/null;\
	mkdir /tmp/tarsnap-key &&\
	sudo mount -t tmpfs -o size=1m tarsnap-key /tmp/tarsnap-key &&\
	ansible-vault decrypt ./files/edms.key \
		--output /tmp/tarsnap-key/tarsnap.key \
		--vault-password-file ./.vault_pass &&\
	tarsnap \
		--list-archives \
		--keyfile /tmp/tarsnap-key/tarsnap.key | sort;\
	shred /tmp/tarsnap-key/tarsnap.key;\
	sudo umount /tmp/tarsnap-key &&\
	rmdir /tmp/tarsnap-key

list-backups-with-size:
	@# Must run the command on the target because it needs the cache dir
	@ssh user@edms.lan "sudo tarsnap --print-stats -f '*'"
