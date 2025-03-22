#### Python Tkinter Import Statement ####
from codecs import register
import json,random
import tkinter as tk
import tkinter
from tkinter.constants import COMMAND, N     
import tkinter.ttk as ttk  
from tkinter import Entry, Grid, Label, Text, messagebox

def raise_frame(frame):
    frame.tkraise()
    
#### Setup Main Application Window ####
root = tk.Tk()            
root.title('Bookshop System')  
root.geometry('500x500')

### Frames ###
login_frame = tk.Frame(root) ### log in frame
login_frame.place(x=0, y=0, width=500, height=500)

register_frame = tk.Frame(root) ## Have you registered?
register_frame.place(x=0, y=0, width=500, height=500)

buyer_frame = tk.Frame(root) ### USER FRAME
buyer_frame.place(x=0, y=0, width=500, height=500)

admin_frame = tk.Frame(root) ### ADMIN FRAME
admin_frame.place(x=0, y=0, width=500, height=500)

change_pasword_frame= tk.Frame(root) ## change frame
change_pasword_frame.place(x=0, y=0, width=500, height=500)

createbook_frame= tk.Frame(root) ## create book frame
createbook_frame.place(x=0, y=0, width=500, height=500)

updatebook_frame= tk.Frame(root) ## update book frame
updatebook_frame.place(x=0, y=0, width=550, height=500)

updatebook2_frame= tk.Frame(root) ## update book frame
updatebook2_frame.place(x=0, y=0, width=550, height=500)

searchbook_frame= tk.Frame(root) ## search book frame
searchbook_frame.place(x=0, y=0, width=500, height=500)

shopbook_frame= tk.Frame(root) ## search book frame
shopbook_frame.place(x=0, y=0, width=500, height=500)

shoppingcart_frame= tk.Frame(root) ## shopping cart frame
shoppingcart_frame.place(x=0, y=0, width=500, height=500)

delete_book_frame= tk.Frame(root) ## delete book frame
delete_book_frame.place(x=0, y=0, width=500, height=500)

view_cart_frame = tk.Frame(root) ### View cart
view_cart_frame.place(x=0, y=0, width=500, height=500)

paid_books_frame=tk.Frame(root) ## View paid books( Admin )
paid_books_frame.place(x=0, y=0, width=500, height=500)

Main_frame = tk.Frame(root) ## have you register
Main_frame.place(x=0, y=0, width=500, height=500)


####  check user registered frame #####
#### UI Widgets###
lbl_title = ttk.Label(Main_frame, text='Welcome to Bookshop System') 
lbl_res = ttk.Label(Main_frame, text='Have you register with us?')
btn_yes = ttk.Button(Main_frame, text='Yes', command=lambda m='Yes' : [confirm(m), raise_frame(login_frame)])
btn_no = ttk.Button(Main_frame, text='No', command=lambda m='No' : [confirm(m), raise_frame(register_frame)])
### UI Layouts ####
lbl_title.grid(row=0, column=1, columnspan=3)                
lbl_res.grid(row=1, column=1, columnspan=2)
btn_yes.grid(row=2, column=1)
btn_no.grid(row=2, column=2)



#### Login Frame ###
#### UI Widgets###
btn_return_3 = ttk.Button(login_frame, text='Back', command=lambda : raise_frame(Main_frame))
lbl_title = ttk.Label(login_frame, text='Bookshop System\'s Login')     
lbl_username = ttk.Label(login_frame, text = 'Username: ')
lbl_password = ttk.Label(login_frame, text = 'Password: ')
login_username = ttk.Entry(login_frame)
login_password = ttk.Entry(login_frame, show="*")
btn_login = ttk.Button(login_frame, text = 'Login',command=lambda:verify_user())
### UI Layouts ####
lbl_title.grid(row=0, column=0, columnspan=2)               
lbl_username.grid(row=1, column=0)
login_username.grid(row=1, column=1)
lbl_password.grid(row=2, column=0)
login_password.grid(row=2, column=1)
btn_login.grid(row=4, column=1)
btn_return_3.grid(row=4, column=0)
#### input admin_or_user access Third frame###
options = ['Admin', 'Buyer']
accesslogin = tkinter.StringVar(login_frame)
accesslogin.set('Select access type')
access_menulogin = tkinter.OptionMenu(login_frame, accesslogin, *options)
access_menulogin.grid(row=3, column= 1, columnspan=2) 


### Register Frame ####
#### input admin_or_user access forth frame###
option = ['Admin', 'Buyer']
access = tkinter.StringVar(register_frame)
access.set('Select access type')
access_menu = tkinter.OptionMenu(register_frame, access, *option)
access_menu.grid(row=3, column= 1, columnspan=2)
#### UI Widgets###
btn_return = ttk.Button(register_frame, text='Back', command=lambda : raise_frame(Main_frame))
lbl_title = ttk.Label(register_frame, text='Bookshop System\'s Registration')     
lbl_username = ttk.Label(register_frame, text = 'Username: ')
lbl_password = ttk.Label(register_frame, text = 'Password: ')
ent_username = ttk.Entry(register_frame)
ent_password = ttk.Entry(register_frame, show="*")
btn_res = ttk.Button(register_frame, text = 'Register', command=lambda : Register())
### UI Layouts ####
lbl_title.grid(row=0, column=0, columnspan=2)                
lbl_username.grid(row=1, column=0)
ent_username.grid(row=1, column=1)
lbl_password.grid(row=2, column=0)
ent_password.grid(row=2, column=1)
btn_res.grid(row=4, column=1)
btn_return.grid(row=4, column=0)

### JSON ###
#Read from json file 
with open('Book_list.json','r') as user_account:
    booklist=json.load(user_account)
with open('User_account.json','r') as user_account:
    db_user_account=json.load(user_account)
with open('Shopping_cart.json', 'r') as user_account:
    shopping_cart=json.load(user_account)
with open('Paid_books.json') as user_account:
    paid_books=json.load(user_account)

def write_to_json():
    with open('Book_list.json','w') as user_account:
        json.dump(booklist,user_account,indent=4)
    with open('User_account.json','w') as user_account:
        json.dump(db_user_account,user_account,indent=4)
    with open('Shopping_cart.json','w') as user_account:
        json.dump(shopping_cart,user_account,indent=4)
    with open('Paid_books.json','w') as user_account:
        json.dump(paid_books,user_account,indent=4)


currentuser={}
currentbook={'title':2,'category':2,'price':2,'date':2,'quantity':2}

#### UI Behaviours ####
class Bookshop_users:
    def __init__(self,username,password,access):
        self.username=username
        self.password=password
        self.access=access
        
class Books:
    def __init__(self,id,title,category,date,price,quantity):
        self.id=id
        self.title=title
        self.category=category
        self.date=date
        self.price=price
        self.quantity=quantity

### COMMAND FOR REGISTER AND LOG IN FRAME ###
### DELETE ENTRY INPUT ###
def cleartext():
    ent_password.delete("0","end")
    ent_username.delete("0","end")
    login_username.delete("0","end")
    login_password.delete("0","end")
    accesslogin.set('Select access type')
    access.set('Select access type')
    admin_do_what2.set('Account Setting')
    admin_do_what.set('Administrator Module')
    buyer_do_what.set('Buyer Module')
    buyer_do_what2.set('Account Setting')
    ent_booktitle.delete("0","end")
    ent_category.delete("0","end")
    ent_date.delete("0","end")
    ent_price.delete("0","end")
    ent_quan.delete("0","end")

def identity(admin_or_buyer):
    print(admin_or_buyer)

def confirm(yes_or_no):
    print(yes_or_no)

# UPDATE NEW USER / ADMIN #
### LOG IN VERIFY & UPDATE ###
def verify_user():
    input_username = login_username.get()  
    input_password = login_password.get()
    input_accces=accesslogin.get()

    #### Run through the dictionary list
    found_user = False
    for account in db_user_account:
        if input_username == account['username']and input_password == account['password'] and input_accces==account['access']:
            
            a={'users':input_username,'password':input_password,'access':input_accces}
            currentuser.update(a)
            found_user = True
            
            if accesslogin.get()=='Buyer':
                user_value = accesslogin.get()
                if user_value == account['access']:
                    raise_frame(buyer_frame)
            elif accesslogin.get()=='Admin':
                admin_value =accesslogin.get()
                if admin_value == account['access']:
                    raise_frame(admin_frame)    
            cleartext()
            break      
    else:
        msg = f'You entered the wrong username, password or access type. Please try again.'
        messagebox.showinfo(title='Please try again',message=msg)
        cleartext()

#### REGISTER VERIFY & UPDATE ###
def Register():
    a=ent_username.get()
    b=ent_password.get()
    c=access.get()
    if c!='Select access type' : 
        if a not in db_user_account and str(a).strip() and str(b).strip(): 
            msg = f'You entered username: {ent_username.get()}. You\'re an {access.get()} '
            messagebox.showinfo(title='New account created',message=msg)

            update={'users':ent_username.get(),'password':ent_password.get(),'access':access.get()}
            currentuser.update(update)
            db_user_account.append(vars(Bookshop_users(ent_username.get(),ent_password.get(),access.get())))
            write_to_json()

            for account in db_user_account:
                if access.get()=='Buyer':
                    user_value = access.get()
                    if user_value == account['access']:
                        raise_frame(buyer_frame)
                elif access.get()=='Admin':
                    admin_value =access.get()
                    if admin_value == account['access']:
                        raise_frame(admin_frame)
        else:
            empty=f'Please enter a valid username or password'
            messagebox.showinfo(title='Invalid password or username',message=empty)
    else:
        wrongacces='Please choose access type'
        messagebox.showinfo(title='Invalid access type',message=wrongacces)
    cleartext()
    
### DELETE ACCOUNT COMMAND ####
def delete_acc():
    user=currentuser['users']
    index=-1
    for i in range(len(db_user_account)):
        if db_user_account[i]['username']==user:
            index=i
            break
    if index == -1:
        raise_frame(Main_frame)
    else:
        delete = tk.messagebox.askquestion('Delete Account','Are you sure you want to delete your account',icon = 'warning')
        if delete == 'yes':
            db_user_account.pop(index)
            write_to_json()
            raise_frame(Main_frame)

#### LOGOUT COMMAND ####
def logout():
    logoff = tk.messagebox.askquestion('Logout','Are you sure you want to logout from your account',icon = 'warning')
    if logoff == 'yes':
        raise_frame(Main_frame)
        currentuser.clear

#### CHANGE PASSWORD COMMAND###
def update_pass():
    new=ent_new.get()
    oldpass=currentuser['password']
    index=-1
    
    for i in range(len(db_user_account)):
        if db_user_account[i]['password']==oldpass:
            index=i
            break
    if index == -1:
        msg = f'{oldpass} not found!'
        messagebox.showinfo(title=f'Error',message=msg)
        raise_frame(Main_frame)
    elif str(new).strip():
        change = tk.messagebox.askquestion('Change password',
        'Are you sure you want to change your password',icon = 'warning')
        if change == 'yes':
            db_user_account[index]['password']=new
            write_to_json()
            password_changed = f"Password for {currentuser['users']} has been changed"
            messagebox.showinfo(title=f'Password Succesfuly changed',message=password_changed)
        else:
            return_to_menu()
    else:
        invalid_password = f'Invalid password input'
        messagebox.showinfo(title=f'Error',message=invalid_password)
    cleartext()

### ADMIN MODULE COMMAND ###
#### CREATE BOOK RECORD ADMIN ###
def Create_book_record():
    
    b=ent_booktitle.get()
    if b not in booklist and  str(b).strip():
        for books in booklist:
            index_list=[]
            index_list.append(books['id'])
            new_index=1
            while new_index in index_list:
                new_index=random.randint(0,99999)

        msg = f'You created a new book entitled {b}'
        messagebox.showinfo(title='Book record updated',message=msg)
        booklist.append(vars(Books(str(new_index),
        ent_booktitle.get(),ent_category.get(),
        ent_date.get(),ent_price.get(),
        ent_quan.get())))
        write_to_json()
        cleartext()
        return_to_menu()
        
## Search books by title
def Search_book_by_titles(entrybook):
    book=entrybook;clear_frame(searchbook_frame)
    index=-1
    
    for i in range(len(booklist)):
        if booklist[i]['title']==book:
            index=i
            break
    if index == -1:
        msg = f' not found!'
        messagebox.showinfo(title=f'Error',message=msg)
    else:
        show_properties=ttk.Label(searchbook_frame,text='--- Book searched properties ---')
        show_title=ttk.Label(searchbook_frame, text=f"Title : {booklist[index]['title']}")
        show_id=ttk.Label(searchbook_frame, text=f"Book ID : {booklist[index]['id']}")
        show_category=ttk.Label(searchbook_frame, text=f"Category : {booklist[index]['category']}")
        show_price=ttk.Label(searchbook_frame, text=f"Price : {booklist[index]['price']}")
        show_year=ttk.Label(searchbook_frame, text=f"Year Published : {booklist[index]['date']}")
        show_properties.grid(row=6,column=0,columnspan=2)
        show_title.grid(row=7,column=0)
        show_id.grid(row=7,column=1)
        show_category.grid(row=8,column=0)
        show_price.grid(row=8,column=1)
        show_year.grid(row=9,column=0)
    searchbook()
    cleartext()

### Update book Command ####
def Update_book_record():
    a=currentbook['title']
    index=-1
    for i in range(len(booklist)):
        if booklist[i]['title']==a:
            index=i
            break
    if index == -1:
        msg = f'not found!'
        messagebox.showinfo(title=f'Error',message=msg)

    else:
        update_book = tk.messagebox.askquestion(f'Update book properties',
        'Are you sure you want to proceed?',
        icon = 'warning')
    if update_book == 'yes':
        booklist[index]['title']=entry2_newbooktitle.get()
        booklist[index]['category']=entry2_category.get()
        booklist[index]['date']=entry2_date.get()
        booklist[index]['price']=entry2_price.get()
        booklist[index]['quantity']=entry2_quan.get()
        write_to_json()
        return_to_menu()
        cleartext()

def Delete_book_record():
    a=del_entry.get()
    index=-1
    for i in range(len(booklist)):
        if booklist[i]['title']==a:
            index=i
            break
    if index == -1:
        msg = f'{a} not found!'
        messagebox.showinfo(title=f'Error',message=msg)
    else:
        delete_book = tk.messagebox.askquestion('Delete Book',
        'Are you sure you want to delete this book? ',icon = 'warning')

        if delete_book == 'yes':
            booklist.pop(index)
            write_to_json()
            return_to_menu()
    cleartext()

### BUYER MODULE ##
def find_book_index(new_book,cart_book_list):
		index_book=-1
		new_book_lowercase=str(new_book).lower()
		for i in range(len(cart_book_list)):
			if new_book_lowercase==cart_book_list[i]['title'].lower():
				index_book=i
				break
		
		return index_book

def get_buyer_list(list_book):
    list_buyer=[]
    for i in range(len(list_book)):
        a=list_book[i]['buyer']
        for key in a.keys():
            list_buyer.append(key)

    return list_buyer

def find_buyer_index(buyer,list_book):
    index_user=-1
    listbuyer=get_buyer_list(list_book)

    for items in listbuyer:
            if buyer==items:
                index_user=listbuyer.index(buyer)
                break
                
    return index_user

def Add_to_cart(book):
    # index=-1
    buyer=currentuser['users']
    index_user=find_buyer_index(buyer,shopping_cart)
     
    if index_user==-1:
        b_list={'buyer':{buyer:{'booklist':[{'title':book['title'],"price":book['price'],'quantity':1}]}}}
        shopping_cart.append(b_list)            
        
    else:
        index_book=find_book_index(book['title'],shopping_cart[index_user]['buyer'][buyer]['booklist'])
        if index_book==-1:
            dict_book={"title":book['title'],"price":book['price'],"quantity":1}
            shopping_cart[index_user]['buyer'][buyer]['booklist'].append(dict_book)
            
        else:
            for i in range(len(booklist)):
                if booklist[i]['title']==book['title']:
                    index=i
            s_quantity=int(shopping_cart[index_user]['buyer'][buyer]['booklist'][index_book]['quantity'])
            n_quantity=int(booklist[index]['quantity'])
            if s_quantity==n_quantity:
                exceed_quantity = f'Exceeding available stock'
                messagebox.showinfo(title=f'Cannot Add to cart',message=exceed_quantity)
            else:
                ### buyer can't buy book exceeded then stock (quantity available)
                shopping_cart[index_user]['buyer'][buyer]['booklist'][index_book]['quantity']+=1
    shoppingbook()             
    write_to_json()

def delete_book(del_book):
    buyer=currentuser['users']
    for i in range(len(shopping_cart)):
        indexuser=find_buyer_index(buyer,shopping_cart)
        indexbook=find_book_index(del_book['title'],shopping_cart[indexuser]['buyer'][buyer]['booklist'])
        if indexuser!=-1:
            quantity_in_cart=shopping_cart[indexuser]['buyer'][buyer]['booklist'][indexbook]['quantity']
            if quantity_in_cart-1>0:
                shopping_cart[indexuser]['buyer'][buyer]['booklist'][indexbook]['quantity']-=1
                break
            elif shopping_cart[indexuser]['buyer'][buyer]['booklist']==[]:
                return_to_menu()
            else:
                ### remove book if book quantity == 0
                updated_booklist=shopping_cart[indexuser]['buyer'][buyer]['booklist']
                updated_booklist.pop(indexbook)
                break
    write_to_json()
    view_books(buyer,shopping_cart,view_cart_frame)            
    
    
def clear_frame(current_frame):
    for widget in current_frame.winfo_children():
        widget.destroy()

## Paid Books
def update_to_booklist(book):

    index_current_book=-1
    for i in range(len(booklist)):
        if booklist[i]['title']==book['title']:
            index_current_book=i
            break
    quantity_total=int(booklist[index_current_book]['quantity'])-int(book['quantity'])
    if quantity_total==0:
        booklist.pop(index_current_book)
    else:

        booklist[index_current_book]['quantity']=str(quantity_total)
        
    write_to_json()
    cleartext()

def Book_Payment():

    buyer=currentuser['users']
    index_cart=find_buyer_index(buyer,shopping_cart)
    shopping_cart_booklist=shopping_cart[index_cart]["buyer"][buyer]['booklist']
    index_book=0
    list_buyer=[]
    list_book=[]
    if paid_books!=[]:    
        index_buyer=find_buyer_index(buyer,paid_books)
        if index_buyer!=-1:
            paid_books_booklist=paid_books[index_buyer]["buyer"][buyer]['booklist']

            for i in range(len(paid_books)):
                a=paid_books[i]['buyer']
                for key in a.keys():
                    list_buyer.append(key)

            for i in range(len(paid_books_booklist)):
                list_book.append(paid_books_booklist[i]['title'])
    
    if buyer in list_buyer:
        index_buyer=find_buyer_index(buyer,paid_books)

        for book in shopping_cart_booklist:

            if book['title'] in list_book:
                index_book=find_book_index(book['title'],paid_books_booklist)
                paid_books_booklist[index_book]['quantity']+=book['quantity']
            
            else:
                paid_books_booklist.append(({'title':book['title'],
                'price':book['price'], 'quantity':book['quantity']}))
                
                index_book=find_book_index(book['title'],paid_books_booklist)

            update_to_booklist(book)
        
    else:
        paid_books.append( {'buyer': {buyer: {'booklist':[] } } } )
        index_buyer=find_buyer_index(buyer,paid_books)
        paid_books_booklist=paid_books[index_buyer]["buyer"][buyer]['booklist']
        for book in shopping_cart_booklist:
            paid_books_booklist.append({'title':book['title'], 'price':book['price'], 'quantity':book['quantity']})
            update_to_booklist(book)

    shopping_cart.pop(index_cart)
    write_to_json()
    return_to_menu()
    
## VIEW SHOPPING CART or View books bought from buyer ##
def view_books(buyer,book_list,current_frame):
    clear_frame(current_frame)
    if currentuser['access']=='Buyer':
        Main_text=f'The cart for buyer {buyer} is as shown below'
    else:
        Main_text=f'The Books paid for buyer {buyer} is as shown below'

    ttk.Label(current_frame,text=Main_text,anchor="center").grid(row=0,columnspan=4,sticky="ew")

    ttk.Label(current_frame,text="Number", anchor="center",
    width=10, borderwidth=3, relief="solid").grid(row=1, column=0, sticky="ew")

    ttk.Label(current_frame,text="Title", anchor="center",
    width=10, borderwidth=3, relief="solid").grid(row=1, column=1, sticky="ew")

    ttk.Label(current_frame,text="Price", anchor="center",
    width=10, borderwidth=3, relief="solid").grid(row=1, column=3, sticky="ew")

    ttk.Label(current_frame,text="Quantity", anchor="center",
    width=10, borderwidth=3, relief="solid").grid(row=1, column=2, sticky="ew")

    row = 2
    number=1
    index_buyer=find_buyer_index(buyer,book_list)
    
    buyer_book_list=tuple(book_list[index_buyer]["buyer"][buyer]['booklist'])
    
    Total_Price=0
    for k in buyer_book_list:
                
        number_label = ttk.Label(current_frame,text=number, anchor="center",
        width=10, borderwidth=3, relief="solid")

        title_label = ttk.Label(current_frame,text=k['title'], anchor="center",
        width=10, borderwidth=3, relief="solid")

        price_label = ttk.Label(current_frame,text=k["price"], anchor="center",
        width=10, borderwidth=3, relief="solid")

        quantity_label = ttk.Label(current_frame,text=k["quantity"], anchor="center",
        width=10, borderwidth=3, relief="solid")

        if currentuser['access']=='Buyer':
            delete_btn = ttk.Button(current_frame, text='Delete',
            command=lambda del_book=k : [delete_book(del_book)])
            delete_btn.grid(row=row, column=4)

        number_label.grid(row=row, column=0)
        title_label.grid(row=row, column=1)
        quantity_label.grid(row=row, column=2)
        price_label.grid(row=row, column=3)

        row += 1
        number +=1

        Total_Price += int(k['quantity'])*int(k['price'])

    if Total_Price>0:
        Total_Price_price_label_name=ttk.Label(current_frame,text='Total Price',
        width=10,borderwidth=3, relief="solid")

        Total_Price_price_label=ttk.Label(current_frame,text=f'{Total_Price}',
        width=10,borderwidth=3, relief="solid")

        Total_Price_price_label_name.grid(row=row,column=2)
        Total_Price_price_label.grid(row=row,column=3)
        if currentuser['access']=='Buyer':
            make_payment = ttk.Button(current_frame, text='Make Payment',
                command=lambda : [paybooks(Total_Price),Book_Payment(), return_to_menu()])
            make_payment.grid(row=row+1, column=3, sticky="ew")
            back_to_user_frame = ttk.Button(current_frame,text="Back",
                command=lambda:return_to_menu())

            back_to_user_frame.grid(row=row+1, column=0, sticky="ew")
        if currentuser['access']=='Admin':
            back_to_user_frame = ttk.Button(current_frame,text="Back",
            command=lambda:[View_paid_books()])
            
            back_to_user_frame.grid(row=row+1, column=0, sticky="ew")
        row+=1

    else:
        clear_frame(current_frame)
        return_to_menu()

    cleartext()

    def paybooks(Total_Price):
        msg = f' RM {Total_Price} has been paid!'
        messagebox.showinfo(title=f'Payment successful',message=msg)
        ## store paid buyer & book in json (viewpaid)
        ## remove buyer from shopping_cart
        ## update book quantity

### Admin View Paid books frame
def View_paid_books():
    clear_frame(paid_books_frame)
    ttk.Label(paid_books_frame,
    text=f"The Paid books for all the buyers is as shown below").grid(row=0,columnspan=4,sticky="ew")
    ttk.Label(paid_books_frame,text="Number", anchor="center",
    width=10, borderwidth=3, relief="solid").grid(row=1, column=0, sticky="ew")
    ttk.Label(paid_books_frame,text="Buyer Name", anchor="center",
    width=12, borderwidth=3, relief="solid").grid(row=1, column=1, sticky="ew")
    ttk.Label(paid_books_frame,text="Total", anchor="center",
    width=10, borderwidth=3, relief="solid").grid(row=1, column=2, sticky="ew")
    ttk.Label(paid_books_frame,text="Quantity", anchor="center",
    width=10, borderwidth=3, relief="solid").grid(row=1, column=3, sticky="ew")
   
    number=1
    row=2
    if len(paid_books[0])!=0:
        buyer_list=get_buyer_list(paid_books)

        for i in range(len(paid_books)):
            buyer_total=0
            buyer_quantity=0
            current_buyer=buyer_list[i]
            current_buyer_booklist=paid_books[i]['buyer'][current_buyer]['booklist']
            for books in current_buyer_booklist:
                buyer_total+=(int(books['quantity'])*int(books['price']))
                buyer_quantity+=int(books['quantity'])

            number_label = ttk.Label(paid_books_frame,text=number, anchor="center",
            width=10, borderwidth=3, relief="solid")

            buyer_name_label=ttk.Label(paid_books_frame,text=current_buyer, anchor="center",
            width=12, borderwidth=3, relief="solid")

            buyer_total_label=ttk.Label(paid_books_frame,text=buyer_total, anchor="center",
            width=10, borderwidth=3, relief="solid")

            buyer_quantity_label=ttk.Label(paid_books_frame,text=buyer_quantity, anchor="center",
            width=10, borderwidth=3, relief="solid")
            
            number_label.grid(row=row, column=0)
            buyer_name_label.grid(row=row, column=1)
            buyer_total_label.grid(row=row, column=2)
            buyer_quantity_label.grid(row=row, column=3)

            go_to_book_list_btn = ttk.Button(paid_books_frame, text='View Books',
                command=lambda curent_buyer=buyer_list[i] : [view_books(curent_buyer,paid_books,paid_books_frame)])
            go_to_book_list_btn.grid(row=row, column=4)
            number+=1
            row+=1

        back_to_user_frame = ttk.Button(paid_books_frame,text="Back",command=lambda:return_to_menu())
        back_to_user_frame.grid(row=row+1, column=0, sticky="ew")
    else:
        return_to_menu()

## CHANGE PASSWORD FRAME ###
## UI Widgets ##
title_change=ttk.Label(change_pasword_frame,text='Insert your new password here')
lbl_change=ttk.Label(change_pasword_frame,text='New password:')
ent_new=ttk.Entry(change_pasword_frame,show='*')
confirm_btn=ttk.Button(change_pasword_frame,text='Confirm', command=lambda : update_pass())
return_btn=ttk.Button(change_pasword_frame,text='Back',command=lambda : return_to_menu())

title_change.grid(row=0,column=1, columnspan=2)
lbl_change.grid(row=1,column=1)
ent_new.grid(row=1,column=2)
confirm_btn.grid(row=2,column=2)
return_btn.grid(row=2,column=1)

##### CREATE BOOK FRAME ####
lbl_create=ttk.Label(createbook_frame,text='Create Book Record')
lbl_booktitle=ttk.Label(createbook_frame,text='Book title : ')
ent_booktitle=ttk.Entry(createbook_frame)
lbl_category=ttk.Label(createbook_frame,text='Category: ')
ent_category=ttk.Entry(createbook_frame)
lbl_date=ttk.Label(createbook_frame,text='Year published: ')
ent_date=ttk.Entry(createbook_frame)
lbl_price=ttk.Label(createbook_frame,text='Price(RM): ')
ent_price=ttk.Entry(createbook_frame)
lbl_quan=ttk.Label(createbook_frame,text='Quantity: ')
ent_quan=ttk.Entry(createbook_frame)
con_btn=ttk.Button(createbook_frame,text='Create Book',command=lambda:Create_book_record())
back_button=ttk.Button(createbook_frame,text='Back',command=lambda:return_to_menu())

lbl_create.grid(row=0,column=1,columnspan=2)
lbl_booktitle.grid(row=1,column=0)
ent_booktitle.grid(row=1,column=1)
lbl_category.grid(row=2,column=0)
ent_category.grid(row=2,column=1)
lbl_date.grid(row=3,column=0)
ent_date.grid(row=3,column=1)
lbl_price.grid(row=4,column=0)
ent_price.grid(row=4,column=1)
lbl_quan.grid(row=5,column=0)
ent_quan.grid(row=5,column=1)
con_btn.grid(row=6,column=1)
back_button.grid(row=6,column=0)

## UPDATE BOOK FRAME ##
def table():
    ttk.Label(updatebook_frame,text="Number", anchor="center").grid(row=0, column=0, sticky="ew")
    ttk.Label(updatebook_frame,text="id", anchor="center").grid(row=0, column=1, sticky="ew")
    ttk.Label(updatebook_frame,text="title", anchor="center").grid(row=0, column=2, sticky="ew")
    ttk.Label(updatebook_frame,text="category", anchor="center").grid(row=0, column=3, sticky="ew")
    ttk.Label(updatebook_frame,text="date", anchor="center").grid(row=0, column=4, sticky="ew")
    ttk.Label(updatebook_frame,text="price", anchor="center").grid(row=0, column=5, sticky="ew")
    ttk.Label(updatebook_frame,text="quantity", anchor="center").grid(row=0, column=6, sticky="ew")
    row = 1
    number=1
    for k in booklist:
        number_label = ttk.Label(updatebook_frame,text=number, anchor="center")
        id_label = ttk.Label(updatebook_frame,text=k["id"], anchor="center")
        title_label = ttk.Label(updatebook_frame,text=k["title"], anchor="center")
        category_label = ttk.Label(updatebook_frame,text=k["category"], anchor="center")
        date_label = ttk.Label(updatebook_frame,text=k["date"], anchor="center")
        price_label = ttk.Label(updatebook_frame,text=k["price"], anchor="center")
        quantity_label = ttk.Label(updatebook_frame,text=k["quantity"], anchor="center")
        action_button = ttk.Button(updatebook_frame,text="Change",
        command=lambda book=k:[raise_frame(updatebook2_frame),whichbook(book)])
        
        number_label.grid(row=row, column=0, sticky="ew")
        id_label.grid(row=row, column=1, sticky="ew")
        title_label.grid(row=row, column=2, sticky="ew")
        category_label.grid(row=row, column=3, sticky="ew")
        date_label.grid(row=row, column=4, sticky="ew")
        price_label.grid(row=row, column=5, sticky="ew")
        quantity_label.grid(row=row, column=6, sticky="ew")
        action_button.grid(row=row, column=7, sticky="ew")

        row += 1
        number +=1
    ttk.Button(updatebook_frame,text='Back',command=lambda:return_to_menu()).grid(row=row+1,column=1,stick="ew")

    def whichbook(book=None):
        currentbook.update(book)
    cleartext()
### UPDATE BOOK FRAME 2 ##
lbl_update=ttk.Label(updatebook2_frame,text='Update book properties')
label=ttk.Label(updatebook2_frame,text='Fill in the new properties of the book below')
label_newbooktitle=ttk.Label(updatebook2_frame,text='New book title: ')
entry2_newbooktitle=ttk.Entry(updatebook2_frame)
label_category=ttk.Label(updatebook2_frame,text='Category: ')
entry2_category=ttk.Entry(updatebook2_frame)
label_date=ttk.Label(updatebook2_frame,text='Year published: ')
entry2_date=ttk.Entry(updatebook2_frame)
label_price=ttk.Label(updatebook2_frame,text='Price(RM): ')
entry2_price=ttk.Entry(updatebook2_frame)
label_quan=ttk.Label(updatebook2_frame,text='Quantity: ')
entry2_quan=ttk.Entry(updatebook2_frame)
back=ttk.Button(updatebook2_frame,text='Back',command=lambda:raise_frame(updatebook_frame))
updatebtn=ttk.Button(updatebook2_frame,text='Update',command=lambda:Update_book_record())

lbl_update.grid(row=0,column=0, columnspan=2)
label.grid(row=1, column=0, columnspan=2)
label_newbooktitle.grid(row=3,column=0)
entry2_newbooktitle.grid(row=3,column=1)
label_category.grid(row=4,column=0)
entry2_category.grid(row=4,column=1)
label_date.grid(row=5,column=0)
entry2_date.grid(row=5,column=1)
label_price.grid(row=6,column=0)
entry2_price.grid(row=6,column=1)
label_quan.grid(row=7,column=0)
entry2_quan.grid(row=7,column=1)
back.grid(row=8,column=0)
updatebtn.grid(row=8,column=1)

entry_newbooktitle=ttk.Entry(updatebook2_frame).insert(0,currentbook['title'])
entry_category=ttk.Entry(updatebook2_frame).insert(0,currentbook['category'])
entry_date=ttk.Entry(updatebook2_frame).insert(0,currentbook['date'])
entry_price=ttk.Entry(updatebook2_frame).insert(0,currentbook['price'])
entry_quan=ttk.Entry(updatebook2_frame).insert(0,currentbook['quantity'])

## SEARCH BOOK FRAME ##
def searchbook():
    lbl_search=ttk.Label(searchbook_frame,text='Search book by book title')
    lbl_title=ttk.Label(searchbook_frame,text='Enter book title: ');ent_title=ttk.Entry(searchbook_frame)
    back_btn=ttk.Button(searchbook_frame,text='Back',command=lambda:[return_to_menu(),clear_frame(searchbook_frame)])
    continue_btn=ttk.Button(searchbook_frame,text='Search',command=lambda:[Search_book_by_titles(ent_title.get())])

    lbl_search.grid(row=0,column=0)
    lbl_title.grid(row=1,column=0);ent_title.grid(row=1,column=1)
    back_btn.grid(row=2,column=0)
    continue_btn.grid(row=2,column=1)
searchbook()

### DELETE BOOK FRAME ##
del_title=ttk.Label(delete_book_frame,text='DELETE BOOK RECORD')
del_book=ttk.Label(delete_book_frame,text='Book title to be deleted : ')
del_entry=ttk.Entry(delete_book_frame)
del_back=ttk.Button(delete_book_frame,text='Back',command=lambda:return_to_menu())
del_con=ttk.Button(delete_book_frame,text='Delete Book', command=lambda: Delete_book_record())

del_title.grid(row=0,column=0)
del_book.grid(row=1,column=0)
del_entry.grid(row=1,column=1)
del_back.grid(row=2,column=0)
del_con.grid(row=2,column=1)

### BUY BOOK FRAME ##
def shoppingbook():
    ttk.Label(shopbook_frame,text="Number", anchor="center").grid(row=0, column=0, sticky="ew")
    ttk.Label(shopbook_frame,text="Title", anchor="center",
                 borderwidth=3, relief="solid").grid(row=0, column=1, sticky="ew")
    ttk.Label(shopbook_frame,text="Price", anchor="center",
                 borderwidth=3, relief="solid").grid(row=0, column=2, sticky="ew")
    ttk.Label(shopbook_frame,text="Availabe Stock", anchor="center",
                 borderwidth=3, relief="solid").grid(row=0, column=3, sticky="ew")
    ttk.Label(shopbook_frame,text="Quantity in cart", anchor="center",
                 borderwidth=3, relief="solid").grid(row=0, column=4, sticky="ew")
    current_buyer_index=find_buyer_index(currentuser['users'],shopping_cart)
    row = 1
    number=1
    for b in booklist:
        cart_quantity=0
        number_lbl_buy = ttk.Label(shopbook_frame,text=str(number)+'.', anchor="center")
        title_lbl_buy = ttk.Label(shopbook_frame,text=b["title"], anchor="center",
                                     borderwidth=3, relief="solid")
        price_lbl_buy = ttk.Label(shopbook_frame,text=b["price"], anchor="center",
                                     borderwidth=3, relief="solid")
        quantity_lbl_buy = ttk.Label(shopbook_frame,text=b["quantity"], anchor="center",
                                     borderwidth=3, relief="solid")
        action_button_buy = ttk.Button(shopbook_frame,text="Add to cart",command=lambda book=b:[Add_to_cart(book)])
        if current_buyer_index!=-1:
            shopping_cart_booklist=shopping_cart[current_buyer_index]['buyer'][currentuser['users']]['booklist']
            current_book_index=find_book_index(b['title'],shopping_cart_booklist)
            if current_book_index!=-1:
                cart_quantity=shopping_cart_booklist[current_book_index]['quantity']

        quantity_in_cart=ttk.Label(shopbook_frame,text=cart_quantity, anchor="center",
                                     borderwidth=3, relief="solid")

        number_lbl_buy.grid(row=row, column=0, sticky="ew")
        title_lbl_buy.grid(row=row, column=1, sticky="ew")
        price_lbl_buy.grid(row=row, column=2, sticky="ew")
        quantity_lbl_buy.grid(row=row, column=3, sticky="ew")
        quantity_in_cart.grid(row=row, column=4, sticky="ew")
        action_button_buy.grid(row=row, column=5, sticky="ew")

        row += 1
        number +=1

    ttk.Button(shopbook_frame,text='View shopping cart',
    command=lambda:[view_books(currentuser['users'],shopping_cart,view_cart_frame),
    raise_frame(view_cart_frame)]).grid(row=row+1,column=5, sticky="w")
    ttk.Button(shopbook_frame,text='Back',
    command=lambda :return_to_menu()).grid(row=row+1,column=0, sticky="e")

    cleartext()

### buyer Frame ####
##### Buyer ACCOUNT SETTING/Buyer Module COMMAND ###
def return_to_menu():
    cleartext()
    if currentuser['access']=='Admin':
        raise_frame(admin_frame)

    elif currentuser['access']=='Buyer':
        raise_frame(buyer_frame)
        
def click_buyer_option2():
    a=buyer_do_what.get()
    b=buyer_do_what2.get()
    cleartext()
    if b == 'Change password':
        raise_frame(change_pasword_frame)
    elif b == 'Log out':
        logout()
    elif b == 'Delete account':
        delete_acc()
    elif a=='Search book':
        searchbook(),raise_frame(searchbook_frame)
    elif a=='Buy Books':
        shoppingbook()
        raise_frame(shopbook_frame)
    elif a=='View Shopping cart':
        index_buyer=find_buyer_index(currentuser['users'],shopping_cart)
        if index_buyer==-1:
            return_to_menu()
        else:
            blist=tuple(shopping_cart[index_buyer]['buyer'][currentuser['users']]['booklist'])
            if len(blist)==0:
                return_to_menu()
            else:
                view_books(currentuser['users'],shopping_cart,view_cart_frame)
                raise_frame(view_cart_frame)

## Buyer Frame ####
## DROPMENU FOR BUYER MODULE ###
buyer_option = ['Search book', 'Buy Books', 'View Shopping cart']
buyer_do_what = tkinter.StringVar(buyer_frame)
buyer_do_what.set('Buyer Module')
buyer_do_what_menu = tkinter.OptionMenu(buyer_frame, buyer_do_what, *buyer_option)
buyer_do_what_menu.grid(row=2, column= 1, columnspan=2)
### DROP MENU FOR BUYER ACCOUNT SETTTING ###
buyer_option2 = ['Change password', 'Log out', 'Delete account']
buyer_do_what2 = tkinter.StringVar(buyer_frame)
buyer_do_what2.set('Account Setting')
buyer_do_what2_menu = tkinter.OptionMenu(buyer_frame, buyer_do_what2, *buyer_option2)
buyer_do_what2_menu.grid(row=3, column= 1, columnspan=2)
#### UI Widgets###
title = ttk.Label(buyer_frame, text='BUYER PAGE')
button_action =ttk.Button(buyer_frame, text='Continue',command=lambda:click_buyer_option2())
### UI Layouts ####
title.grid(row=0, column=1, columnspan=3)
button_action.grid(row=4, columnspan=3)

#### ADMIN ACCOUNT SETTING COMMAND ###
def click_admin_option2():
    a=admin_do_what.get()
    b=admin_do_what2.get()
    cleartext()
    if b == 'Change password':
        raise_frame(change_pasword_frame)
    elif b == 'Log out':
        logout()
    elif b == 'Delete account':
        delete_acc()
    elif a=='Create book record':
        raise_frame(createbook_frame)
    elif a=='Search book by book titles':
        searchbook(),raise_frame(searchbook_frame)
    elif a=='Delete book record':
        raise_frame(delete_book_frame)
    elif a=='Update book record':
        table()
        raise_frame(updatebook_frame)
    elif a=='View the paid books':
        View_paid_books()
        raise_frame(paid_books_frame)

#### ADMIN FRAME ####
### DROPDOWN MENU FOR ADMIN MODULE ###
admin_option = ['Create book record', 'Search book by book titles',
                'Update book record', 'Delete book record','View the paid books']

admin_do_what = tkinter.StringVar(admin_frame)
admin_do_what.set('Administrator Module')
admin_do_what_menu = tkinter.OptionMenu(admin_frame, admin_do_what, *admin_option)
admin_do_what_menu.grid(row=2, column= 1, columnspan=2)
#### DROPDOWN MENU FOR ADMIN ACCOUNT SETTING ##3
admin_option2 = ['Change password', 'Log out', 'Delete account']
admin_do_what2 = tkinter.StringVar(admin_frame)
admin_do_what2.set('Account Setting')
admin_do_what2_menu = tkinter.OptionMenu(admin_frame, admin_do_what2, *admin_option2)
admin_do_what2_menu.grid(row=3, column= 1, columnspan=2)
#### UI Widgets###
title = ttk.Label(admin_frame, text='ADMIN PAGE')
button_action_admin =ttk.Button(admin_frame, text='Continue',command=lambda:click_admin_option2())
### UI Layouts ####
title.grid(row=0, column=1, columnspan=2)
button_action_admin.grid(row=4, columnspan=3)

#### Run Gui Application ####
root.mainloop()