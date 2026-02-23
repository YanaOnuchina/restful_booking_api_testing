# Restful-Booker API Automation Project

This repository contains an automated testing framework for the **Restful-Booker API**, a specialized playground for API testing. The project is built using **Python** and **Pytest**.

## Tech Stack

* **Language:** Python 3.x
* **Testing Framework:** Pytest
* **Library:** Requests (HTTP client)
* **Validation:** JSON Schema (jsonschema library)
* **Reporting:** Pytest-HTML

## Project Structure

The project follows a modular architecture for scalability and maintainability:

restful_booking_api_testing/
├── config.py                 # Global configurations (Base URL, Credentials)
├── conftest.py               # Shared fixtures (Auth token, reusable entities)
├── tests/                    # Test suites
│   ├── test_auth.py          # Authentication scenarios
│   └── test_booking_crud.py  # CRUD operations
│   └── test_negative.py      # Negative scenarios
│   └── test_search.py        # Search bookings with parameters
└── .gitignore                # Files excluded from version control

Report screenshot:
<img width="1270" height="575" alt="image" src="https://github.com/user-attachments/assets/c7932f29-63e2-43a0-b580-78f195f6cf17" />
