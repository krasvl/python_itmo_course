import pytest
from click.testing import CliRunner
from ..utils.wc import wc

def test_wc_1file():
    runner = CliRunner()
    
    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\n')

        result = runner.invoke(wc, ['file1.txt', '--lines', '--words', '--chars'])
        
        assert result.output == '3 6 21 file1.txt\n'

def test_wc_2files():
    runner = CliRunner()
    
    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\n')
        with open('file2.txt', 'w') as f:
            f.write('line 2\nline 3\n')

        result = runner.invoke(wc, ['file1.txt', 'file2.txt', '--lines', '--words', '--chars'])
        
        assert result.output == '3 6 21 file1.txt\n2 4 14 file2.txt\n5 10 35 total\n'

def test_wc_stdin():
    runner = CliRunner()
    
    result = runner.invoke(wc, ['--lines', '--words', '--chars'], input='line 1\nline 2\nline 3\n')
    
    assert result.output == '3 6 21\n'

def test_wc_stdin_lines():
    runner = CliRunner()
    
    result = runner.invoke(wc, ['--lines'], input='line 1\nline 2\nline 3\n')
    
    assert result.output == '3\n'

def test_wc_stdin_words():
    runner = CliRunner()
    
    result = runner.invoke(wc, ['--words'], input='line 1\nline 2\nline 3\n')
    
    assert result.output == '6\n'

def test_wc_stdin_chars():
    runner = CliRunner()
    
    result = runner.invoke(wc, ['--chars'], input='line 1\nline 2\nline 3\n')
    
    assert result.output == '21\n'



if __name__ == '__main__':
    pytest.main()