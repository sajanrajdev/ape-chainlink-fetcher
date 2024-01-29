from rich.console import Console
console = Console()

def test_add(owner, my_contract):
    MAX_UINT = 115792089237316195423570985008687907853269984665640564039457584007913129639935
    a = my_contract.test()

    assert a == MAX_UINT
    console.print('[blue]DONE[/blue]')