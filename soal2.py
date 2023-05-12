text = input('text to be replaced : ')
oldText = input('old text to be replaced : ')
newText = input('replacement text : ')

if oldText in text:
    replaceText = text.replace(oldText, newText)
    print(replaceText)