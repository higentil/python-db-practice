import sqlite3
import re
dbase = sqlite3.connect('contacts.db')
dbase.execute('create table if not exists' +
              ' contacts(name text, qq_number text, phone text, email text)')
cur=dbase.cursor()

def welcome():
    inn = input("\n A: Add a record \n\n D: Delete a record \n\n C: Modify a record \n\n F: Find a record \n\n S: Search for a record\n\n Please enter the letter corresponding to the fucntion:  ")
    return inn.lower()
def check(name):
    cur.execute(f'select name from contacts where name="{name}"')
    obj = cur.fetchone()
    if obj:
        return True
    else:
        return False
def valid_no(name):

    while True:
        phone = input(f"Enter {name}'s phone number: ")
        if len(phone) == 10 or len(phone) == 8:
            qq_number = input(f"Enter {name}'s qq_number : ")
            if len(qq_number) == 8 or len(qq_number) == 5:
                email = input(f"Enter {name}'s email : ")
                if re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    return phone, qq_number, email
                else:
                    print("Email is invalid.")
            else:
                print("QQ number is invalid.")
        else:
            print("Phone number is invalid.")
        

def delete():
    name = input('Enter the name to be deleted: ')
    name = name.title()
    if check(name):
        cur.execute(f"delete from contacts where name='{name}'")
        print("Delete successful")
    else:
        print(f"No contact exist named '{name}'")
    dbase.commit()
def new():
    name = input("Enter new contact name: ")
    name = name.title()
    phone, qq_number, email = valid_no(name)

    cur.execute('insert into contacts (name, qq_number, phone, email) values (?,?,?,?)',
            (f'{name}', f'{qq_number}', f'{phone}', f'{email}'))

    
    print("new contact info added!")
    dbase.commit()



def all():
    cur.execute('select * from contacts')
    obj = cur.fetchall()
    if obj==None:
        print("No contact exist!")
    for a in obj:
        print('\t No. ', a[0], ' \t Name: ', a[1], '\t QQ: ', a[2], '\t Phone: ', a[3], '\t E-mail: ', a[4])
    dbase.commit()


def update_name():
    n = input("Enter the contact number to be modified: ")
    name = input("Enter the new contact name: ")
    cur.execute(f'select name from contacts where phone="{n}"')
    obj=cur.fetchone()
    if obj:
        cur.execute(f'update contacts set name="{name.title()}" where phone="{n}"')
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()

def update_qq():
    n = input("Enter the contact number to be modified: ")
    qq_number = input("Enter the new qq_number: ")
    cur.execute(f'select * from contacts where phone="{n}"')
    obj=cur.fetchone()
    if obj:
        cur.execute(f'update contacts set qq_number="{qq_number}" where phone="{n}"')
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()

def update_phone():
    n = input("Enter the contact number to be modified: ")
    qq_number = input("Enter the new phone: ")
    cur.execute(f'select * from contacts where phone="{n}"')
    obj=cur.fetchone()
    if obj:
        cur.execute(f'update contacts set phone="{phone}" where phone="{n}"')
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()

def update_mail():
    n = input("Enter the contact number to be modified: ")
    email = input("Enter the new email: ")
    cur.execute(f'select * from contacts where phone="{n}"')
    obj=cur.fetchone()
    if obj:
        cur.execute(f'update contacts set email="{email}" where phone="{n}"')
        print("update successful")
    else:
        print(f"No contact exist which has number: {n}")
    dbase.commit()


def search_phone():
    phone = input("Enter the contact phone number to be searched: ")
    cur.execute(f'select name from contacts where phone like "%{phone}%"')
    obj=cur.fetchone()
    if obj:
        obj = obj[0]
        print("name: ",obj)
        cur.execute(f'select name,qq_number,email from contacts where name="{obj}"')
        obj=cur.fetchone()
        print("contacts: \n",'\t Name: ', obj[0], '\t QQ: ', obj[1], '\t E-mail: ', obj[2])
    else:
        print(f"No contact exist which has number: {phone}")
    dbase.commit()

def search_name():
    name = input("Enter the contact name to be searched: ")
    cur.execute(f'select name from contacts where name like "%{name}%"')
    obj=cur.fetchone()
    if obj:
        obj = obj[0]
        print("name: ",obj)
        cur.execute(f'select qq_number,phone,email from contacts where name="{obj}"')
        obj=cur.fetchone()
        print("contacts: \n",'\t QQ: ', obj[0], ' \t Phone: ', obj[1], ' \t E-mail: ', obj[2])
    else:
        print(f"No contact exist which named: {name}")
    dbase.commit()

def search_qq():
    qq_number = input("Enter the contact qq_number to be searched: ")
    cur.execute(f'select name from contacts where qq_number like "%{qq_number}%"')
    obj=cur.fetchone()
    if obj:
        obj = obj[0]
        print("name: ",obj)
        cur.execute(f'select name,phone,email from contacts where name="{obj}"')
        obj=cur.fetchone()
        print("contacts: \n",'\t Name: ', obj[0], ' \t Phone: ', obj[1], ' \t E-mail: ', obj[2])
    else:
        print(f"No contact exist which named: {qq_number}")
    dbase.commit()

def search_email():
    email = input("Enter the contact email to be searched: ")
    cur.execute(f'select name from contacts where email like "%{email}%"')
    obj=cur.fetchone()
    if obj:
        obj = obj[0]
        print("name: ",obj)
        cur.execute(f'select name,qq_number,phone from contacts where name="{obj}"')
        obj=cur.fetchone()
        print("contacts: \n",'\t Name: ', obj[0], ' \t QQ: ', obj[1], ' \t Phone: ', obj[2])
    else:
        print(f"No contact exist which named: {email}")
    dbase.commit()

print(" ############################### NKCS INFOSystem V0.1 ############################### \n ====================================================================== Powered by Zodiac==")
while(True):
    inn = welcome()
    if inn=='a':
        new()
    elif inn=='f':
        all()
    elif inn=='c':
        while True:
            i = input("Choose an option to modify contact information: \n n: name \n q: qq_number \n p: phone \n m: email \n: ")
            if i=='n':
                update_name()
                break
            elif i=='q':
                update_qq()
                break
            elif i=='p':
                update_phone()
                break
            elif i =='m':
                update_mail()    
            else:
                print("Please enter the letter corresponding to the fucntion: ")
    elif inn=='s':
        while True:
            i = input("Choose an option to search contact information: \n n: name \n q: qq_number \n p: phone \n m: email \n: ")
            if i=='n':
                search_name()
                break
            elif i=='q':
               search_qq()
               break
            elif i=='p':
                search_phone()
                break
            elif i =='m':
                search_email()
            else:
                print("Please enter the letter corresponding to the fucntion: ")
    elif inn=='d':
        delete()
    elif inn=='exit':
        print('DONE!!')
        break
    else:
        print("Please enter the letter corresponding to the fucntion: ")

dbase.close()



