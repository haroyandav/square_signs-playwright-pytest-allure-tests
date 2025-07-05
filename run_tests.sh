echo "Cleaning previous Allure results and report..."
rm -rf allure-results allure-report

echo "Running pytest with Allure..."
pytest -s -v --alluredir=allure-results

echo "Generating fresh Allure report..."
allure generate allure-results --clean -o allure-report

echo "Opening Allure report in browser..."
allure open allure-report