num_list = []
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        else:
            num_list.append(int(num))
    except:
        print("Please enter only numbers next time")
        quit()
print(num_list)
print("Maximum: ", max(num_list))
print("Minimum: ", min(num_list))
