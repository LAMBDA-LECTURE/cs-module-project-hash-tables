def no_dups(s):
    # Your code here
    s_list = s.split()
    output = ""
    for word in s_list:
        if output.find(word) == -1:
            output = output + word + " "
    return output.strip(" ")


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))