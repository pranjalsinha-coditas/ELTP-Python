from typing import Callable
def validate(input, *pipeline: list[Callable]) -> Callable[..., bool]:
    return [validator(input) for validator in pipeline]

def check_dt(dt: type) -> Callable:
    return lambda input: isinstance(input, dt)

def has_length(min_length: int, max_length: int) -> Callable[..., bool]:
    return lambda input: min_length <= len(input) <= max_length

validators = {
    "is_str": check_dt(str),
    "is_int": check_dt(int),
    "has_length": has_length
}

name_validators = [
    validators["is_str"],
    validators["has_length"](1, 100)  
]

password_validators = [
    validators["is_str"],
    validators["has_length"](8, 20) 
]

name_valid = validate("Pranjal", *name_validators)
password_valid = validate("prs@123456", *password_validators)

print("Name validation results:", name_valid)
print("Password validation results:", password_valid)
