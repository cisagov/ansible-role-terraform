# ansible-role-terraform #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-terraform/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-terraform/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-terraform.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-terraform/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-terraform.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-terraform/context:python)

This is an Ansible role for installing
[Terraform](https://www.terraform.io/) and
[terraform-docs](https://github.com/terraform-docs/terraform-docs).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| group | The group associated with the Terraform and terraform-docs binaries. | `root` | No |
| mode | The mode of the Terraform and terraform-docs binaries. | `0755` | No |
| owner | The owner of the Terraform and terraform-docs binaries. | `root` | No |
| install\_dir | The directory where the Terraform and terraform-docs binaries are to be installed. | `/usr/local/bin` | No |
| terraform\_version | The version of Terraform to install. | `1.0.4` | No |
| terraform\_docs\_version | The version of terraform-docs to install. | `0.14.1` | No |

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - terraform
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
