class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name 
        self.password = password 
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password
    
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
    
#functions belonging to a class are called methods
    def user_info(self):
        print(f"User {self.name} currently works as {self.current_job_title}. You can contact them at {self.user_email}")

app_one_user = User("pranjalsinha1965@gmail.com", "Pranjal", "prs@123456", "analyst")
app_one_user.user_info()

# closures in Python help to invoke functions outside their scope.

