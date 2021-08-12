"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "filename", ["/usr/local/bin/terraform", "/usr/local/bin/terraform-docs"]
)
def test_expected_files_are_present(host, filename):
    """Verify that the expected files were installed."""
    f = host.file(filename)
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755
