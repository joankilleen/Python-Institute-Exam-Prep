def greeting(word):
    greeting_word = str(word)
    if word is None:
        raise AssertionError("Not a valid greeting!")

    def generate(applyTo):
        if applyTo is None:
            raise AssertionError(greeting_word + " " + "cannot be applied to: " + "None")
        return greeting_word.title() + " " + applyTo.title() + "!"
    return generate

hello = greeting("hello")

print(hello("Joan"))