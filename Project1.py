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
         
    
obj=chatbook()
         