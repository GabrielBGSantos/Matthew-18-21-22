from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        print(f"Trying password: {password}...")
        zf_handle.extractall(pwd=bytes(password, 'utf-8'))
        print(f"\n\033[0;32mPassword found!: {password}\033[0m\n")
        return password
    except:
        return

def main():
    wordlist = "rockyou.txt" #Insert your wordlist name here
    file = "enc.zip" #Insert your zip name here
    passwords = []
    print("[+] Beginning bruteforce ")
    with ZipFile(file) as zf:
        with open(wordlist, 'r') as f:
            for word in f:
                word = word.strip()
                passwords.append(attempt_extract(zf, word))
    passwords = [item for item in passwords if item]           
    if len(passwords) == 0:
        print("[+] Password not found in list")
    else:
        print("\nPasswords found: ")
        for psw in passwords:
            print(f"{psw}, ")

if __name__ == "__main__":
    main()