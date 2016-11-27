###Terminal options:
-sa --show_approx              (shows approximation quotients)
-ax --axis                     (smooth axes)
-hg --hide_grid                (don't show grid)
-sp --show_podgon              (shows podgonian results)

###Input file options:
cp                             (connects points on the graph)
form <form>                    (defines appearance of the points)
ap <degree>                    (approximation degree)
err <err1, err2, ... ,errx>    (errors)
∇ <mes1, mes2>                 (nabla-podgon: gives right answer, according to the two trusty measurements)
Δ <desired_quotient>           (delta-podgon: gives right answer, if desired quotient is known)

###Input file example:
a x 1 2 3 4 5 form rd cp err 0.1
a y 1 2 3 4 6
b x 1 2 3 4 5 ap 1 form rd Δ 1 err 0.1 0.2 0.3 0.4 0.5
b x 1 2 3 4 6
c x 1 2 3 4 5 ap 1 form rd ∇ 2 3
c x 1 2 3 4 6

###Variety of forms(for form option):
##Consist of <color><form>
##Colors:
'b'  	blue
'g' 	green
'r' 	red
'c' 	cyan
'm' 	magenta
'y' 	yellow
'k' 	black
'w' 	white
##Forms:
'-' 	solid line style
'--' 	dashed line style
'-.' 	dash-dot line style
':' 	dotted line style
'.' 	point marker
',' 	pixel marker
'o' 	circle marker
'v' 	triangle_down marker
'^' 	triangle_up marker
'<' 	triangle_left marker
'>' 	triangle_right marker
'1' 	tri_down marker
'2' 	tri_up marker
'3' 	tri_left marker
'4' 	tri_right marker
's' 	square marker
'p' 	pentagon marker
'*' 	star marker
'h' 	hexagon1 marker
'H' 	hexagon2 marker
'+' 	plus marker
'x' 	x marker
'D' 	diamond marker
'd' 	thin_diamond marker
'|' 	vline marker
'_' 	hline marker