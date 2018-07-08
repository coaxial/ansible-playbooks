limit ?= mainframe
.PHONY: all install_reqs playbook_run clean

all: playbook_run

install_reqs:
	@echo 'Fetching dependencies...'
	@if [ -s requirements.yml ]; then \
		ansible-galaxy install -r requirements.yml -f; \
	fi

# ask user for vault pass and save it with mode 0600, unless it's already saved.
.vault_pass:
	@if [ ! -s .vault_pass ]; then \
		stty -echo; \
		read -p ".vault_pass missing, enter vault password: " vpwd; \
		stty echo; \
		echo $$vpwd > .vault_pass; \
		chmod 600 .vault_pass; \
		echo; \
	else \
		echo '.vault_pass found'; \
	fi

playbook_run: .vault_pass install_reqs
	ansible-playbook --limit $(limit) playbook.yml --vault-password-file .vault_pass

clean:
	@-rm -f .vault_pass
