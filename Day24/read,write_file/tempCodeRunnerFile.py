with open('file.txt', encoding="utf-8") as f:
    read_data = f.read()
    print(read_data)

    f.close()