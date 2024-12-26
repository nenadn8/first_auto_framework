### Nenad's first test framework.

#### Features

1. **Selenium/Python test framework using the Page Object Model**
   1. classes containing generic methods for common page actions
   2. logging infrastructure
   3. assertions **(NEW!)**
   4. ordering (via fixtures) **(NEW!)**
2. **Login test** - for https://www.letskodeit.com/
   1. includes a negative test **(NEW!)**

#### Planned & potential features

1. **Screenshots on test failure**
2. **Further addition of pytest fixtures**
3. **TestRail integration**
4. **Headless execution via terminal parameters if possible**

#### Changelog/notes

**Commit 9** (2024-12-26): Note: check test_valid_login, test_invalid_login, login_successful and login_failed for naming consistency.

**Commit 7** (2024-12-06): Note: Maybe remove the default value for locator_type in SeDriver for simplicity and consistency. If done this way, also change LoginPage methods to reflect this change. 

**Commit 6** (2024-11-29): Fixed a bug where unittest didn't recognize there is 1 test in the suite. Test methods must start with "test_" which wasn't the case initially which caused the bug.
