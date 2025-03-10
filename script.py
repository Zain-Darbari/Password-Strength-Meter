import re
import random
import string
import streamlit as st

def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))

# Common weak passwords to reject
BLACKLISTED_PASSWORDS = {"password", "123456", "qwerty", "password123", "letmein", "abc123"}

def check_password_strength(password):
    score = 0
    feedback = []
    
    if password in BLACKLISTED_PASSWORDS:
        return "❌ This password is too common. Choose a more secure one."
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        return "✅ Strong Password!"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.\n" + "\n".join(feedback)
    else:
        return "❌ Weak Password - Improve it using the suggestions below.\n" + "\n".join(feedback)

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    result = check_password_strength(password)
    st.markdown(result)

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"🔹 Suggested Strong Password: `{strong_password}`")
