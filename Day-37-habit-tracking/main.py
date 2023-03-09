import requests
import datetime as dt
import os
import secrets
import json


pixela_url = "https://pixe.la/v1/users"
# user_name = None
TOKEN = os.environ.get("PIXELA_TOKEN")
#graph_id = "graph1"

# N/B: You could modularize the try blocks into a function to test for the file presence


# Step 1, setting user account on pixela
# use secrets module to generate random tokens
def create_user():
    """Creates a new user in pixela website"""
    #global user_name
    user_name = input("Enter your username: ")
    token = secrets.token_hex(14)
    data = {
        "username": user_name,
        "token": token,
        "ids": []
    }
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    user_params = {
        "token": token,
        "username": user_name,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    resp = requests.post(url=pixela_url, json=user_params)
    resp.raise_for_status()
    print(resp.json()['message'])

# Step 2: Create a graph definition
def create_graph():
    """Function creates a graph for the user"""

    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Please register your details")
    else:
        user_name = data.get("username")
        id = input("Enter a unique graph id e.g graph1: ")
        name = input("Enter the title of your graph: ")
        units = input("Enter the units of measurement e.g km: ")
        type = input("Should the units be int or float?: ")

        # add the Id to the list. User may have more than one graph
        graph_data = {
            "id": id,
            "unit": units
        }
        data["ids"].append(graph_data)
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        pixela_graph_endpoint = f"{pixela_url}/{user_name}/graphs"
        graph_params = {
            "id": id,
            "name": name,
            "unit": units,
            "type": type,
            "color": "sora",
        }
        headers = {
            "X-USER-TOKEN": data.get("token")
        }
        response = requests.post(url=pixela_graph_endpoint, json=graph_params, headers=headers)
        print(response.json()['message'])

# Step 3: Posting a pixel to the graph
def post_pixel():
    """Post pixel for today"""
    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Register your details!")
    else:
        ids = data.get("ids")
        graph_id = data['ids'][0]['id']
        user_name = data.get("username")
        if len(ids) > 1:
            graph_id = input(f"Which graph are you updating {ids[0]}, {ids[1]}...: ")
        today = dt.datetime.now().strftime("%Y%m%d")
        pixela_post_pixel_url = f"{pixela_url}/{user_name}/graphs/{graph_id}"
        pixel_params = {
            "date": today,
            "quantity": input(f"How many {data['ids'][0]['unit']}s today?: ")
        }
        headers = {
            "X-USER-TOKEN": data.get("token")
        }
        resp = requests.post(url=pixela_post_pixel_url, json=pixel_params, headers=headers)
        resp.raise_for_status()
        print(resp.json()['message'])

# Step 4:  updating the pixel
def update_pixel():
    """For the formation"""
    year = input("Enter the year e.g 2023: ")
    month = input("Enter the month e.g 08: ")
    day = input("Enter the day e.g 28: ")
    quantity = input("Enter quantity: ")
    date = year + month + day

    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Register your details!")
    else:
        ids = data.get("ids")
        graph_id = data['ids'][0]['id']
        user_name = data.get("username")
        if len(ids) > 1:
            graph_id = input(f"Which graph are you updating {ids[0]['id']}, {ids[1]['id']}...: ")
        pixela_put_pixel_url = f"{pixela_url}/{user_name}/graphs/{graph_id}/{date}"
        headers = {
            "X-USER-TOKEN": data.get("token")
        }
        pixela_params = {
            "quantity": quantity
        }
        resp = requests.put(url=pixela_put_pixel_url, json=pixela_params, headers=headers)
        resp.raise_for_status()
        print(resp.json()['message'])
def delete_pixela():
    """Deletes pixela"""

    try:
        with open("data.json", 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Register your details!")
    else:
        year = input("Enter the year e.g 2023: ")
        month = input("Enter the month e.g 08: ")
        day = input("Enter the day e.g 28: ")
        date = year + month + day
        ids = data.get("ids")
        graph_id = data['ids'][0]['id']
        user_name = data.get("username")
        if len(ids) > 1:
            graph_id = input(f"Which graph are you updating {ids[0]['id']}, {ids[1]['id']}...: ")
        pixela_put_pixel_url = f"{pixela_url}/{user_name}/graphs/{graph_id}/{date}"
        headers = {
            "X-USER-TOKEN": data.get("token")
        }
        # Step 5: Deleting one of the pixels
        res = requests.delete(url = pixela_put_pixel_url, headers=headers)
        res.raise_for_status()
        print(res.json()['message'])

def update_details():
    """Updates user details"""
    token = input("Enter your token( More than 10 characters): ")
    username = input("Enter your username: ")
    data = {
        "username": username,
        "token": token,
        "ids": []
    }
    have_a_graph = input("Do you have a graph, yes or no?: ").lower()
    if have_a_graph == 'yes':
        no_graphs = int(input("How many graphs e.g 2: "))
        for _ in range(no_graphs):
            graph_id = input("Enter graph id e.g graph1: ")
            graph_unit = input("Enter the units of the graph e.g Km: ")
            graph_data = {
                "id": graph_id,
                "unit": graph_unit
            }
            data["ids"].append(graph_data)

    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

while True:

    print("What do you want to do today?:\n\t1. Create user\n\t2. Create graph\n\t"
          "3. Post pixela\n\t4. Update pixela\n\t"
          "5. Delete pixela\n\t6. Register your details\n\t7. Exit program\n"
          "Please select number option above e.g 1:\t")
    try:
        user_input = int(input())
    except ValueError:
        pass
    else:
        match user_input:
            case 1:
                create_user()
            case 2:
                create_graph()
            case 3:
                post_pixel()
            case 4:
                update_pixel()
            case 5:
                delete_pixela()
            case 6:
                update_details()
            case 7:
                break



