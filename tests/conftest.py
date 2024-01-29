import pytest


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def my_contract(project, owner):
    # ^ use the 'project' fixture from the 'ape-test' plugin
    return owner.deploy(project.Example)