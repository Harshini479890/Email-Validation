email = input("Enter your email: ")  # Example: g@g.in , wscube@gmail.com
k, j, d = 0, 0, 0

if len(email) >= 6:  # Condition 1: Length should be at least 6
    if email[0].isalpha():  # Condition 2: First character must be a letter
        if ("@" in email) and (email.count("@") == 1):  # Condition 3: Must contain one '@'
            if email[-4] == "." or email[-3] == ".":  # Condition 4: Last 3rd or 4th character must be '.'
                for i in email:
                    if i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i in "_@.":
                        continue
                    else:
                        d = 1

                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email (Invalid Characters)")
                else:
                    print("Valid Email")
            else:
                print("Wrong Email (Invalid Dot Placement)")
        else:
            print("Wrong Email (Invalid '@' Count)")
    else:
        print("Wrong Email (First Character Must Be a Letter)")
else:
    print("Wrong Email (Too Short)")