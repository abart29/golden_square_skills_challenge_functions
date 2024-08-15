def make_snippet(str):
    new_string = str.split(" ")
    if len(new_string) <= 5:
        return " ".join(new_string)
    elif len(new_string) > 5:
        return " ".join(new_string[:5]) + "..."
