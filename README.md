# 🧠 **Day 49 – Selenium Automation: Gym Class Booker**  

### 🐍 Project Overview  
This project is part of my **Day 49** in the Python Bootcamp — where I worked with **Selenium WebDriver** to automate a booking process on the mock website [`https://appbrewery.github.io/gym`](https://appbrewery.github.io/gym).  

It automatically:  
1. Logs into the gym website 🏋️  
2. Searches for Tuesday and Thursday **6:00 PM** classes 🕕  
3. Books or joins the waitlist for those classes 📅  
4. Prints a clean booking summary 📋  
5. Verifies bookings on the “My Bookings” page ✅  

---

## ⚙️ **Tech Stack**
- 🐍 **Python 3.x**  
- 🌐 **Selenium WebDriver** (for browser automation)  
- 💻 **Google Chrome** (browser used)  

---

## 🧩 **How the Code Works**

### 1. 🚀 **Launch Chrome Browser**
```python
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
```
- Starts Chrome in normal mode (not headless).  
- Keeps the browser open after script execution.  
- Disables Chrome’s password manager warnings.  

---

### 2. 🔐 **Login Process**
The script goes to the Gym website and clicks the login button.  
It fills in your **email** and **password**, then signs you in automatically.  

```python
email_input.send_keys(email)
password_input.send_keys(password)
submit_button.click()
```

🧠 *Note:* I used a **trial/test account** (`student@test.com`) — not my real one,  
since I couldn’t get Chrome profiles to work even after **3 days** of debugging 😅  
(Chrome profiles + Selenium were trickier than expected, and the official solution code was outdated.)

---

### 3. 📅 **Booking Logic**
Once logged in, the code finds all available classes.  
It looks specifically for:
- **Tuesdays (Tue)**  
- **Thursdays (Thu)**  
- **6:00 PM** slots  

Then it decides whether to:
- ✅ **Book Class**  
- 🕓 **Join Waitlist**  
- Skip if already **Booked** or **Waitlisted**  

All this is logged neatly in the terminal.

---

### 4. 📋 **Booking Summary**
After looping through the classes, the code prints:  
- Total booked classes  
- Total waitlists joined  
- Total already booked/waitlisted classes  
- A detailed list of all affected classes  

Example output:
```
--- 📋 BOOKING SUMMARY ---
Classes booked: 2
Waitlists joined: 1
Already booked/waitlisted: 1
Total Tuesday & Thursday 6PM classes: 4
```

---

### 5. 🔎 **Verification Step**
Finally, it goes to the **"My Bookings"** page and double-checks that all bookings appear correctly.

If everything matches up:
```
✅ SUCCESS: All bookings verified!
```
Otherwise:
```
❌ MISMATCH: Missing X bookings
```

This final check ensures your automation actually did what it was supposed to — and that no class booking silently failed.

---

## 🧠 **What I Learned**
- How to navigate real websites using Selenium’s `find_element()` and `find_elements()` methods.  
- How to handle conditional logic for dynamic content (buttons with text like “Booked”, “Waitlisted”, etc.).  
- The importance of **explicit waits** and **error handling** (especially `NoSuchElementException`).  
- That even AI models and documentation sometimes don’t provide a direct solution — persistence matters! 💪  

I spent **3 days** figuring out Chrome profiles, only to realize the issue was in Selenium’s compatibility layer — but the journey taught me a ton about browser automation and debugging under real constraints.

---

## 💡 **Future Improvements**
1. **🌐 Add Resilience for Network Failures:**  
   - Implement retries and connection checks using `try/except`.  
   - Pause and resume automation if network disconnects temporarily.

2. **🕒 Add Dynamic Waits:**  
   - Replace `implicitly_wait` with Selenium’s `WebDriverWait` for more precise timing.

3. **📁 Chrome Profile Integration (Retry):**  
   - Allow persistent login without typing credentials each time.

4. **📊 Reporting:**  
   - Save booking summary to a `.txt` or `.csv` file for easy tracking.

---


## ❤️ **Final Thoughts**
This day reminded me that **debugging is a skill of patience**.  
Even though the Chrome profile setup didn’t work, completing this project using a test account made me appreciate Selenium’s power even more.  

> “Automation is not just about writing code — it’s about persistence, adaptability, and learning through trial and error.” 🚀  
