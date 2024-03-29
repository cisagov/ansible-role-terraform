# ansible-role-terraform #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-terraform/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-terraform/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-terraform/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-terraform/actions/workflows/codeql-analysis.yml)

This is an Ansible role for installing
[Terraform](https://www.terraform.io/) and
[terraform-docs](https://github.com/terraform-docs/terraform-docs).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| terraform\_docs\_version | The version of terraform-docs to install. | `0.14.1` | No |
| terraform\_group | The group associated with the Terraform and terraform-docs binaries. | `root` | No |
| terraform\_install\_dir | The directory where the Terraform and terraform-docs binaries are to be installed. | `/usr/local/bin` | No |
| terraform\_mode | The mode of the Terraform and terraform-docs binaries. | `0755` | No |
| terraform\_owner | The owner of the Terraform and terraform-docs binaries. | `root` | No |
| terraform\_version | The version of Terraform to install. | `1.0.4` | No |

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install Terraform
      ansible.builtin.include_role:
        name: terraform
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

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
