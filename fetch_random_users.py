import requests
import json
import pandas as pd
import time

def fetch():
    url = "https://randomuser.me/api/?results=1000"
    wait = 5
    
    for i in range(3):
        try:
            resp = requests.get(url)
            if resp.status_code == 200:
                data = resp.json()
                return data["results"]
            else:
                print("Error - Bad response from server")
        
        except Exception as e:
            print("Error fetching data - ", e)
        
        print("Retrying in - ", wait)
        time.sleep(wait)
    
    return None

def to_json(data):
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved to users.json")

def to_csv(data):
    if not data:
        print("No data")
        return
    
    df = pd.json_normalize(data)
    df.to_csv("users.csv", index=False)
    print("Data saved to users.csv")

def main():
    a = fetch()
    if a:
        to_json(a)
        to_csv(a)

if __name__ == "__main__":
    main()
