# deploy-docker-service

Deploy a docker service using `docker-compose`

## Usage

Make any edits necessary to the `docker-compose.yml` (ports, address binding,
etc.), set your vars (either `rds__src_path` or `rds__src_repo`), then run:

```yaml
---
- hosts: all
  vars:
    rds__src_repo: https://github.com/user/my-service.git
    rds__src_repo_version: deploy

  pre_tasks:
    - name: Ensure everything is in place
    ...

  roles:
    - ../deploy-docker-service
```

## Variables

`rds__src_path`: path to the directory containing the `docker-compose.yml`
file. The service's name will be derived from the basename to lowercase with
spaces replaced by `-`s. i.e. `/path/to/MyAwesome Project` will yield
`myawesome-project` as the service name.

`rds__src_repo`: URL to the git repo to deploy
`rds__src_repo_version`: The branch/tag name. Defaults to `HEAD` (only used
when `rds__src_repo` is set)

*Note*: `rds__src_path` and `rds__src_repo` are mutually exclusive.
