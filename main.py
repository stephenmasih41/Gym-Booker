from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# ------------------------ ACCOUNT DETAILS ------------------------
email = "student@test.com"
password = "password123"
url = "https://appbrewery.github.io/gym"

# ------------------------ CHROME OPTIONS ------------------------
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("prefs", {
    "profile.password_manager_leak_detection": False,
})

# ------------------------ START CHROME WEBDRIVER ------------------------
driver = webdriver.Chrome(options=chrome_options)
print("🚀 Opening Gym Website...")
driver.get(url)
driver.implicitly_wait(2)

# ------------------------ LOGIN STEPS ------------------------
print("🔐 Logging in...")
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
driver.implicitly_wait(2)

email_input = driver.find_element(By.ID, "email-input")
password_input = driver.find_element(By.ID, "password-input")
submit_button = driver.find_element(By.ID, "submit-button")

email_input.send_keys(email)
password_input.send_keys(password)
submit_button.click()

# ------------------------ BOOKING / WAITLIST ------------------------
print("📅 Checking Tuesday and Thursday 6PM classes...")

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^=class-card-]")

booked = 0
waitlist = 0
already_booked = 0
all_classes = []

for card in class_cards:
    day_container = card.find_element(By.XPATH, "./ancestor::div[contains(@id,'day-group-')]")
    day_title = day_container.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^=class-time-]").text

        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^=class-name-]").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^=book-button-]")
            class_info = f"{class_name} on {day_title} 🤗"

            if button.text == "Booked":
                print(f"✓ Already Booked: {class_info}")
                already_booked += 1
                all_classes.append(f"[Booked] {class_info}")

            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked += 1
                all_classes.append(f"[Waitlisted] {class_info}")

            elif button.text == "Book Class":
                button.click()
                print(f"✅ Booked: {class_info}")
                booked += 1
                all_classes.append(f"[New Booking] {class_info}")

            elif button.text == "Join Waitlist":
                button.click()
                print(f"🕓 Joined waitlist for: {class_info}")
                waitlist += 1
                all_classes.append(f"[New Waitlist] {class_info}")

# ------------------------ BOOKING SUMMARY ------------------------
print("\n--- 📋 BOOKING SUMMARY ---")
print(f"Classes booked: {booked}")
print(f"Waitlists joined: {waitlist}")
print(f"Already booked/waitlisted: {already_booked}")
print(f"Total Tuesday & Thursday 6PM classes: {booked + waitlist + already_booked}")

print("\n--- 🧾 DETAILED CLASS LIST ---")
for class_detail in all_classes:
    print(f" • {class_detail}")

total_classes = booked + waitlist + already_booked
# ------------------------ VERIFICATION ------------------------
print("\n🔎 Verifying 'My Bookings' page...")
verification_button = driver.find_element(By.ID, "my-bookings-link")
verification_button.click()
driver.implicitly_wait(2)
verified_count = 0
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*=card-]")

for card in all_cards:
    try:
        day_paragraph = card.find_element(By.XPATH,".//p[strong[text()='When:']]")
        day_text = day_paragraph.text

        # ------------------------ CONDITION ------------------------
        if ("Tue" in day_text or "Thu" in day_text) and "6:00 PM" in day_text:
            class_name = card.find_element(By.TAG_NAME,"h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_classes} bookings")
print(f"Found: {verified_count} bookings")

if total_classes == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_classes - verified_count} bookings")