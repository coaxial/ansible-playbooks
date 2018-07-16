limit ?= mainframe
.PHONY: all install_reqs playbook_run clean limit_info editvars

all: limit_info playbook_run

limit_info:
	@echo 'Running against: $(limit)'

install_reqs:
	@echo 'Fetching dependencies...'
	@if [ -s requirements.yml ]; then \
		ansible-galaxy install -r requirements.yml --force; \
	fi

# ask user for vault pass and save it with mode 0600, unless it's already saved.
.vault_pass:
	@stty -echo; \
	read -p ".vault_pass missing, enter vault password: " vpwd; \
	stty echo; \
	echo $$vpwd > .vault_pass; \
	chmod 600 .vault_pass; \
	echo

editvars: .vault_pass
	@ansible-vault edit vars/vars.yml --vault-password-file .vault_pass

playbook_run: .vault_pass install_reqs
	@ansible-playbook --limit $(limit) playbook.yml --vault-password-file .vault_pass
	@- rm -f playbook.retry

clean:
	@-rm -f .vault_pass
