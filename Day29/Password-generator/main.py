from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entries.get()
    email = email_entries.get()
    password = password_entries.get()
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entries.delete(0, END)
        password_entries.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label =  Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="password:")
password_label.grid(row=3, column=0)

#Entries
website_entries = Entry(width=36)
website_entries.grid(row=1, column=1, columnspan=2)
website_entries.focus()
email_entries = Entry(width=36)
email_entries.grid(row=2, column=1, columnspan=2)
email_entries.insert(0, "anurajkumar6294@gmail.com")
password_entries= Entry(width=18)
password_entries.grid(row=3, column=1)

#Buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add",width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()