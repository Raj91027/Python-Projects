import smtplib

my_email = "sistkcsetechclub@gmail.com"
password = "xzqmcklkmbctqzwg"

with open("email.txt") as email_file:
    all_emails = email_file.readlines()

file_path = "format.txt"
with open(file_path) as letter_file:
    contents = letter_file.read()

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    for i in range(81):
        connection.sendmail(from_addr=my_email,
                            to_addrs=all_emails[i],
                            msg=f"Subject:Technical Club Coding Test\n\n{contents}")