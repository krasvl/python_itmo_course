import click
from utils.nl import nl
from utils.tail import tail
from utils.wc import wc

@click.group()
def cli():
    pass

cli.add_command(nl)
cli.add_command(tail)
cli.add_command(wc)

if __name__ == '__main__':
    cli()