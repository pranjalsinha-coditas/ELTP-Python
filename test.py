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
        def wrapper(data, role, **kwargs):
            if role != "HR":
                raise PermissionError("User not authorized to delete")
            return func(data, role, **kwargs)
        return wrapper

    return add_step, execute, delete_authorization

add_step, execute_pipeline, delete_authorization = authorize()

@add_step('get')
def get(data, role):
    return {
        "name": data["name"],
        "age": data["age"],
        "department": data["department"]
    }

@add_step('post')
def post(data, role):
    return "User data accessed for storage"

@add_step('delete')
@delete_authorization
def delete(data, role):
    return f"User deleted data successfully"

initial_data = {'name': 'Pranjal', 'age': 32, 'department': 'CE0'}
role = "HR"  # Change role to "intern" to test

pipeline_result = execute_pipeline(initial_data, role)
print(pipeline_result)
