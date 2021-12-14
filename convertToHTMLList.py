# function to convert list into HTML code
def ulify(filename, streamingService):
    file = open(filename, "r")
    list_of_lists = []
    string = ""
    for line in file:
        stripped_line = line.strip()
        list_of_lists.append(stripped_line)
    for s in list_of_lists:
        string += "<li>" + str(s) + " - " + streamingService + "</li>\n"  # Dette kunne også være et argument, det
    file.close()
    return string


output = ulify("finalTV2Play.txt", "TV2Play")

file = open("ulList.txt", "a")
file.write(output)

output = ulify("finalDRTV.txt", "DRTV")
file.write(output)

file.close()
