from ape import networks, accounts, project
from ape.cli import get_user_selected_account
from rich.console import Console
console = Console()

def main():
    with networks.ethereum.mainnet.use_provider("infura"):
        # account = accounts.load("dev")
        account = get_user_selected_account()
        account.deploy(project.Example)