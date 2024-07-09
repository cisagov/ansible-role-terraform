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


@pytest.mark.parametrize(
    "executable",
    ["/usr/local/bin/terraform", "/usr/local/bin/terraform-docs"],
)
def test_tools_executable_architecture(host, executable):
    """Verify that the installed tools have the appropriate architecture."""
    command = f"file {executable}"
    cmd = host.run(command)
    assert cmd.rc == 0, f"Command {command} returned a non-zero exit code."
    # host.system_info.arch will return either "x86_64" or "aarch64", whereas
    # file prints out the architecture as "x86-64" or "aarch64".  The call to
    # string.replace() is therefore necessary to match up these two
    # conventions.
    assert host.system_info.arch.replace("x86_64", "x86-64") in cmd.stdout


@pytest.mark.parametrize(
    "command",
    ["/usr/local/bin/terraform --version", "/usr/local/bin/terraform-docs --version"],
)
def test_tools_can_run(host, command):
    """Verify that the installed tools can run.

    Note that this test can still pass when running under qemu if the
    executable architecture does not match the container but does match
    the host.
    """
    cmd = host.run(command)
    assert cmd.rc == 0, f"Command {command} returned a non-zero exit code."
