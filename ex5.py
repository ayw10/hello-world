# conversions
inches_to_cm = 2.54
lbs_to_kg = 0.453592

name = 'Alice'
age = 26 # not a lie
height = 63 # inches
height_cm = height * inches_to_cm
weight = 120 # lbs
weight_kg = weight * lbs_to_kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d centimeters tall." % height_cm
print "She's %d pounds heavy." % weight
print "She's %d kilograms." % weight_kg
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes.lower(), hair.lower())
print "Her teeth are incredibly %s." % teeth.lower()

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)