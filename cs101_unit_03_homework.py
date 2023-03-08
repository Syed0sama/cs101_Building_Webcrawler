"""
Question 1 - Search Engines and the Web
Fill in initial values of the elements of p to produce the behaviour shown below:

    p = [?,?,?]

    p[0] = p[0] + p[1]
    p[1] = p[0] + p[2]
    p[2] = p[0] + p[1]

    print p
    When your values of p are acceptable, the output should be:

        [1, 2, 3]
        
"""

p = [1,0,1]

p[0] = p[0] + p[1]
p[1] = p[0] + p[2]
p[2] = p[0] + p[1]

#print p


"""
 # Define a procedure, product_list,
 # takes as input a list of numbers,
 # and returns a number that is
 # the result of multiplying all
 # those numbers together.

 def product_list():

 #print product_list([9])
 #>>> 9

 #print product_list([1,2,3,4])
 #>>> 24

 #print product_list([])
 #>>> 1
"""

def product_list(numbers):
    total=1
    for entry in numbers:
        total=total*entry
    return total

print product_list([1,2,4,3])



"""
Question 4 - Greatest
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest():

    #greatest([4,23,1])
    #>>> 23
    #greatest([])
    #>>> 0
"""


def greatest(q):
    big=0
    for i in q:
        if i>big:
            big=i
    return big
        

#print greatest([12,45,9,10])
"""
Question 5 - Lists of Lists
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).
"""

def total_enrollment(q):
    total_student=0
    tution_fee=0
    for name,student,tution in q:
        total_student=total_student+student
        tution_fee=tution_fee+ (student*tution)
    return total_student,tution_fee


#usa_universities=[ ['california',274,1000],['virginia',200,1500]]

def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return ('<html> <body> This is a test page for learning to crawl! '
            '<p> It is a good idea to '
            '<a href="http://www.udacity.com/cs101x/crawling.html">learn to '
            'crawl</a> before you try to  '
            '<a href="http://www.udacity.com/cs101x/walking.html">walk</a> '
            'or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. '
            '</p> </body> </html> ')
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return ('<html> <body> I have not learned to crawl yet, but I '
            'am quite good at '
            '<a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>.'
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return ('<html> <body> I cant get enough '
            '<a href="http://www.udacity.com/cs101x/index.html">crawling</a>! '
            '</body> </html>')
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return ('<html> <body> The magic words are Squeamish Ossifrage! '
            '</body> </html>')
    except:
        return ""
    return ""

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed,max_pages):
    tocrawl = [seed]
    crawled = []
    while tocrawl and len(crawled)<max_pages:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled

print crawl_web("http://www.udacity.com/cs101x/index.html",4) 






