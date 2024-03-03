import random
import smtplib
import threading
from customtkinter import *

# generate a random 6-digit OTP
def generate_otp():
    otp = random.randint(100000, 999999)
    return str(otp)

#  send OTP via email
def send_otp_email_thread(email, otp):
    try:
        smtp_server = 'smtp.gmail.com'  
        smtp_port = 587 
        #The sender email and password are supposed to be stored in env file when working on a production environment
        sender_email = 'taskintern2@gmail.com'    
        sender_password = 'ccuv ctay aegb tjdc' 

        message = f"Your OTP is: {otp}"
        subject = "OTP Verification"

        # Connect to the SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Compose and send the email
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(sender_email, email, email_message)

        # Close the connection
        server.quit()
        messagebox("OTP Sent", "OTP sent successfully to your email!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


# send OTP via email
def send_otp_email(email, otp):
    email_thread = threading.Thread(target=send_otp_email_thread, args=(email, otp))
    email_thread.start()


# verify OTP
def verify_otp():
    user_otp = otp_entry.get()
    if user_otp == current_otp:
        messagebox("OTP Verification", "OTP is valid. You are verified!")
    else:
        messagebox("OTP Verification", "Invalid OTP. Please try again.")
        
# Function to resend OTP
def resend_otp():
    global current_otp
    current_otp = generate_otp()
    email = email_entry.get()
    if send_otp_email(email, current_otp):
        messagebox("Resend OTP", "New OTP sent successfully!")
    else:
        messagebox("Resend OTP", "Failed to resend OTP. Please try again.")
        
def messagebox(title,messasge):
    toplevel = CTkToplevel(app) # Create a new window
    toplevel.geometry("300x100")   
    toplevel.attributes('-topmost', 'true')
    toplevel.title(title)
    CTkLabel(toplevel, text=messasge).pack(padx=10, pady=10)
    CTkButton(toplevel, text="OK", command=toplevel.destroy, width=10, fg_color="blue").pack(padx=10, pady=10)
    toplevel.focus()
    
        
app = CTk()
app.geometry("550x200")
title_label = CTkLabel(app, text="OTP Verification")
label = CTkLabel(app, text="Enter OTP:")
otp_entry = CTkEntry(app, width=80) 
verify_button = CTkButton(app, text="Verify OTP", command=verify_otp, width=10, fg_color="green") 
email_label = CTkLabel(app, text="Enter your email:")
email_entry = CTkEntry(app, width=250)
send_email_button = CTkButton(app, text="Send OTP", command=lambda: send_otp_email(email_entry.get(), current_otp), width=10, fg_color="blue")  # Added background color
resend_button = CTkButton(app, text="Resend OTP", command=resend_otp, width=10, fg_color="red")
 







title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=5)
email_label.grid(row=1, column=0, padx=10, pady=15)
email_entry.grid(row=1, column=1, padx=10, pady=15)
send_email_button.grid(row=1, column=2, padx=10, pady=5)
label.grid(row=2, column=0, padx=10, pady=5)
otp_entry.grid(row=2, column=1,padx=10 , pady=5,)
verify_button.grid(row=2, column=2, padx=10, pady=5)
resend_button.grid(row=3, column=1, padx=10, pady=5)


# Generate a random OTP when the program starts
current_otp = generate_otp()

#  Tkinter main loop
app.mainloop()
