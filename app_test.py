from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -------------------------
# APPIUM OPTIONS
# -------------------------
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "sdk_gphone16k_x86_64"
options.automation_name = "UiAutomator2"

options.app_package = "com.microsoft.todos"
options.app_activity = "com.microsoft.todos.ui.MainActivity"  # <-- FIXED

options.no_reset = True
options.auto_grant_permissions = True

# -------------------------
# DRIVER INIT
# -------------------------
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 30)

print(" App launched successfully")

# -------------------------
# DISMISS POPUP (if exists)
# -------------------------
try:
    dismiss_btn = wait.until(
        EC.element_to_be_clickable(
            (
                AppiumBy.ANDROID_UIAUTOMATOR,
                'new UiSelector().className("android.widget.Button").textContains("DIS")'
            )
        )
    )
    dismiss_btn.click()
    print(" Clicked DISMISS button")
except:
    print("ℹ No DISMISS popup found")

# -------------------------
# CLICK + ADD TASK
# -------------------------
add_task_btn = wait.until(
    EC.element_to_be_clickable(
        (
            AppiumBy.XPATH,
            "//android.widget.ImageButton[@content-desc='Add a task']"
        )
    )
)
add_task_btn.click()
print(" Clicked + Add Task")

time.sleep(5)
driver.quit()
print(" Test completed successfully")from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# =========================
# HARD-CODED CONFIG
# =========================
TASK_TEXT = "I have a meeting at 3:30 PM"
APPIUM_SERVER = "http://127.0.0.1:4723"

PLATFORM_NAME = "Android"
DEVICE_NAME = "sdk_gphone16k_x86_64"
AUTOMATION_NAME = "UiAutomator2"

APP_PACKAGE = "com.microsoft.todos"
APP_ACTIVITY = "com.microsoft.todos.ui.MainActivity"

# =========================
# DRIVER SETUP
# =========================
options = UiAutomator2Options()
options.platform_name = PLATFORM_NAME
options.device_name = DEVICE_NAME
options.automation_name = AUTOMATION_NAME
options.app_package = APP_PACKAGE
options.app_activity = APP_ACTIVITY
options.no_reset = True
options.auto_grant_permissions = True

driver = webdriver.Remote(APPIUM_SERVER, options=options)
wait = WebDriverWait(driver, 30)

print(" App launched")

# =========================
# DISMISS POPUP
# =========================
try:
    wait.until(EC.element_to_be_clickable((
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiSelector().className("android.widget.Button").textContains("DIS")'
    ))).click()
    print(" Dismissed popup")
except TimeoutException:
    print("ℹ No popup")

# =========================
# OPEN ADD TASK
# =========================
try:
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        '//android.widget.RelativeLayout[@resource-id="com.microsoft.todos:id/homeview_banner_stub"]/android.widget.LinearLayout'
    ))).click()
    print(" Banner clicked")
except TimeoutException:
    pass

try:
    wait.until(EC.element_to_be_clickable((
        AppiumBy.XPATH,
        "//android.widget.ImageButton[@content-desc='Add a task']"
    ))).click()
    print("➕ Add Task clicked")
except TimeoutException:
    pass

# =========================
# TYPE TASK
# =========================
typed = False
for locator in [
    (AppiumBy.CLASS_NAME, "android.widget.EditText"),
    (AppiumBy.ID, "com.microsoft.todos:id/task_entry_view"),
    (AppiumBy.XPATH, "//android.widget.EditText")
]:
    try:
        field = wait.until(EC.element_to_be_clickable(locator))
        field.click()
        field.clear()
        field.send_keys(TASK_TEXT)
        typed = True
        print(f" Typed: {TASK_TEXT}")
        break
    except TimeoutException:
        continue

if not typed:
    raise RuntimeError(" Task input not found")

driver.press_keycode(66)
print("✅ Task submitted")

time.sleep(1.5)

# =========================
# FIND TASK
# =========================
recycler = wait.until(EC.presence_of_element_located((
    AppiumBy.XPATH,
    '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.microsoft.todos:id/tasks_recycler_view"]'
)))

try:
    task = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        (
            'new UiScrollable(new UiSelector().resourceId("com.microsoft.todos:id/tasks_recycler_view"))'
            '.scrollIntoView(new UiSelector().text("{}"))'
        ).format(TASK_TEXT)
    )
    print("✅ Task found")
except NoSuchElementException:
    raise RuntimeError(" Task not found")

# =========================
# OPEN TASK DETAILS
# =========================
task.click()
print(" Task opened")

# =========================
# CLEANUP
# =========================
time.sleep(3)
driver.quit()
print(" Test completed")
