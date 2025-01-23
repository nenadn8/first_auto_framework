### Nenad's first test framework.

#### Features

1. **Selenium/Python test framework using Page Object Model**
   1. classes containing generic methods for common page actions
   2. logging infrastructure
   3. assertions
   4. ordering (via fixtures)
   5. **set-up and tear-down fixtures (NEW!)**
   6. **driver generator class for reuse of common commands (NEW!)**
   7. **command line parameters for different browsers (Firefox, Chrome, Edge) (NEW!)**
2. **Login test** - for https://www.letskodeit.com/
   1. including a negative test

#### Planned & potential features

1. Screenshots on test failures
2. Further addition of pytest fixtures
3. TestRail integration
4. Headless execution via terminal parameters
5. **Switch to Selenium Manager for WebDriver handling. (NEW!)**

#### Known issues (NEW!)

1. **~~Sometimes the second test (successful login) fails, even though the site works. For some reason, the email fields gets filled in twice, causing an invalid login when a valid login should be inputted. (NEW!)~~ Fixed!**  

#### Changelog/notes

**Commit 11 (2025-01-23): fix for the successful login test's false negatives. Some readme.md tweaks. (NEW!)**

**Commit 10 (2025-01-17): login_test.py refactor, added driver_generator.py, conftest.py, small changes to login_page.py (NEW!)**

**Commit 9** (2024-12-26): Note: check test_valid_login, test_invalid_login, login_successful and login_failed for naming consistency.

**Commit 7** (2024-12-06): Note: Maybe remove the default value for locator_type in SeDriver for simplicity and consistency. If done this way, also change LoginPage methods to reflect this change. 

**Commit 6** (2024-11-29): Fixed a bug where unittest didn't recognize there is 1 test in the suite. Test methods must start with "test_" which wasn't the case initially which caused the bug.
