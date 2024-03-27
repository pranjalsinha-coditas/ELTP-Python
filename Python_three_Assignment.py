# minmize if and else pass it as a dictionary. Operations for user get, post, delete : 
# (should not be able to delete it ). So hr should delete but intern should not delete. 
# Input name, age, department and other details
from typing import Callable
def get_details(details_list: list[Callable]) -> Callable[..., bool]:
    user_details = {
        "name": details_list[0], 
        "age" : details_list[1], 
        "department"  : details_list[2]
    }             
    return user_details

def post_details(details_list: list[Callable]) -> Callable[..., bool]:
    return details_list #The dictionary used

def deletion_details(details_list: list[Callable]) -> str | None:
    try:
        if details_list[2] == "Intern":
            return f"Not authorized as the user is designated to {details_list[2]}"
        # details_list = details_list.clear #for reference 
        # return f"The details are deleted {details_list}"
    except ValueError:
                details_list = details_list.clear #for reference 
                return f"The details are deleted {details_list}"
    
my_methods = {
    "GET": get_details, 
    "POST": post_details, 
    "DELETE": deletion_details
}

my_details = ["Pranjal", 21, "SDET"]
details_userone = ["Amar", 23, "Intern"]
details_usertwo = ["Yamal", 26, "Director"] 

print(get_details(my_details))
print(deletion_details(my_details))
print(get_details(details_userone))
print(deletion_details(details_userone))
print(get_details(details_usertwo))
print(deletion_details(details_usertwo))
print(post_details(my_details))







