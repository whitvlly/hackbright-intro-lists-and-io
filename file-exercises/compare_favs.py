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