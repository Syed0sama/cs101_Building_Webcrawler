import urllib2

response = urllib2.urlopen("https://www.wikipedia.org/")

pageinfo = response.read()
def get_next_link(page):
   start_link=page.find('<a href=')
   if start_link==-1:
     return None,0
   start_quote=page.find('"',start_link)
   end_quote=page.find('"',start_quote+1)
   url=page[start_quote+1:end_quote]

   return url,end_quote

def print_all_links(page):
  lllinks=''
  while True:
      url,endpos=get_next_link(page)
      if url:
        lllinks=lllinks+url; 
        #print url 
        page=page[endpos:]
      else:
         break
  return lllinks


final=print_all_links(pageinfo)
#print final


string="My, name. is abubbakar"
lists=string.split()
print lists
print lists[0]


elements={'hydrogen':1,'Helium':2}

print elements['hydrogen']
elements['lithium']=4
print elements['lithium']
