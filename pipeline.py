# def pipeline():
#     steps = {}
#     def add_step(name):
#         def decorator(func):
#             steps[name] = func
#             return func 
#         return decorator
#     def execute(data):
#         result = data
#         for step_name, step_func in steps.items():
#             result = step_func(*result)
#             if result is None:
#                 return False
#         return True
#     return add_step, execute 

# add_step, execute_pipeline = pipeline()
    
# @add_step('get')
# def get(name, age, department, **kwargs):
#     return f"Name: {name}, Age: {age}, Department: {department}"
# @add_step('post')
# def post(name, age, department, **kwargs):
#     return f"Name: {name}, Age: {age}, Department: {department}"
# @add_step('delete')
# def delete(name, age, department, **kwargs):
#     try:
#         if department == "HR":
#             return f"User: {name} successfully deleted"
#         else: ValueError
#     except:
#         return f"User not authorized"

# initial_details = ("Pranjal", 32, "ASE")
# role = "Intern"
# result = execute_pipeline(initial_details, role)
# print(result)
#sample without output based code 
def authorize():
    steps = {}
    def add_step(name):
        def decorator(func):
            steps[name] = func
            return func
        return decorator
    def execute(data, role, **kwargs):
        for step_name, step_func in steps.items():
            data = step_func(data, role, **kwargs)
        return data
    def delete_authorization(func):
        def wrapper(data, role, *args, **kwargs):
            return func(data, role, *args, **kwargs) 
        return wrapper
    return add_step, execute, delete_authorization

add_step, execute_pipeline, delete_authorization = authorize()

@add_step('get')
def get(data, role, **kwargs):
    return {
        "name": data["name"],
        "age": data["age"],
        "department": data["department"] 
    }

@add_step('post')
def post(data, role, **kwargs):
    return f"User data accessed for storage"

@add_step('delete')
@delete_authorization
def delete(data, role, **kwargs):
    try:
        return f"User deleted data successfully"
    except Exception as e:
        return f"An error occurred: {str(e)}"

initial_data = {'name': 'Pranjal', 'age':32, 'department':'CEO'}
role = "HR"
result = execute_pipeline(initial_data, role)
print(result)



        




    