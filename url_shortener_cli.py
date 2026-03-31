import json
import random
import string
from pathlib import Path

file_name = "urls.json"

def load_data():
    path = Path(file_name)

    if path.exists():
        try: 
            f = open(file_name, "r")
            data = json.load(f)
            f.close()
            return data
        except:
            print("file issue... starting fresh")
            return {}
    else:
        return {}
    
def save(sv):
    try:
        f = open(file_name , "w")
        json.dump(sv,f,indent = 2)
        f.close()
    except:
        print("Error while saving")

def code_gen():
    chars = string.ascii_letters + string.digits
    code = ""
    i = 0

    while(i < 6):
        code = code + random.choice(chars)
        i += 1

    return code
def shorten(sv,long_URL):
    for c in sv:
        if sv[c] == long_URL:
            return c
    
    code = code_gen()

    while True:
        if code not in sv:
            break
        else:
            code = code_gen()

    sv[code] = long_URL

    save(sv) 

    return code

def expand(sv,code):
    if code in sv:
        return sv[code]
    return None

def main():
    print("URL Shortener")
    print("------------------------")
    print("commands : shorten, expand, list, help, quit\n")

    sv = load_data()
    
    while True:
        user_input = input("> ")

        if user_input == "":
            continue                 #Ignoring Blank input by the user
        parts = user_input.strip().split(" ")
        command = parts[0].lower()

        if command == "quit":
            print("closing program...")
            break

        elif command == "help":
            print("shorten <url>")
            print("expand <code>")
            print("list")
            print("quit")

        elif command == "list":
            if len(sv) == 0:
                print("no urls yet")
            else:
                print("saved urls:")
                for k in sv:
                    print(k + " -> " + sv[k])

        elif command == "shorten":
            if len(parts) < 2:
                print("Enter url pls")
                continue

            url = ""
            for i in range(1,len(parts)):
                url += parts[i]
                if i != len(parts) - 1:
                    url += " "

            code = shorten(sv,url)

            print("short code is: ",code)
            print("use:", "http://short.com/" + code)

        elif command == "expand":
            if len(parts) <2:
                print("enter code")
                continue

            code = parts[1]

            result = expand(sv,code)

            if result != None:
                print("Original: ",result)
            else:
                print("not found")

        else:
            print("unknown command type(help)")

if __name__ == "__main__":
    main()