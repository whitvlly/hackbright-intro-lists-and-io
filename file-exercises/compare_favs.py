whit = open("whitney_fav_foods.txt")
gul = open("gulmira_fav_foods.txt")
whitney_favs = whit.readlines()
gulmira_favs = gul.readlines()
print whitney_favs
print gulmira_favs
whit.close()
gul.close()
def compare_favs(whitney_favs, gulmira_favs):
	if (whitney_favs == gulmira_favs):
		print "Our favorite foods are the same!"
	print "Our foods are different"
compare_favs(whitney_favs, gulmira_favs)



def compare_favs2(whitney_favs, gulmira_favs):
	if gulmira_favs[0] in whitney_favs:
		print "We both love", gulmira_favs[0]
	elif gulmira_favs[1] in whitney_favs:
		print "We both love", gulmira_favs[1]
	elif gulmira_favs[2] in whitney_favs:
		print "We both love", gulmira_favs[2]

compare_favs2(whitney_favs, gulmira_favs)

fav_foods = open("whitney_fav_foods.txt"), ("gulmira_fav_foods.txt")

def read_files(file1):
	foodfile = open(file1) 
	favs = foodfile.readlines()	
	foodfile.close()
	print favs

read_files("whitney_fav_foods.txt")
read_files("gulmira_fav_foods.txt")