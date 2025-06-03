echo " Running pytest with Allure."
pytest -s -v --alluredir=allure-results

echo "Generating Allure report"
allure generate allure-results --clean -o allure-report

echo "Opening Allure report in browser"
allure open allure-report