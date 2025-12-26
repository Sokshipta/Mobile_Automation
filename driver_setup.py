from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "sdk_gphone16k_x86_64"
    options.automation_name = "UiAutomator2"
    options.app_package = "com.microsoft.todos"
    options.app_activity = "com.microsoft.todos.ui.LaunchActivity"
    options.no_reset = True
    options.new_command_timeout = 300

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )
    return driver
