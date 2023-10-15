def main(a):
    a=a.strip().lower()
    if a.endswith(".jpg") or a.endswith(".jpeg"):
        print("image/jpeg")
    elif a.endswith(".png"):
        print("image/png")
    elif a.endswith(".gif"):
        print("image/gif")
    elif a.endswith(".zip"):
        print("application/zip")
    elif a.endswith(".pdf"):
        print("application/pdf")
    elif a.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")




main(input("File name: "))