import time
from driver_setup import create_driver
from pages.home_page import HomePage

def test_add_task_in_my_day():
    driver = create_driver()
    home = HomePage(driver)

    print(" App launched")

    home.dismiss_popup_if_present()
    print(" Popup handled")

    home.open_my_day()
    print(" My Day opened")

    home.tap_add_task()
    print(" Add Task clicked")

    home.enter_task("Meeting at 3:30PM")
    print(" Task entered")

    home.tap_zero_icon()
    print(" Reminder icon selected")

    driver.press_keycode(66)  # ENTER
    print(" Task saved")

    driver.quit()
    print(" Test completed")
