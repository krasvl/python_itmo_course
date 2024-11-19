import pytest
from click.testing import CliRunner
from ..utils.tail import tail

def test_tail_1file():
    runner = CliRunner()
    
    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\n')

        result = runner.invoke(tail, ['file1.txt', '--lines', 2])
        
        assert result.output == 'line 2\nline 3\n'

def test_tail_3files():
    runner = CliRunner()
    
    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\n')
        with open('file2.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\n')
        with open('file3.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\n')

        result = runner.invoke(tail, ['file1.txt', 'file2.txt', 'file3.txt', '--lines', 1])
        
        assert result.output == '==> file1.txt <==\nline 3\n==> file2.txt <==\nline 3\n==> file3.txt <==\nline 3\n'

def test_tail_1file_default_lines():
    runner = CliRunner()
    
    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\nline 4\nline 5\nline 6\nline 7\nline 8\nline 9\nline 10\nline 11\n')

        result = runner.invoke(tail, ['file1.txt'])
        
        assert result.output == 'line 2\nline 3\nline 4\nline 5\nline 6\nline 7\nline 8\nline 9\nline 10\nline 11\n'

def test_tail_stdin():
    runner = CliRunner()
    
    result = runner.invoke(tail, ['--lines', 2], input='line 1\nline 2\nline 3\n')
        
    assert result.output == 'line 2\nline 3\n'

if __name__ == '__main__':
    pytest.main()