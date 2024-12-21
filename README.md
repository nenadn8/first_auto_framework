### Nenad's first test framework.

#### Features

1. **Selenium/Python test framework using the Page Object Model**
   1. classes containing generic methods for common page actions
   2. logging infrastructure
2. **Login test** - for https://www.letskodeit.com/

#### Planned & potential features

1. **Unittest assertions**
2. **Screenshots on test failure**
3. **Pytest fixtures** - e.g. for ordering tests
4. **TestRail integration**
5. **Headless execution via terminal parameter if possible**

#### Changelog/notes

**Commit 7** (2024-12-06): Note: Maybe remove the default value for locator_type in SeDriver for simplicity and consistency. If done this way, also change LoginPage methods to reflect this change. 

**Commit 6** (2024-11-29): Fixed a bug where unittest didn't recognize there is 1 test in the suite. Test methods must start with "test_" which wasn't the case initially which caused the bug.
