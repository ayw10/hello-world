tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split \non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "\a"
print "this is a test\b"
print "\f"
print "\n"
print u"\N{arc}"
print "I think I need some \r ASCII lines to test this."
print "\t ASCII why do I need the ASCII part?"
print u"color \u002D"
print "what in the world \v is a vertical tab???"
print "I still don't get what an \o00 octal value is."


# while True:
#	for i in ["/","-","|","\\","|"]:
#		print "%s\r" %i,

string = "you would need to escape out of those characters."		
print "I guess the main point is if you actually wanted to type the characters \'%%s', %s" % string

print "I think this last drill is saying, %r" % "\"Do this.\""
print "I think this last drill is saying, %s" % "\"Do this.\""