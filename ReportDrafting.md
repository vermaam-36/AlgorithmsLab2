#  Decision Rule  
Given a 100x100 2D plane. For any polygon with points {p1, p2...pn} n >= 3 and point m {x,y} 0 <= x <= 100, 0 <= y <= 100.  
Let 4 lines be drawn outward from point m, one vertical up, one vertical down, one horizontal right, one horizontal left.  
If all 4 lines touch at least one line created by the polygon points {p1, p2...pn} then the point m lies within the polygon  
else point m lies outside the polygon  