# dd2-P1-Polygans ( Project 1: Deep Dive Python 3 Part2 )

## GOAL 1

Create a **Polygon** class:


### Initializer
+ number of edges/vertices
+ circumradius

### Properties
+ \# edges
+ \# vetices
+ interior angle
+ edge length
+ apothem
+ area
+ perimeter

### Functionality
+ a proper representation(`__repr__`)
+ implements equality(`==`) based on \# vertices and circumsradius(`__eq__`)
+implements `>` based on number of vertices only(`__gt__`)

## Goal 2

Implement a Polygons sequence type:

### Initializer
+ number of vertices for largest polygon in sequence
+ common circumradius for all plygons

### Properties
+ max efficiency  polygon: returns the Polygon with the highest `area : perimeter` ratio
+ support the `len()` function(`__len__`)
