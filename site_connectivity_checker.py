import urllib.request as urllib
def connectivity_checker(url):
    print("This function simply checks the connectivity and status of a url \n")

    print("checking connectivity......")
    try:
        response = urllib.urlopen(url)
    except:
        print("No connection established")
    else:
        print("\nConnected to ", url, "successfully")
        print("The respose code was: ", response.getcode())

url = input("Enter your urls to check the connectivity status: ")
connectivity_checker(url)