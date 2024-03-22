def pipeline():
    steps = {}

    def add_step(name):
        def decorator(func):
            steps[name] = func
            return func
        
        return decorator
    
    def execute(data, role):
        for step_name, step_func in steps.items():
            data = step_func(data, role)
        return data
    
    return add_step, execute

add_step, execute_pipeline = pipeline()

@add_step('get')
def get(data, role):
    return {
        "name": data["name"], 
        "age": data["age"], 
        "department": data["department"]
    }

@add_step('post')
def post(data, role):
    return f"User {data['name']} added successfully"

@add_step('delete')
def delete(data, role):
    if role == 'HR':
        return f"User {data['name']} deleted successfully"
    else:
        return "User denied access, as not authorized"

initial_details = {"name": "Pranjal", "age": 32, "department": "ASE"}
role = "Intern"
result = execute_pipeline(initial_details, role)
print(result)