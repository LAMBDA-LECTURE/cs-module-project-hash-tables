def word_count(s):
    # Your code here
    dictionary = {}
    s_list = s.split()
    for word in s_list:
        word = word.strip('":;,.-+=/\\|[]}{()*^&')
        if word == '':
            continue
        word = word.lower()
        if word not in dictionary:
            dictionary[word] = 1
        else:
            dictionary[word] += 1
    return dictionary

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))