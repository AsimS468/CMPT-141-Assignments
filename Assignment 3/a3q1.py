print("Enter email address:")
email = str(input())

#if statements for determining if inputted email is valid
if (email.find("@") == -1):
    print('Invalid email address.')
elif (email.find(".") == -1):
    print('Invalid email address.')
else:
    email.index("@")
    username = email[:email.index("@")]
    print("Username: " + username)  
    
    FQD = email.find(".")
    subDomain = email.index(".", FQD+1)
    #
    domain = email[email.index(".", FQD+1)+1:]
    print("First Subdomain/Domain: " + domain)  


