from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    # ---------- LOCATORS ----------
    DISMISS_BTN = (By.ID, "android:id/button2")

    MY_DAY = (
        By.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("My Day")'
    )

    ADD_TASK_BTN = (
        By.ACCESSIBILITY_ID,
        "Add a task"
    )

    TASK_INPUT = (By.CLASS_NAME, "android.widget.EditText")

    REMINDER_ZERO = (
        By.ANDROID_UIAUTOMATOR,
        'new UiSelector().text("0")'
    )

    # ---------- ACTIONS ----------
    def dismiss_popup_if_present(self):
        if self.is_present(self.DISMISS_BTN):
            self.click(self.DISMISS_BTN)

    def open_my_day(self):
        self.click(self.MY_DAY)

    def tap_add_task(self):
        self.click(self.ADD_TASK_BTN)

    def enter_task(self, task_text):
        self.send_keys(self.TASK_INPUT, task_text)

    def tap_zero_icon(self):
        self.click(self.REMINDER_ZERO)
