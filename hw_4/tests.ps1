Remove-Item -Path "artifacts\*" -Recurse -Force

pytest -v ./src/fibonachi_tests.py > ./artifacts/tests_result.txt

pytest -v ./src/integrate_tests.py >> ./artifacts/tests_result.txt

pytest -v ./src/processes_tests.py >> ./artifacts/tests_result.txt