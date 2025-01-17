import  pytest
from base.driver_generator import DriverGenerator


@pytest.fixture(scope="class")
def one_time_setup(request, use_browser):
    print("Running one-time set-up.")
    driver_generator = DriverGenerator(use_browser)
    driver = driver_generator.instantiate_webdriver()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    driver.quit()
    print("Running one-time tear-down.")

def pytest_addoption(parser):
    parser.addoption("--use-browser",
                     default="firefox",
                     choices=["firefox", "chrome", "edge"],
                     help="Accepted browsers are: Firefox, Chrome and Edge.")

@pytest.fixture(scope="session")
def use_browser(request):
    return request.config.getoption("--use-browser")
