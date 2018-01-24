print ('Welcome to nrityashakti academy')
loop='true'
while(loop=='true'):
    username=input("Username please:")
    password=input("Password please:")
    if(username=="nrityashakti" and password=="nrityashaktipassword"):
        print ('Logged in successfully as  '+username)
        loop='false'
        loop1='true'
        while(loop1=='true'):
            command=input(username+">>>>>")
            if(command=="exit" or command=="Exit"):
                break
            else:print ("'"+ command+ " is not a valid command!")
    else:
         print ('Invalid details')
