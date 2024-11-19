echo "nl tests" > ./artifacts/tests_result.txt
pytest -v ./tests/nl_tests.py >> ./artifacts/tests_result.txt

echo "tail tests" >> ./artifacts/tests_result.txt
pytest -v ./tests/tail_tests.py >> ./artifacts/tests_result.txt

echo "wc tests"  >> ./artifacts/tests_result.txt
pytest -v ./tests/wc_tests.py >> ./artifacts/tests_result.txt