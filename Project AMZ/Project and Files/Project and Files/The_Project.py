'''
Created on Nov 24, 2023

@author: andri

Description: This is a GUI that is used as we help desk at the CCIT. it contains a forum for a student who is renting a laptop
and store the information in a text file called projectfile.txt
it enables the user to search though the stored data using the first name.
and lastly is displays the overall activity under a description box. 
you can add to the file and remove as well. 
'''
import tkinter as tk 
from tkinter import messagebox, StringVar, IntVar, ttk, Spinbox
from PIL import ImageTk, Image


######INFO#######

#this is a function that reads the file and stores it in a dictionary 
storage1 = {}

def storefiles():
    file = open("../Project/projectfile.txt", "r")
    filereader = file.readlines()
    fileelement = ["Rented Day", "first", "last", "year", "id", "cpu", "Return Day"]
    
    for line in filereader:
        line = line.split(":")
        store = {}
        for i in range(len(fileelement)):
            store[fileelement[i]] = line[i].strip()  # strip to remove leading/trailing whitespaces
        id = store['id']
        storage1[id] = store
    return storage1
#this function closes the GUI
def clo():
    wn.destroy()
#this function reads from the file and stores it in a text box for display
def loadtextinfo(file):
    storefiles()
    stored_info.delete(0, tk.END)
    for key, value in file.items():
        stored_info.insert(tk.END, value['cpu'])
#this function is used to update the description part when you select a specific computer name 
def updatesuspectinfo(event=None):
    selected_index = stored_info.curselection()
    if selected_index:
        selected_cpu = stored_info.get(selected_index)
        loadInformation(selected_cpu, storage1)

#this function loads the information to the text box
def loadInformation(cpu, file):
    for keys in file:
        if cpu == file[keys]['cpu']:
            stored_info_display.delete('1.0', tk.END)
            stored_info_display.insert(tk.END, f"Name: {file[keys]['first']} {file[keys]['last']}\n")
            stored_info_display.insert(tk.END, f"Rented Day: {file[keys]['Rented Day']}\n")
            stored_info_display.insert(tk.END, f"Return Day: {file[keys]['Return Day']}\n")
            stored_info_display.insert(tk.END, f"CPU: {file[keys]['cpu']}\n")
            stored_info_display.insert(tk.END, f"ID: {file[keys]['id']}\n")
#this function lets the user to remove a selected file from the stored info
def remove_selected_item():
    selected_index = stored_info.curselection()
    if selected_index:
        selected_cpu = stored_info.get(selected_index)
        for key, value in storage1.items():
            if value['cpu'] == selected_cpu:
                del storage1[key]
                break
        stored_info.delete(selected_index)
        stored_info_display.delete('1.0', tk.END)  # Clear the displayed information
        #update the new file
        file = open("../Project/projectfile.txt", "w")
        for key, value in storage1.items():
                file.write(f"{value['Rented Day']}:{value['first']}:{value['last']}:{value['year']}:{value['id']}:{value['cpu']}:{value['Return Day']}\n")




########Rental Email Maker ###########
def distroy():
    wn.destroy()#closes the windows
    demo = False
# this is a function that creates the students info to the file and store it if the user is "okay" with it.
def create():
    storefiles()
    id = Id_Entry.get()

    # Check if the name already exists
    if id in storage1.keys():
        return messagebox.showerror("Warning", "The Student Already Exist") # Exit the function if the name already exists

    # If the Id is not found, proceed with creating the email
    conformation = messagebox.askokcancel("Email", f"On Day {day_Entry.get()}/{month_Entry.get()}/{year_Entry.get()}, Student {fnameE.get().capitalize()} {lnameE.get()}({year_label.get()}) by the ID number {IdE.get()}, Rented a computer with a name : {CmpE.get()},That will be returned on {day2_Entry.get()}/{month2_Entry.get()}/{year2_Entry.get()}.\n")
    
    if conformation: 
        file = open(f"../Project/projectfile.txt", "a")#this opens up the file so that we can append the file
        #append the file in a regular forum so that it could be accessed easily 
        file.write(f"{day_Entry.get()}/{month_Entry.get()}/{year_Entry.get()}:{fnameE.get().capitalize().strip()}:{lnameE.get().capitalize().strip()}:{year_label.get()}:{IdE.get()}:{CmpE.get()}:{day2_Entry.get()}/{month2_Entry.get()}/{year2_Entry.get()}.\n")
        file.close()
#clear button for the importing forum 
def clear():
    fname_Entry.delete(0, tk.END)
    lname_Entry.delete(0, tk.END)
    Id_Entry.delete(0, tk.END)
    Computer_Entry.delete(0, tk.END)
    day_Entry.delete(0, tk.END)
    month_Entry.delete(0, tk.END)
    year_Entry.delete(0, tk.END)
    day2_Entry.delete(0, tk.END)
    month2_Entry.delete(0, tk.END)
    year2_Entry.delete(0, tk.END)
    year_label.delete(0,tk.END)
    
#### Search Already EXISTED #####
def close2():
    wn.destroy() #closes the Windows 
    

def clear2():
    fsearchE.delete(0,tk.END) #clears the search box on the first name search menu

def search():
    storage = storefiles()
    find = fsearchE.get().strip().capitalize()#searches through the file regardless of the format of the user input
    for key,value in storage.items():
        if find == storage[key]["first"]:
            messagebox.showinfo("Found", f"Student: {storage[key]['first']} {storage[key]['last']}, Rented a computer({storage[key]['cpu']}) on {storage[key]['Rented Day']} that will be returned on {storage[key]['Return Day']}")
            break
        else:
            messagebox.showinfo("Not Found","Student Not Found!!")
            break
        
        
######Welcome GUI######   
# this function reads the users input and assigns it to this variable and closes the window    
def submit():
    user_input = var.get()
    wn.destroy()
    
    return user_input

if __name__ == '__main__':
    # this is a while loop that created for the user not to break the code
    # and not to exit and stay in an loop until they enter the right number to exit 
    demo = True 
    while demo:
        # this is the code for the First GUI that is displayed 
        wn = tk.Tk()
        wn.title("Welcome User")
        
        first_frame = tk.LabelFrame(wn, text = '')
        first_frame.grid(row = 0 , column = 0, padx = 5, pady = 6)
        
        logo_label = tk.Label(first_frame, width = 200, height = 200)
        logo_label.grid(row = 0, column = 0, padx = 5, pady = 5, rowspan = 3)
        #imports the logo of the project
        logo_image = ImageTk.PhotoImage((Image.open("../Project/logoo.jpg")))
        logo_label['image'] = logo_image
        logo_label.image = logo_image
        
        second_frame = tk.LabelFrame(wn, text = '')
        second_frame.grid(row = 0 , column = 1, padx = 5, pady = 6)
        #labels for the first user interface GUI
        title_label = tk.Label(second_frame, text = "Welcome to the HelpDesk!!", font = 15)
        title_label.grid(row = 0, column = 0, padx = 5, pady = 5  )
    
        choice_label = tk.Label(second_frame, text = "=> Please select the number you want info to: ")
        choice_label.grid(row = 1, column = 0, padx = 5, pady = 5  )
        choice1_label = tk.Label(second_frame, text = "1. Rental Forum ")
        choice1_label.grid(row = 2, column = 0, padx = 5, pady = 5  , sticky = tk.W)
        choice2_label = tk.Label(second_frame, text = "2. Search for already registered file ")
        choice2_label.grid(row = 3, column = 0, padx = 5, pady = 5  , sticky = tk.W)
        choice2_label = tk.Label(second_frame, text = "3. All stored File")
        choice2_label.grid(row = 4, column = 0, padx = 5, pady = 5  , sticky = tk.W)
        choice3_label = tk.Label(second_frame, text = "4. Quit ")
        choice3_label.grid(row = 5, column = 0, padx = 5, pady = 5   , sticky = tk.W)
        
        var = StringVar()
        blank = tk.Entry(second_frame, textvariable= var, width = 5)
        blank.grid(row = 5, column = 0, padx = 5, pady = 5 ,sticky = tk.E)
        
        ##### Buttons####
        
        submit_butt  = tk.Button(second_frame, text = "Submit", command = submit)
        submit_butt.grid(row = 5, column = 1, padx = 5, pady = 5)
        
        wn.mainloop()
        user_input = var.get()
        # based on the user input the following code will be executed 
        if user_input == "4":
            demo = False 
        elif user_input == "3":
            wn = tk.Tk()
            wn.title("Stored Information")
            data = storefiles()
            # labels for stored information display option
            frame_one = tk.LabelFrame(wn, text='Computer')
            frame_one.grid(row=0, column=0, padx=5, pady=5)
            
            #created and updates the list box from the text file
            stored_info = tk.Listbox(frame_one, width=15)
            stored_info.grid(row=0, column=0, padx=5, pady=5)
            stored_info.bind("<<ListboxSelect>>", updatesuspectinfo)
        
            frame_two = tk.LabelFrame(wn, text='Description')
            frame_two.grid(row=0, column=1, padx=5, pady=5)
        
            stored_info_display = tk.Text(frame_two, width=40, height=10)
            stored_info_display.grid(row=0, column=1, padx=5, pady=5)
            
            ### Buttons 
            frame_three = tk.LabelFrame(wn, text='')
            frame_three.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)
        
            close_button = tk.Button(frame_three, text="Close", command=clo)
            close_button.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
        
            remove_button = tk.Button(frame_three, text="Remove", command = remove_selected_item)
            remove_button.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        
            loadtextinfo(data)
        
            wn.mainloop()
            demo = True
        elif user_input == "2":
            wn = tk.Tk()
            wn.title("Search Already Registered File")
            search_label1 = tk.LabelFrame(wn, text = "")
            search_label1.grid(row = 0, column = 1, padx = 5, pady = 5)
            #labels for search by first name Display option
            fsearch = tk.Label(search_label1, text = "Search by First Name:")
            fsearch.grid(row = 0, column = 0, padx = 5, pady = 5)
            
            fE = StringVar()
            fsearchE = tk.Entry(search_label1, textvariable= fE)
            fsearchE.grid(row = 0, column = 1,columnspan = 2, padx = 5, pady = 5)
            
            search_label2 = tk.LabelFrame(wn, text = "")
            search_label2.grid(row = 1, column = 1, padx = 5, pady = 5)
        
            
            #BBBBBBUUUUUUUTTTTTTTTOOOOOOONNNNNNNNSSSSSS
            butt_label = tk.LabelFrame(wn, text = "")
            butt_label.grid(row = 2, column = 1, padx = 5, pady = 5)
            
            search_butt = tk.Button(butt_label, text = "Search", width = 10, command = search)
            search_butt.grid(row = 1, column = 1,padx = 5, pady = 5,columnspan = 2 )
            close_butt = tk.Button(butt_label, text = "Close", width = 10, command = close2)
            close_butt.grid(row = 0, column = 2,padx = 5, pady = 5)
            clear_butt = tk.Button(butt_label, text = "Clear", width = 10, command = clear2)
            clear_butt.grid(row = 0, column = 1,padx = 5, pady = 5)
        
            wn.mainloop()
            demo = True 
            
        elif user_input == "1":
            wn = tk.Tk()
            wn.title("Rental Email Maker")
            # the Rental forum Display option labels 
            inside_frame = tk.LabelFrame(wn, text = '')
            inside_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
            
            title_label = tk.Label(inside_frame, text = "Tech Saint's Email Creator", width = 40, font = 100)
            title_label.grid(row = 0, column = 1, padx = 5, pady = 5, columnspan = 5 )
            
            logo_label = tk.Label(inside_frame)
            logo_label.grid(row = 0, column = 0, padx = 5, pady = 5)
            logo_image = ImageTk.PhotoImage((Image.open("../Project/logo.jpg")))
            logo_label['image'] = logo_image
            logo_label.image = logo_image
            
            
           
            another_frame = tk.LabelFrame(wn, text = '')
            another_frame.grid(row = 1, column = 0, padx = 5, pady = 5)
            
            fname_label = tk.Label(another_frame, text = "First Name: ")
            fname_label.grid(row = 1, column = 0, padx = 5, pady = 5, sticky = tk.E)
            
            fnameE = StringVar()
            fname_Entry = tk.Entry(another_frame, textvariable= fnameE)
            fname_Entry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = tk.W)
            
            lname_label = tk.Label(another_frame, text = "Last Name: ")
            lname_label.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = tk.E)
            
            lnameE = StringVar()
            lname_Entry = tk.Entry(another_frame, textvariable= lnameE)
            lname_Entry.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = tk.W)
            
            Id_label = tk.Label(another_frame, text = "ID Number: ")
            Id_label.grid(row = 2, column = 0, padx = 5, pady = 5)
            
            IdE = StringVar()
            Id_Entry = tk.Entry(another_frame, textvariable= IdE)
            Id_Entry.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = tk.W)
            
            computer_label = tk.Label(another_frame, text = "Computer's Name: ")
            computer_label.grid(row = 2, column = 2, padx = 5, pady = 5)
            
            CmpE = StringVar()
            Computer_Entry = tk.Entry(another_frame, textvariable= CmpE)
            Computer_Entry.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = tk.W)
            
            yearr_label = tk.Label(another_frame, text = "Year: ")
            yearr_label.grid(row = 3, column = 0, padx = 5, pady = 5)
            year_label = ttk.Combobox(another_frame, values = ['Freshman', 'Sophomore', 'Junior', 'Senior',''])
            year_label.grid(row = 3, column = 1, padx = 5, pady = 5)
            
            
            
            
            other_frame = tk.LabelFrame(wn, text = '')
            other_frame.grid(row = 2, column = 0, padx = 5, pady = 5)
            
            rental_label = tk.Label(other_frame, text = "Rental date(dd/mm/yy): ")
            rental_label.grid(row = 0, column = 0, padx = 5, pady = 5)
            
            # spin box for the date to change is using arrows and number limits
            day_Entry = tk.Spinbox(other_frame, from_ = 1, to = 30, width = 3)
            day_Entry.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = tk.W)
            
            month_Entry = tk.Spinbox(other_frame, from_ = 1, to = 12, width = 4)
            month_Entry.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = tk.W)
            
            year_Entry = tk.Spinbox(other_frame, from_ = 2023, to = 2030, width = 5)
            year_Entry.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = tk.W)
            
            return_label = tk.Label(other_frame, text = "Return date(dd/mm/yy): ")
            return_label.grid(row = 1, column = 0, padx = 5, pady = 5)
            
            
            day2_Entry = tk.Spinbox(other_frame, from_ = 1, to = 30, width = 3)
            day2_Entry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = tk.W)
            
            month2_Entry = tk.Spinbox(other_frame, from_ = 1, to = 12, width = 4)
            month2_Entry.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = tk.W)
            
            year2_Entry = tk.Spinbox(other_frame, from_ = 2023, to = 2030, width = 5)
            year2_Entry.grid(row = 1, column = 3, padx = 5, pady = 5, sticky = tk.W)
            
            third_frame = tk.LabelFrame(wn, text = '')
            third_frame.grid(row = 3, column = 0, padx = 5, pady = 5)
            
            ####Button####
            
            clear_butt = tk.Button(third_frame, text = "Clear", width = 7, command = clear)
            clear_butt.grid(row = 0, column = 0 , padx = 5, pady = 5)
            
            create_butt = tk.Button(third_frame, text = "Create", width = 7, command = create)
            create_butt.grid(row = 0, column = 1 , padx = 5, pady = 5)
            
            close_butt = tk.Button(third_frame, text = "Close", width = 7, command = distroy)
            close_butt.grid(row = 1, column = 0 , padx = 5, pady = 5, columnspan = 2)
            
            wn.mainloop()
            demo = True 
        else: 
            messagebox.showerror("Wrong Number", "Please Choose the Right Number!:(")
            demo = True 
            
            
            
            
            
            
            
            
            
            
            
            
            