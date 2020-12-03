#def foo(name):
    #return "Hi %s" % name.title()
    #This will make the first letter of the name uppercase 


def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalize = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalize)
    else:
        return "{}.".format(capitalize)

#print(sentence_maker("how are you"))

results = []
while True:
    user_input = input("Say something:")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))