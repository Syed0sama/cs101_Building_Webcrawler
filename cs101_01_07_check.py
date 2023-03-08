print 299792458*100*(1.0/1000000000)
speed_of_light=299792458
cycles_per_second=2700000000.0
answer=(speed_of_light/cycles_per_second)
print answer


hours=9
hours=hours+1
hours=hours*2
print hours


year=365
age=28
number_of_days_alive=year*age
print number_of_days_alive

name="Syed Muhammad Osama"
print name


s="audacity"
print "U"+ s[2: ]





page=('<div id="top_bin"><div id="top_content" class="width960">'
        '<div class="udacity float-left"><a href="http://udacity.com">')
start_link= page.find("<a href=")
start=page.find('"',start_link)
end=page.find('"',start+1)
url=page[start+1:end]
print url
print page.find("i", 1)

