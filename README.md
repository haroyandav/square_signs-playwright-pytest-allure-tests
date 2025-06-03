#  Automated UI Testing with Playwright + Pytest + Allure

This project contains UI tests written in **Python** using **Playwright** and **Pytest**, with detailed HTML test reports generated using **Allure**.

---

## Requirements

- Python 3.8+
- pip (comes with Python)
- Allure CLI

---

##  Setup 

# STEP 1: Install Python

- Download from: https://www.python.org/downloads/
- During installation, make sure to check **"Add Python to PATH"**

Then verify installation:

```bash
python --version
pip --version
```

# STEP 2: Create & Activate Virtual Environment
```bash 
 python -m venv venv
```

# For macOS / Linux:
```bash 
source venv/bin/activate 
```

# For Windows:
```bash 
venv\Scripts\activate
```

# STEP 3: Install Project Dependencies

```bash 
pip install -r requirements.txt
```

# STEP 4: Install Playwright browsers
```bash 
python -m playwright install
```

# STEP 5: Install Allure CLI
```bash 
brew install allure
```

# STEP 6: Run the Tests and View the Report
```bash 
chmod +x run_tests.sh
```

```bash 
./run_tests.sh
```

## Windows (manual steps):
 - pytest -s -v --alluredir=allure-results
 - allure generate allure-results --clean -o allure-report
 - allure open allure-report


 # Project Structure

├── tests/
│   └── retractable_banners/
│       ├── configuration/
│       │   ├── test_unit_switch.py
│       │   └── test_warning_modal_functionality.py
│       ├── pricing/
│       │   ├── test_base_price.py
│       │   ├── test_discounted_price.py
│       │   └── test_total_price.py
│       ├── test_data/
│       │   └── tab_navigation_data.json
│       ├── ui/
│       │   └── test_tab_navigation.py
│       └── utils/
│           ├── constants.py
│           ├── priceUtils.py
│           └── getDetailsFixture.json
├── pages/
│   ├── base_page.py
│   └── retractable_banners.py
├── utils/                        # Global helper functions or fixtures
├── run_tests.sh                  # Shell script to run tests and open report
├── requirements.txt              # Python dependencies
└── README.md                     # You're here