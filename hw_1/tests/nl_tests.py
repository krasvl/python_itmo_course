import pytest
from click.testing import CliRunner
from ..utils.nl import nl

def test_nl_file():
    runner = CliRunner()
    
    with runner.isolated_filesystem():
        with open('file1.txt', 'w') as f:
            f.write('line 1\nline 2\nline 3\n')

        result = runner.invoke(nl, ['file1.txt'])
        
        assert result.output == '1\tline 1\n2\tline 2\n3\tline 3\n'

def test_nl_stdin():
    runner = CliRunner()
    
    result = runner.invoke(nl, input='line 1\nline 2\nline 3\n')
    
    assert result.output == '1\tline 1\n2\tline 2\n3\tline 3\n'

if __name__ == '__main__':
    pytest.main()