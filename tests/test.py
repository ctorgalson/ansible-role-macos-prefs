import os

import pytest

import testinfra.utils.ansible_runner


@pytest.mark.parametrize("domain,string", [
    ("com.googlecode.iterm2", "Name = Dev"),
])
def test_preference_contents(host, domain, string):
    contents = host.check_output("defaults read {}".format(domain))

    assert string in contents
