import click

def count_lines(file):
    file.seek(0)
    return sum(1 for _ in file)

def count_words(file):
    file.seek(0)
    return sum(len(line.split()) for line in file)

def count_chars(file):
    file.seek(0)
    return sum(len(line) for line in file)

@click.command()
@click.argument('files', nargs=-1, type=click.File('r'))
@click.option('--lines', is_flag=True, help='Подсчитать количество строк.')
@click.option('--words', is_flag=True, help='Подсчитать количество слов.')
@click.option('--chars', is_flag=True, help='Подсчитать количество символов.')
def wc(files, lines, words, chars):
    """Утилита для подсчёта строк, слов и символов."""
    if not files:
        text = click.get_text_stream('stdin')
        result = ''
        if lines:
            result += f'{count_lines(text)} '
        if words:
            result += f'{count_words(text)} '
        if chars:
            result += f'{count_chars(text)} '
        click.echo(f'{result.strip()}')
    else:
        l, w, c = 0, 0, 0
        for file in files:
            result = ''
            if lines:
                l += count_lines(file)
                result += f'{count_lines(file)} '
            if words:
                w += count_words(file)
                result += f'{count_words(file)} '
            if chars:
                c += count_chars(file)
                result += f'{count_chars(file)} '
            click.echo(f'{result.strip()} {file.name}')
        if len(files) > 1:
            click.echo(f'{l} {w} {c} total')

if __name__ == '__main__':
    wc()