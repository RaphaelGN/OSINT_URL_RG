def transformation_text_sauvergarde(toto):
    file = open("resultat.txt", "w+")

    # Saving the array in a text file
    content = str(toto)
    file.write(content)
    file.close()

    # Displaying the contents of the text file


# file = open("sample.txt", "r")
# content = file.read()

# print("Array contents in sample.txt: ", content)
# file.close()
