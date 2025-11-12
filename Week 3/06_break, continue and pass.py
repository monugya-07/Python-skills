# break, continue and pass

email = input()

for i in email:                     
    if i == "@":
        break                       # break after @, suppose xyz123@google.com
    # print(i)
    print(i, end = '')              # xyz123



email = input()

for i in email:
    if i == "@":
        continue
    # print(i)
    print(i, end = '')              # xyz123google.com


# What is pass?

# pass is a null statement — it does nothing when executed.
# It’s used as a placeholder where a statement is required syntactically, but you don’t want any code to run yet.

for i in range(11):
    if i%3 == 0:
        print(i)
    else:
        pass                          


for i in range(5):
    pass                             # Loop runs, but does nothing

print("Loop finished")


num = 10

if num > 0:
    pass                             # Placeholder for future code
else:
    print("Negative number")

