import functions

def find_distance(point, line):                                                    # Briskoume thn eukleidia apostash shmeiou apo eutheia
    x1, y1 = line[0]
    x2, y2 = line[1]
    x0, y0 = point
    return abs((y2-y1)*x0 - (x2-x1)*y0 + x2*y1 - y2*x1) / ((y2-y1)**2 + (x2-x1)**2)**0.5

def find_furthest_point(A, B, S):                                                  # Briskoume to shmeio pou apexei perissotero apo thn AB
    max_distance = 0                                                               # Arxikopoioume thn megisth apostash
    furthest_point = None                                                          # Arxikopoioume to trexon shmeio
    for point in S:                                                                # Gia kathe shmeio 
        distance = find_distance(point, (A, B))                                    # Briskoume thn apostash tou shmeiou apo thn eutheia
        if distance > max_distance:                                                # An h apostash einai megaluterh apo auth pou exoume hdh brei
            max_distance = distance                                                # Ananewnoume thn megisth apostash 
            furthest_point = point                                                 # Allazoume to shmeio 

    return furthest_point                                                          # Epistrefoume to shmeio 

##################################################################################################################################################################################

def points_right_of_line(A, B, points):                                            # Epistrefoume ta shmeia pou einai deksia apo thn euteia AB
    return [point for point in points if functions.CCW(A,B,point) != 2]

def find_min_max_y(points):                                                        # Briskei ta shmeia me thn megaluterh kai mikroterh tetagmenh
    if len(points) == 0:                                                           # An to sunolo einai keno epistrefoume None
        return None, None  

    min_point = max_point = points[0]                                              # Arxikopoioume to max, min points me to prwto shmeio
    min_y = max_y = points[0][1]                                                   # Arxikopoioume kai thn min kai thn max y-suntetagmenh me thn y-suntetagmenh tou prwtou shmeiou 

    for point in points[1:]:                                                       # Gia ola ta shmeia
        y = point[1]                                                               # Kratame thn y suntetagmenh tou trexontos shmeiou                                                 
        if y < min_y:                                                              # An einai mikroterh apo to prohgoumeno shmeio
            min_y = y                                                              # Ananewnoume to elaxisto stoixeio kai thn antistoixh suntetagmenh tou 
            min_point = point
        elif y > max_y:                                                            # Elegxoume an to trexon shmeio exei megaluterh tetagmenh apo to prohgoumeno an isxuei 
            max_y = y                                                              # Ananewnoume to maximum stoixeio
            max_point = point

    return min_point, max_point                                                    # Epistrefoume to max kai to min stoixeio

##################################################################################################################################################################################

def point_inside_quadrilateral(quadrilateral, points):                             # Exei orismata tis korufes enos tetrapleurou kai ena sunolo shmeiwn epistrefei ta shmeia pou den anhkoun sto eswteriko tou tetrapleurou
    not_inside_points = []
    for point in points:                                                           # Gia kathe shmeio apo to sunolo 
        for i in range(4):                         
            x1, y1 = quadrilateral[i]                                              
            x2, y2 = quadrilateral[(i + 1) % 4]
            if functions.CCW((x1,y1), point, (x2,y2)) != 1:                        # Elegxoume an to shmeio einai sthn idia pleura ths kathe korufhs
                not_inside_points.append(point)                                    # Bazoume to shmeio sthn lista
    not_inside_points = list(dict.fromkeys(not_inside_points))                     # Afairoume diplotupa an uparxoun 

    return not_inside_points                                                       # Epistrefoume to sunolo twn shmeiwn

def QuickHull(A, B, S):                                                            # Ektelei ton algorithmo Quick Hull
    if len(S) <= 2:                                                              
        return [A, B]                              
    else:                                                                          # An exoume sunolo me panw apo 3 shmeia
        furthest_point = find_furthest_point(A, B, S)                              # Briskoume to shmeio G pou apexei perissotero apo thn AB
        if furthest_point is None:
            return [A, B]
        M = points_right_of_line(A, furthest_point, S)                             # Briskoume ta shmeia pou einai deksia ths euteias AG                       
        N = points_right_of_line(furthest_point, B, S)                             # Briskoume ta shmeia pou einai deksia ths euteias GB 
        return QuickHull(A, furthest_point, M) + QuickHull(furthest_point, B, N)   # Ekteloume ksana ton algorithmo gia tis eutheies AG kai GB

##################################################################################################################################################################################

def Convex_hull_QuickHull(points, L, U, R, D):                                     # Briskoume to kurto periblhma

    edges = [L, U, R, D]                                                           # Exoume arxika tis 4 akraies korufes
    not_inside_points = point_inside_quadrilateral(edges, points)                  # Briskoume apo to sunolo twn shmeiwn ta shmeia pou den einai eswterika twn 4 akraiwn korufwn 
    convex_hull = []                                                               # Arxikopoioume to kurto periblhma                                      

    h = QuickHull(L, U, not_inside_points)                                         
    convex_hull = convex_hull + h                                                  # Prosthetoume to h sto kurto periblhma
    h = QuickHull(U, R, not_inside_points)
    convex_hull = convex_hull + h
    h = QuickHull(R, D, not_inside_points)
    convex_hull = convex_hull + h
    h = QuickHull(D, L, not_inside_points)
    convex_hull = convex_hull + h

    h = list(dict.fromkeys(h))                                                     # Elegxoume gia diplotupa

    return convex_hull                                                             # Epistrefoume to kurto periblhma

def main():
    N = 100
    points = []
    convex_hull = []
    # points = [(-2, -10), (1,7), (-10, 5), (5,6), (9, 3), (11, 8), (15, -11), (18, -3), (24,-8)]
    flag = input("Press 1 if you want to use points on general position or 2 if you want to have some collinear points: ")
    if int(flag) == 1:
        points = functions.generate_points_general_position(N)                     # Ftiaxnoume shmeia se genikh thesi
    if int(flag) == 2:
        points = functions.generate_collinear_points(N)                            # Ftiaxnoume shmeia pou merika apo auta einai suneutheiaka 

    points.sort()                                                                  # Taksinomoume ta stoixeia ws pros x
    L = points[0]                                                                  # To prwto stoixeio tha einai to aristerotero
    R = points[-1]                                                                 # To teleutaio stoixeio tha einai to deksiotero
    (D, U) = find_min_max_y(points)                                                # Briskoume to panw kai katw akraio shmeio 

    convex_hull = Convex_hull_QuickHull(points, L, U, R, D)                        # Briskoume to kurto periblhma me ton algorithmo Quick Hull
    functions.Plot_Convex_Hull(points, convex_hull, 'Quick_Hull-2D.png')           # Sxediazoume to kurto periblhma

    return

main()