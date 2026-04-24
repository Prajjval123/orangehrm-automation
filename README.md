# OrangeHRM Automation Project

Selenium + Python test automation for [OrangeHRM](https://opensource-demo.orangehrmlive.com)
OrangeHRM is an open source HR management application - used here as a demo site for automation practice.

---

## What I automated

| Module              | Test Cases | What is covered |
|---------------------|-----------|-----------------|
| Login               | 6 | valid login, dashboard visible, wrong credentials, empty username, logout |
| Employee Management | 5 | employee list page loads, search existing employee, search non-existing, add employee navigation |

**Total: 11 test cases**

---

## Folder structure

```
orangehrm-automation/
│
├── pages/
│   ├── base_page.py       → common methods shared by all pages
│   ├── login_page.py      → login page locators and actions
│   ├── dashboard_page.py  → dashboard navigation and logout
│   └── pim_page.py        → employee list, search, add employee
│
├── tests/
│   ├── test_login.py      → 6 login test cases
│   └── test_employee.py   → 5 employee management test cases
│
├── utils/
│   └── test_data.py       → credentials and test inputs in one place
│
├── conftest.py            → opens and closes Chrome for each test
├── pytest.ini             → pytest config
└── requirements.txt       → libraries to install
```

---

## How to run

```bash
# install libraries (only needed once)
pip install -r requirements.txt

# run all tests
pytest

# run only login tests
pytest tests/test_login.py

# run only employee tests
pytest tests/test_employee.py
```

---

## Tech used
- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model pattern
- WebDriver Manager
