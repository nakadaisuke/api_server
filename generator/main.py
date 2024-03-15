import os, requests, time, json

user_list = ["/user", "/user/0001", "/user/0001/user_name", "/user/0001/email", "/user/0001/card", "/user/0001/phone", "/user/0001/address/zip", "/user/0001/address/pref", "/user/0001/address/local_address"]
service_list = ["/service/pref_list", "/service/user_number", "/service/user_pref"]
post_list = ["/user"]
delete_list = ["/user"]

def get_test():
    for i in user_list:
        url = "http://" + os.getenv("url") + i
        r = requests.get(url)
        data = r.json()

        if "user" in data:
            print('ok')
        else:
            print('error')

        time.sleep(1)

    for i in service_list:
        url = "http://" + os.getenv("url") + i
        r = requests.get(url)
        data = r.json()

        if "service" in data:
            print('ok')
        else:
            print('error')

        time.sleep(1)


def post_test():
    for i in post_list:
        url = "http://" + os.getenv("url") + i
        data = {"userid":"0004","name":"test name","email":"test@test.com","card":"1111-2222-3333-4444","phone":"03-1234-5678","zip": "1234566","pref": "tokyo", "local_address": "123 1231 123"}
        json_data = json.dumps(data)

        r = requests.post(url, data = json_data)

        r_data = r.json()
        if "user" in r_data:
            print('ok')
        else:
            print('error')

        time.sleep(1)

def delete_test():
    for i in delete_list:
        url = "http://" + os.getenv("url") + i + "/0004"
        r = requests.delete(url)
        data = r.json()

        if "user" in data:
            print('ok')
        else:
            print('error')

        time.sleep(1)

if __name__ == "__main__":
    while(True):
        get_test()
        post_test()
        delete_test()