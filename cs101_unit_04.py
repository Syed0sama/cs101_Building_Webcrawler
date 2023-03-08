import pdb
pdb.set_trace()

def add_to_index(index,keyword,url):
    for entry in index:
        if  entry[0]==keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index,keyword):
    for entry in index:
        if entry[0]==keyword:
           return entry[1]
    return []
def add_page_to_index(index,url,content):
    words=content.split()
    for word in words:
        add_to_index(index,word,url)


index=[]
add_page_to_index(index,
        'https://stackoverflow.com',
        'This is a function that my teammate is using to check the links in an HTML page to see if it is broken or not.')

add_page_to_index(index,
        'https//syed0sama.github.io',
        'This is my cv resume is in this page and this is based on HTML')

print index

"""
index:[]
url:'https://stackoverflow.com'
content:'This is a function that my teammate is using to check the links in an HTML page to see if it is broken or not.'
words: ['This', 'is', 'a', 'function',...,'not.']
word: 'This'

the following is inside add_to_index function
keyword:'This'
index before: []
index after : [['This',['https://stackoverflow.com']]]

the following is inside the add_page_to_index function
word: 'is'





the following is inside add_to_index function
keyword: 'is'
index before : [['This',['https://stackoverflow.com']]]
index : [['This',['https://stackoverflow.com']],['is',['https://stackoverflow.com']]]
...

calling add_page_to_index with another url(line 27)

index : [['This',['https://stackoverflow.com']],['is',['https://stackoverflow.com']]]
content:'This is my cv resume is in this page and this is based on HTML'
words: ['this','is',....'HTML']
word: 'This'

the following is inside add_to_index function
keyword: 'This'
index before:[['This',['https://stackoverflow.com']],['is',['https://stackoverflow.com']]]
index after: [['This',['https://stackoverflow.com','syed0sama.github.io']],['is',['https://stackoverflow.com']]]
"""
