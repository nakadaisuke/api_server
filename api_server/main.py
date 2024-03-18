import uvicorn
import csv
import json
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
filename = "user_data.csv"

class Item(BaseModel):
    userid: str
    name: str
    email: str
    card: str
    phone : str
    zip : str
    pref : str
    local_address : str


@app.get("/user")
def get_item():
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    userid = [d.get('userid') for d in content]
    username = [d.get('name') for d in content]
    user_dict = dict()
    for k in userid:
        for v in username:
            user_dict[k] = v

    json_dict = {"user": user_dict}
    return json_dict


@app.get("/user/{item_name}")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i}
            return json_dict

@app.get("/user/{item_name}/user_name")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i["name"]}
            return json_dict

@app.get("/user/{item_name}/email")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i["email"]}
            return json_dict

@app.get("/user/{item_name}/card")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i["card"]}
            return json_dict

@app.get("/user/{item_name}/phone")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i["phone"]}
            return json_dict

@app.get("/user/{item_name}/address/zip")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i["zip"]}
            return json_dict

@app.get("/user/{item_name}/address/pref")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i["pref"]}
            return json_dict

@app.get("/user/{item_name}/address/local_address")
def get_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == item_name:
            json_dict = {"user": i["local_address"]}
            return json_dict

@app.post("/user")
def post_item(body: Item):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    for i in content:
        if i["userid"] == body.userid:
            return {"error": "The data is already exist"}

    csvdata = [body.userid, body.name, body.email, body.card, body.phone, body.zip, body.pref, body.local_address]

    with open(filename, encoding='utf8', mode='a') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(csvdata)

    return {"user": body}

@app.delete("/user/{item_name}")
def delete_item(item_name):
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    i = 0
    csvdata = []

    if item_name not in [d.get('userid') for d in content]:
        return {"error": "The data is not exist"}

    for k in [d.get('userid') for d in content]:
        if k != item_name:
            data = list(content[i].values())
            csvdata.append(data)
            i = i + 1
        else:
            i = i + 1

    with open(filename, encoding='utf8', mode='w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(["userid","name","email","card","phone","zip","pref","local_address"])

    for i in csvdata:
        with open(filename, encoding='utf8', mode='a') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(i)

    return {"user": {"delete": item_name}}

@app.get("/service")
def get_item():
    return {"service": ["perf_list", "user_number","user_pref"]}

@app.get("/service/pref_list")
def get_item():
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    pref_all = [d.get('pref') for d in content]
    pref_unique = []
    for v in pref_all:
        if v not in pref_unique:
            pref_unique.append(v)

    json_dict = {"pref": pref_unique}
    return json_dict

@app.get("/service/user_number")
def get_item():
        with open(filename, encoding='utf8', newline='') as f:
            csvreader = csv.DictReader(f)
            content = [row for row in csvreader]

        user_number = len([d.get('userid') for d in content])
        json_dict = {"user number": user_number}
        return json_dict

@app.get("/service/user_pref")
def get_item():
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.DictReader(f)
        content = [row for row in csvreader]

    user_data = {}
    i = 0
    for k in [d.get('pref') for d in content]:
        if k not in user_data:
            user_id = [d.get('userid') for d in content][i]
            user_name = [d.get('name') for d in content][i]
            data = {k: [{"user_id": user_id, "name": user_name}]}
            user_data.update(data)
            i = i + 1
        else:
            user_id = [d.get('userid') for d in content][i]
            user_name = [d.get('name') for d in content][i]
            data = [{"user_id": user_id, "name": user_name}]
            user_data[k].append(data)

    return user_data

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
