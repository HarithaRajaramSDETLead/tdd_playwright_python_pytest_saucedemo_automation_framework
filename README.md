# TDD Playwright Python Pytest SauceDemo Automation Framework

This project is a Python-based UI automation framework built with Playwright and pytest for testing the SauceDemo application. It follows a Test-Driven Development (TDD) style structure and organizes test logic using a Page Object Model (POM) approach.

The framework is designed to validate login flows, product access, and other common end-to-end user actions in a realistic web application environment.

## Tech Stack

- Python
- Playwright
- pytest
- Page Object Model (POM)
- SauceDemo Demo App

## Project Structure

```text
tdd_playwright_python_pytest_saucedemo_automation_framework/
├── helper/
│   ├── __init__.py
│   ├── actions_for_pages.py
│   ├── data.py
│   └── utils.py
├── locators/
│   ├── __init__.py
│   ├── inventory_locators.py
│   ├── login_locators.py
│   └── ...
├── pages/
│   ├── __init__.py
│   ├── inventory_page.py
│   ├── login_page.py
│   └── ...
├── test_tests/
│   ├── __init__.py
│   ├── test_inventory.py
│   ├── test_login.py
│   └── ...
├── README.md
└── ...