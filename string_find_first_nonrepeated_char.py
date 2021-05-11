# How do you print the first non-repeated character from a string?
# Example: helloworldandhello ==> w

s = "helloworldandhello"

l = list(s)
for i in range(len(l)):
    if l.count(l[i]) == 1:
        print('the first non-repeated char is the ' + str(i+1) + 'th char : ', l[i])
        break