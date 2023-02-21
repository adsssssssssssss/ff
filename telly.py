try:
    import requests
    from os import system

    system("title " + "By Hashem")

except Exception as m:
    print(m)
    input("Press Any Key To Exit...\n")

print("""                                     
        Tellonym Username Checker by Hashem
        
                        """)

input("Press any Key to start..\n")

a = requests.Session()

ggg = open("User.txt", "r")

co = 0
do = 0
fa = 0

while 1:
    user = ggg.readline().split("\n")[0]
    if user == "":
        break
    url = f"https://tellonym.me/{user}"

    head = {
        'Host': 'tellonym.me',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
    }


    re = a.get(url, headers=head)

    if re.status_code == 404:
        if len(user) >= 4:
            co += 1
            do += 1
            print(f"[+] Found >> {user} : Checked: {co}")
            with open("Found.txt", "a") as result:
                result.write(f"{user}\n")
        else:
            co += 1
            fa += 1
            print(f"[-] Taken >> {user} : Checked: {co}")
    elif re.status_code == 200:
        co += 1
        fa += 1
        print(f"[-] Taken >> {user} : Checked: {co}")

print(f"Found: {do} : Taken: {fa} : Checked: {co}\nTellyonm Username Checker by Hashem\nSaved All in Found.txt\n")

input("Press any Key to Exit...\n")