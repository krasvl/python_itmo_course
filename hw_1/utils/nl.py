import click

def number_lines(input_stream):
    for i, line in enumerate(input_stream, 1):
        click.echo(f'{i}\t{line}', nl=False)

@click.command()
@click.argument('file', type=click.File('r'), required=False)
def nl(file):
    """Утилита для вывода пронумерованных строк."""
    if file:
        number_lines(file)
    else:
        number_lines(click.get_text_stream('stdin'))

if __name__ == '__main__':
    nl()