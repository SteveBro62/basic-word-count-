import sys
def nr_bytes(string):
    return len(text.encode("utf-8")) + nr_lines(string)
def nr_lines(string):
    return string.count("\n")
def nr_words(string):
    return len(string.split())
def nr_characters(string):
    return len(string) + nr_lines(string) 
lst = input().split()
if len(lst) > 2:
    sys.exit("Error: Too many words.")       
text = ""
if len(lst) == 1:
    file_name = lst[0]
    try:
        with open(f"{file_name}", "r", encoding="utf-8") as file:
            text = file.read()
    except:
        sys.exit("Error: File is missing or the encoding is wrong")
    print(f" {nr_lines(text)} {nr_words(text)} {nr_bytes(text)} {file_name}")
else:
    file_name = lst[1]
    try : 
        with open(f"{file_name}", "r", encoding="utf-8") as file:
            text = file.read()
    except:
        sys.exit("Error: File is missing or the encoding is wrong")
    if lst[0] == "-c":
        print(f"{nr_bytes(text)}   {file_name}")
    elif lst[0] == "-l":
        print(f"{nr_lines(text)}   {file_name}")
    elif lst[0] == "-w":
        print(f"{nr_words(text)}   {file_name}")
    elif lst[0] == "-m":
        print(f"{nr_characters(text)}   {file_name}")
    else:
        sys.exit("Error: Unknown command.")