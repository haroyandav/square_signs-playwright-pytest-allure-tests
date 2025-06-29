echo "🚀 Running pytest with Allure..."
pytest -s -v --alluredir=allure-results

echo "🧼 Cleaning previous Allure report (if any)..."
rm -rf allure-report

echo "📊 Generating fresh Allure report..."
allure generate allure-results --clean -o allure-report

echo "🌐 Opening Allure report in browser..."
allure open allure-report