def get_query(url):
    query = url.split("?")
    query_params = query[1].split("&")
    query_dict = {}
    for keys in query_params:
        key = keys.split("=")
        query_dict[f"{key[0]}"] = key[1]
    return query_dict

def handle_users(*args, **kwargs):
    print(f"user {kwargs['user']} is authenticated")

def handle_products(*args, **kwargs):
    print("Got the product details")
    print(kwargs)

def handle_unknown():
    print("Check your URL: ")

def extract_url_components(url):
    endpoint = url.split("/")[-1].split("?")[0]
    query_dict = get_query(url)
    return {"endpoint": endpoint, "params": query_dict}

endpoint_handlers = {
    "users": handle_users,
    "products": handle_products,
}

url = "example.com/users?user=John&password=12345"
result = extract_url_components(url)

handler_func = endpoint_handlers.get(result["endpoint"], handle_unknown)
handler_func(**result["params"])

