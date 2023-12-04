def main():
    print("Welcom to my email slicer")
    email = input("Please enter your email: ")
    username, domain = email.split("@")
    domain, extention = domain.split(".")
    print("Username: " + username)
    print("Domain: " + domain)
    print("Extention: " + extention) 

# make it run continously with a while loop
main()