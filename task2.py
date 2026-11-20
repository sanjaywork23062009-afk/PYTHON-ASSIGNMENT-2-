correct_otp = "1234"

print("--- While Loop Implementation ---")
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    user_input = input("Enter OTP (or leave blank): ")
    if user_input == "":
        pass
        print("Blank entry. Does not count as an attempt.")
        continue
    
    attempts += 1
    if user_input == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print(f"Incorrect OTP. Attempt {attempts} of {max_attempts}.")
else:
    print("Account locked for 30 minutes due to 3 failed attempts.")

print("\n--- For Loop Implementation ---")
attempts_count = 0
for i in range(3):
    user_input = input("Enter OTP (or leave blank): ")
    if user_input == "":
        pass
        print("Blank entry. Does not count as an attempt.")
        # To handle blank entries without wasting a loop iteration in a for-range,
        # we can adjust or use a while loop, but here is standard demonstration:
        continue
    
    attempts_count += 1
    if user_input == correct_otp:
        print("OTP verified successfully!")
        break
    else:
        print("Incorrect OTP.")
else:
    if attempts_count >= 3:
        print("Account locked for 30 minutes due to 3 failed attempts.")
