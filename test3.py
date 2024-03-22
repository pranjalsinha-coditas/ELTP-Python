import time
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
        def wrapper(data, role=None, **kwargs):
            # Generator function to check authorization
            def authorization():
                yield role == role
            auth_check = next(authorization())
            if not auth_check:
                raise ValueError("User not authorized to delete")
            start_time = time.time()
            result = func(data, role=role, **kwargs)
            end_time = time.time()
            print(f"Execution time of {func.__name__}: {end_time - start_time} seconds")
            return result
        return wrapper
    return add_step, execute, delete_authorization

add_step, execute_pipeline, delete_authorization = authorize()

@add_step('get')
def get(data, role=None, **kwargs):
    return {
        "name": data["name"], 
        "age": data["age"], 
        "department": data["department"]
    }

@add_step('post')
def post(data, role=None, **kwargs):
    return f"User details successfully updated from the browser console"

@add_step('delete')
@delete_authorization
def delete(data, role=None, **kwargs):
        while(role != "HR"):
            raise ValueError("User not authorized to delete")
        return f"User data successfully deleted"

initial_details = {"name": "Pranjal", "age": 32, "department": "ASE"}

# Try with role="HR"
role = "HR"
result = execute_pipeline(initial_details, role)
print(result)

# Try with role="Intern"
role = "HR"
result = execute_pipeline(initial_details, role)
print(result)
