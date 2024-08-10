import functions

def Grahams_scan(points):                                                          # Ektelei ton algorithmo Graham's Scan
    n = len(points)
    if n < 3:
        return []
    points.sort()                                                                  # Taksinomei ta shmeia se auksousa leksikografikh seira

    L = []
    L.append(points[0])
    L.append(points[1])

    for p in points[1:]:                                                           # Ypologizei to L_anw
        while len(L) >= 2 and functions.CCW(L[-2], L[-1], p) != 1:    
            L.pop()
        L.append(p)

    for p in reversed(points[:-1]):                                                # Ypologizei to L_katw kai ksekinaei apo to shmeio n-2 mias kai to n-1 uparxei hdh sto L
        while len(L) >= 2 and functions.CCW(L[-2], L[-1], p) != 1:
            L.pop()
        L.append(p)                                                                # Prosthetoume to p sth lista L
    L.pop()                                                                        # Afairoume to teleutaio shmeio gia na mhn exoume diplotupa

    return L                                                                       

def main():

    points = []
    convex_hull = []
    N = 100
    # points = [(-2, -10), (1,7), (-10, 5), (5,6), (9, 3), (11, 8), (15, -11), (18, -3), (3,4), (24,-8)]
    flag = input("Press 1 if you want to use points on general position or 2 if you want to have some collinear points: ")
    if int(flag) == 1:
        points = functions.generate_points_general_position(N)                     # Ftiaxnoume shmeia se genikh thesi
    if int(flag) == 2:
        points = functions.generate_collinear_points(N)                            # Ftiaxnei shmeia pou merika apo auta einai suneutheiaka 
    
    convex_hull = Grahams_scan(points)                                             # Kaloume ton algorithmo gia thn euresh tou kurtou periblhmatos
    functions.Plot_Convex_Hull(points, convex_hull, 'Grahams-Scan-2D.png')         # Sxediazoume to kurto periblhma
    
main()