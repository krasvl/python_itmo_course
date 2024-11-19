import click

def tail_file(file, num):
    lines = file.readlines()
    for line in lines[-num:]:
        click.echo(line, nl=False)

@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
@click.option('--lines', default=10, help='Количество строк для вывода из файла. По умолчанию 10.')
def tail(files, lines):
    """Утилита для вывода последних N строк из каждого файла."""
    if not files:
        tail_file(click.get_text_stream('stdin'), lines)
    else:
        for file in files:
            if len(files) > 1:
                click.echo(f'==> {file.name} <==')
            tail_file(file, lines)

if __name__ == '__main__':
    tail()