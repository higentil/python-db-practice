import sqlite3
import re

dbase = sqlite3.connect('contacts.db')
dbase.execute('create table if not exists contacts(name text, qq_number text, phone text, email text)')
cur = dbase.cursor()

def welcome():
    inn = input("\n A: Add a record \n\n D: Delete a record \n\n C: Modify a record \n\n F: Find a record \n\n S: Search for a record\n\n Please enter the letter corresponding to the function:  ")
    return inn.lower()

def check(name):
    cur.execute('select name from contacts where name=?', (name,))
    return cur.fetchone() is not None

def valid_no(name):
    while True:
        phone = input(f"Enter {name}'s phone number: ")
        if len(phone) in (8, 10):
            qq_number = input(f"Enter {name}'s qq_number : ")
            if len(qq_number) in (5, 8):
                email = input(f"Enter {name}'s email : ")
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    return phone, qq_number, email
                print("Email is invalid.")
            else:
                print("QQ number is invalid.")
        else:
            print("Phone number is invalid.")

def delete():
    name = input('Enter the name to be deleted: ').title()
    if check(name):
        cur.execute('delete from contacts where name=?', (name,))
        print("Delete successful")
    else:
        print(f"No contact exist named '{name}'")
    dbase.commit()

def new():
    name = input("Enter new contact name: ").title()
    phone, qq_number, email = valid_no(name)
    cur.execute('insert into contacts (name, qq_number, phone, email) values (?,?,?,?)', (name, qq_number, phone, email))
    print("new contact info added!")
    dbase.commit()

def all():
    cur.execute('select name, qq_number, phone, email from contacts')
    obj = cur.fetchall()
    if not obj:
        print("No contact exist!")
        return
    for idx, a in enumerate(obj, 1):
        print(f'\t No. {idx} \t Name: {a[0]} \t QQ: {a[1]} \t Phone: {a[2]} \t E-mail: {a[3]}')
    dbase.commit()

def update_name():
    n = input("Enter the contact phone number to be modified: ")
    name = input("Enter the new contact name: ").title()
    cur.execute('select name from contacts where phone=?', (n,))
    if cur.fetchone():
        cur.execute('update contacts set name=? where phone=?', (name, n))
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()

def update_qq():
    n = input("Enter the contact phone number to be modified: ")
    qq_number = input("Enter the new qq_number: ")
    cur.execute('select name from contacts where phone=?', (n,))
    if cur.fetchone():
        cur.execute('update contacts set qq_number=? where phone=?', (qq_number, n))
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()

def update_phone():
    n = input("Enter the contact phone number to be modified: ")
    new_phone = input("Enter the new phone number: ")
    cur.execute('select name from contacts where phone=?', (n,))
    if cur.fetchone():
        cur.execute('update contacts set phone=? where phone=?', (new_phone, n))
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()

def update_mail():
    n = input("Enter the contact phone number to be modified: ")
    email = input("Enter the new email: ")
    cur.execute('select name from contacts where phone=?', (n,))
    if cur.fetchone():
        cur.execute('update contacts set email=? where phone=?', (email, n))
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()

def search_field(field_name, prompt):
    val = input(prompt)
    cur.execute(f'select name, qq_number, phone, email from contacts where {field_name} like ?', (f'%{val}%',))
    results = cur.fetchall()
    if results:
        for obj in results:
            print(f"\nMatch found:\n\t Name: {obj[0]} \t QQ: {obj[1]} \t Phone: {obj[2]} \t E-mail: {obj[3]}")
    else:
        print(f"No contact matching that criteria found.")
    dbase.commit()

print(" ############################### NKCS INFOSystem V0.1 ############################### \n ====================================================================== Powered by Zodiac==")
while True:
    inn = welcome()
    if inn == 'a':
        new()
    elif inn == 'f':
        all()
    elif inn == 'c':
        while True:
            i = input("Choose an option to modify contact information: \n n: name \n q: qq_number \n p: phone \n m: email \n: ")
            if i == 'n':
                update_name()
                break
            elif i == 'q':
                update_qq()
                break
            elif i == 'p':
                update_phone()
                break
            elif i == 'm':
                update_mail()
                break
            else:
                print("Please enter a valid letter options.")
    elif inn == 's':
        while True:
            i = input("Choose an option to search contact information: \n n: name \n q: qq_number \n p: phone \n m: email \n: ")
            if i == 'n':
                search_field('name', "Enter the contact name to be searched: ")
                break
            elif i == 'q':
                search_field('qq_number', "Enter the contact qq_number to be searched: ")
                break
            elif i == 'p':
                search_field('phone', "Enter the contact phone number to be searched: ")
                break
            elif i == 'm':
                search_field('email', "Enter the contact email to be searched: ")
                break
            else:
                print("Please enter a valid letter option.")
    elif inn == 'd':
        delete()
    elif inn == 'exit':
        print('DONE!!')
        break
    else:
        print("Please enter the letter corresponding to the function.")

dbase.close()
