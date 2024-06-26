
while True:
    import Firelink
    print(' - hackerrank\n - python_tutorial\n - quran \n choose a website name from the above list or terminate:', end=" ")
    website=input()
    if website=='terminate':
        exit()
    else:
        Firelink.Firefox(website)




