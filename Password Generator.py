import string
import random
while True:
    if __name__=="__main__":
        s1 = string.ascii_uppercase
        s2 = string.ascii_lowercase
        s3 = ["@",".","_","-",]
        s4 = string.digits

        p1 = int(input("\nEnter Number of Uppercase Alphabets in PassWord\n \
                    (If don't want any type '0') : "))
        p2 = int(input("\nEnter Number of Lowercase Alphabets in PassWord\n \
                    (If don't want any type '0') : "))
        p3 = int(input("\nEnter Number of Special Charaters in PassWord\n \
                    (If don't want any type '0') : "))
        p4 = int(input("\nEnter Number of digits in PassWord\n \
                    (If don't want any type '0') : "))
        
        l1 = []
        l2 = []
        l3 = []
        l4 = []

        l1.append(list(s1))
        l2.append(list(s2))
        l3.append(s3)
        l4.append(list(s4))

        # random.shuffle(s1)
        x1 = ("".join(random.sample(s1, p1)))
        
        # random.shuffle(s2)
        x2 = ("".join(random.sample(s2, p2)))
        
        # random.shuffle(s3)
        x3 = ("".join(random.sample(s3, p3)))
        
        # random.shuffle(s4)
        x4 = ("".join(random.sample(s4, p4)))
        
        x = x1 + x2 +x3 + x4
        print("\n\nYour Password is : ",x)
    
    z = input("\n\nWant To Generate Another Password (yes/no) : ").lower()

    if z != "yes" :
        break
print("Thank You !!")
