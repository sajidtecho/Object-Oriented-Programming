class chatbook:
    def __init__(self):
        print("Chatbook class initialized")  
        self.username=""
        self.password=""
        self.loggin_status=False
        self.menu()
        
    #creating a method  
    def menu(self):
        user_input=input(""""Welcome to Chatbook!
                         1. Press 1 to Sign Up
                         2. Press 2 to Log In
                         3. Press 3 to write a post
                         4. Press 4 to message a freind
                         5. Press any key to exit
                         """)
        if user_input=="1":
            self.sign_up()
        elif user_input=="2":
            self.log_in()
        elif user_input=="3":
            self.write_post()
        elif user_input=="4":
            self.message_friend()
        else:
            print("Thank you for using Chatbook. Goodbye!")
            exit()
     
    def sign_up(self):
        self.username=input("Enter your username: ")
        self.password=input("Enter your password: ")
        print("Sign Up successful! Please log in.")
        print("\n")
        self.menu()  
    
    def log_in(self):
        if self.username=="" or self.password=="":
            print("No user found. Please sign up first.")
        else:
            username=input("Enter your username: ")
            password=input("Enter your password: ")
            if self.username==username and self.password==password:
                self.loggin_status=True
                print("Log In successful!")
            else:
                print("Invalid credentials. Please try again.")
            print("\n")
            self.menu()
            
    def write_post(self):
        if self.loggin_status==True:
            post=input("Write your post: ")
            print("Post published:", post)
        else:
            print("Please log in to write a post.")
        print("\n")
        self.menu()
        
    def message_friend(self):
        if self.loggin_status==True:
            friend=input("Enter your friend's name: ")
            message=input("Enter your message: ")
            print(f"Message sent to {friend}: {message}")
        else:
            print("Please log in to message a friend.")
        print("\n")
        self.menu()

    
obj=chatbook()
         