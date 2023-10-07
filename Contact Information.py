#Contact Information: Store name, phone number, email, and address for each contact.
#Add Contact: Allow users to add new contacts with their details.
#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.
#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.
#User Interface: Design a user-friendly interface for easy interaction.
import csv
def AddContact():
    file = open('Contacts.csv','a')
    rec = csv.writer(file)
    while True:
        name = input('Enter The NAME: ')
        phno = int(input('Enter The PHONE NUMBER : '))
        email = input('Enter The EMAIL: ')
        address = input('Enter The ADDRESS: ')
        lst=[name,phno,email,address]
        rec.writerow(lst)
        ask = input('Do You Want To Add More (y/n): ')
        if ask.lower()=='n':
            break
def DisplayContact():
    file = open('Contacts.csv','r')
    rec = csv.reader(file)
    print('-'*86)
    print('| CONTACT NAME | PHONE NUMBER | CONTACTS E-MAIL ADDRESS | CONTACT ADDRESS (LOCATION) |')
    print('-'*86)
    for i in rec:
        print('|',i[0],' '*(11-len(i[0])),'|',i[1],' '*(11-len(i[1])),'|',i[2],' '*(22-len(i[2])),
              '|',i[3],' '*(25-len(i[3])),'|')
        print('-'*86)
def SearchContact():
    file = open('Contacts.csv','r')
    rec = csv.reader(file)
    ask = input('Enter 1 for searching by Name or 2 for searching by Phone Number: ')
    if ask == '1':
        name = input('Enter The Name: ')
        count = 0
        for i in rec:
            if i[0].lower() == name.lower():
                print('CONTACT NAME: ',i[0].upper())
                print('PHONE NUMBER: ',i[1])
                print('E-MAIL ADDRESS: ',i[2])
                print('ADDRESS: ',i[3].upper())
                count+=1
                break
            else:
                print('No Record Found!')
                
            
    elif ask == '2':
        phno = int(input('Enter The Phone Number: '))
        for i in rec:
            if i[1] == phno:
                print('CONTACT NAME: ',i[0].upper())
                print('PHONE NUMBER: ',i[1])
                print('E-MAIL ADDRESS: ',i[2])
                print('ADDRESS: ',i[3].upper())
                break
            else:
                print('No Record Found!')
                break
    else:
        print('Wrong Command!')
def UpdateContact():
    file = open('Contacts.csv','r+',newline='')
    rec = csv.reader(file)
    templist = list(rec)
    phno =input('Enter the Phone Number: ')
    count=len(templist)
    for i in templist:
        if i[1] == phno:
            count-=1
            ask =int(input('''Enter 1 to edit the Name
Enter 2 to edit the Phone Number
Enter 3 to edit the E-Mail Address
Enter 4 to edit the Address
*** Enter Your Choice *** : '''))
            if ask == 1:
                for i in templist:
                    if i[1]==phno:
                        new = input('Enter The New Name: ')
                        i[0] = new
                        print(i)
                        print('Updated')
                        file.seek(0)
                        file.truncate()
                        wr= csv.writer(file)
                        wr.writerows(templist)
                    else:
                        print('Wrong Input')

            elif ask == 2:
                for i in templist:
                    if phno == i[1]:
                        new = int(input('Enter The New Phone Number: '))
                        i[1] = new
                        print('Updated')
                        file.seek(0)
                        file.truncate()
                        wr = csv.writer(file)
                        wr.writerows(templist)
                    else:
                        print('Wrong Input')

            elif ask == 3:
                for i in templist:
                    if phno == i[1]:
                        new = input('Enter The New E-Mail: ')
                        i[2] = new
                        print('Updated')
                        file.seek(0)
                        file.truncate()
                        wr = csv.writer(file)
                        wr.writerows(templist)
                    else:
                        print('Wrong Input')

            elif ask == 4:
                for i in templist:
                    if phno == i[1]:
                        new = input('Enter The New Address: ')
                        i[3] = new
                        print('Updated')
                        file.seek(0)
                        file.truncate()
                        wr = csv.writer(file)
                        wr.writerows(templist)
                    else:
                        print('Wrong Input')
            else:
                print('Wrong Input')
            
        else:
            if count == 0:
                print('No Contacts Found')
            
def DeleteContact():
    file = open('Contacts.csv','r+',newline='')
    rec = csv.reader(file)
    temp_file = list(rec)
    phno =input('Enter the Phone Number To Delete: ')
    for i in temp_file:
        if i[1] == phno:
            temp_file.remove(i)
            print('Deleted Successfully')
            file.seek(0)
            file.truncate()
            wr = csv.writer(file)
            wr.writerows(temp_file)
            break
        else:
            print('No Record Found')
            break
def MainMenu():
    while True:
        ask = int(input('''Enter 1 for Add Contact
Enter 2 for Display Contact
Enter 3 for Search Contact
Enter 4 for Update Contact
Enter 5 for Delete Contact
Enter Your Choice: '''))
        if ask == 1:
            AddContact()
        elif ask == 2:
            DisplayContact()
        elif ask == 3:
            SearchContact()
        elif ask == 4:
            UpdateContact()
        elif ask == 5:
            DeleteContact()
        x = input('Do You Want To Continue(y/n): ')
        if x.lower() == 'n':
            print('Thank You')
            break
MainMenu()
