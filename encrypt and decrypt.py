#Written and Developed By Maimo Harris Alias Vlad Dracula
print('''Make a Choice
[+]:1 Encryption
[+]:2 Decryption
''')
choice = int(input("Enter Choice:"))
array=[' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o','p','q','r','s','t','u','v','w','x','y','z','&','$','%','@']
if choice==1:
    data=input("Enter Data To be encrypted:").lower()
    key=input("Enter Encryption key:")
    index=0
    str=""
    for i in data:
        if i in array and array.index(i)<len(array)-3:
            index=array.index(i)
            str=str+array[index+3]
    dbw=open('database.txt','w')
    dbw.write(str+':'+key)
elif choice==2:
    verify=input("Enter Data Associated Keys to Decrypt Data:")
    dbr=open('database.txt','r')
    data=dbr.readline()
    keys=data.split(':')[1]
    encrypted=data.split(':')[0]
    if verify==keys:
        str=""
        print("Data to be decrypted is:"+encrypted)
        print("Decrypting Data......")
        for i in encrypted:
            if i in array:
                index=array.index(i)
                str=str+array[index-3]
        print("Data Decryption Successful")
        print("Results is:"+str)