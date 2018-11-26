import pyperclip
pyperclip.copy('the text tp be copied to the clipboard.')
spam = pyperclip.paste()

if not pyperclip.is_available():
    print("copy not found")
else: print("copy found and ready")
