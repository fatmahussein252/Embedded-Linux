import webbrowser

url_dic={'hackerrank': 'https://www.hackerrank.com/skills-verification/problem_solving_basic',
        'python_tutorial': 'https://docs.python.org/3.12/tutorial/index.html',
        'quran': 'https://equran.me/read-2.html'}

def Firefox(website):
        if website in url_dic:         
                webbrowser.open_new_tab(url_dic.get(website))
        else:
                print("website not found")
 