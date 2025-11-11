height = float(input("enter the height in cm"))
        
if height < 150:
    print ("you are short")
elif 150 <= height < 170:
    print ("You have an average height")
elif 170 <= height < 185:
    print ("you are tall")
else:
    print("you are very tall.")