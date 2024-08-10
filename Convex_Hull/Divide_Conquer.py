import math
import functions
from scipy.spatial import ConvexHull
from collections import OrderedDict

def get_angle(point, centroid):                                                    # Ypoligzei thn gwnia se rad anamesa se ena shmeio kai to kentro tou polugwnou
    x = point[0] - centroid[0]
    y = point[1] - centroid[1]
    return math.atan2(y, x)

def sort_points_clockwise(points):                                                 # Taksinomei shmeia se orologiakh diataksi gurw apo to kentro tous
    centroid = [sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)]   # Briskei to kentro 
    return sorted(points, key=lambda p: (get_angle(p, centroid) + 2 * math.pi) % (2 * math.pi))

def sort_points_counterclockwise(points):                                           # Taksinomei shmeia se anti-orologiakh diataksi gurw apo to kentro tous
    centroid = [sum(p[0] for p in points) / len(points), sum(p[1] for p in points) / len(points)]
    return sorted(points, key=lambda p: (get_angle(p, centroid)))

##################################################################################################################################################################################

def upper_bridge(A, B):                                                            # Briskoume thn panw gwfura
    na = len(A)                                                                    # Arithmos shmeiwn tou A
    nb = len(B)                                                                    # Arithmos shmeiwn tou B

    A = sort_points_clockwise(A)                                                   # Taksinomoume ta shmeia tou A se orologiakh diataksh
    B = sort_points_counterclockwise(B)                                            # Taksinomoume ta shmeia tou B se anti-orologiakh diataksh
    right_A = 0
    left_B = 0

    for i in range(1, na):                                                         # Briskoume to deksiotero shmeio tou A
        if A[i][0] > A[right_A][0]:                                                # To deksiotero shmeio einai auto me to megalutero x
            right_A = i

    for i in range(1, nb):                                                         # Briskoume to aristerootero shmeio tou B
        if B[i][0] < B[left_B][0]:                                                 # To aristerotero shmeio einai auto me to mikrotero x
            left_B = i

    index_A = right_A
    index_B = left_B
    flag = 0
    while flag != 1:                                                               # Briskoume thn panw gefura
        flag = 1
        while functions.CCW(B[index_B], A[index_A], A[(index_A+1) % na]) != 2:
            index_A = (index_A + 1) % na
 
        while functions.CCW(A[index_A], B[index_B], B[(nb+index_B-1) % nb]) == 2:
            index_B = (nb + index_B - 1) % nb
            flag = 0
 
    return [(A[index_A][0], A[index_A][1]), (B[index_B][0], B[index_B][1])]        # Epistrefoume thn panw gefura

##################################################################################################################################################################################

def lower_bridge(A, B):                                                            # Briskoume thn katw gefura
    na, nb = len(A), len(B)

    A = sort_points_counterclockwise(A)                                            # Taksinomoume ta shmeia tou A se anti-orologiakh diataksh
    B = sort_points_counterclockwise(B)                                            # Taksinomoume ta shmeia tou B se anti-orologiakh diataksh

    right_A = 0
    left_B = 0

    for i in range(1, na):                                                         # Briskoume to deksiotero shmeio tou A
        if A[i][0] > A[right_A][0]:                                                # To deksiotero shmeio einai auto me to megalutero x
            right_A = i

    for i in range(1, nb):                                                         # Briskoume to aristerootero shmeio tou B
        if B[i][0] < B[left_B][0]:                                                 # To aristerotero shmeio einai auto me to mikrotero x
            left_B = i

    index_A = right_A
    index_B = left_B
    flag = 0
    while flag != 1:                                                               # Briskoume thn katw gefura
        flag = 1
        while functions.CCW(A[index_A], B[index_B], B[(index_B + 1) % nb]) != 2:
            index_B = (index_B + 1) % nb

        while functions.CCW(B[index_B], A[index_A], A[(na + index_A - 1) % na]) == 2:
            index_A = (na + index_A - 1) % na
            flag = 0

    return [(A[index_A][0], A[index_A][1]), (B[index_B][0], B[index_B][1])]        # Epistrefoume thn katw gefura

##################################################################################################################################################################################

def divide_points(points):                                                         # Xwrizoume ta shmeia sta 2 kai briskoume ta 2 KP
    points.sort()                                                                  # Taksinomoume ta shmeia me auksousa leksikografikh seira
    n = len(points)
    A = []
    B = []
    convex_A = []
    convex_B = []

    for i in range(0, math.ceil(n/2)):                                             # Kratame sto A ta prwta misa shmeia
        A.append(list(points[i]))  
    for i in range(math.ceil(n/2), n):                                             # Kratame sto B ta upoloipa shmeia
        B.append(list(points[i]))  

    convex_A1 = ConvexHull(A)                                                      # Briskoume to KP tou A
    convex_B1 = ConvexHull(B)                                                      # Briskoume to KP tou B
 
    for i in convex_A1.vertices:    
        point_index = i
        convex_A.append(A[point_index])
    for i in convex_B1.vertices:    
        point_index = i
        convex_B.append(B[point_index])

    return (convex_A, convex_B)                                                    # Epistrefoume ta KP

##################################################################################################################################################################################

def Convex_hull_Divide_Conquer(points):                                            # Briskei to KP me ton algorithmo divide and conquer
    (convex_A, convex_B) = divide_points(points)                                   # Briskoume ta duo KP
    upper_bridge_points = upper_bridge(convex_A, convex_B)                         # Briskoume thn panw gefura
    lower_bridge_points = lower_bridge(convex_A, convex_B)                         # Briskoume thn katw gefura

    Hull = []
    for p in convex_A:
        if functions.CCW(upper_bridge_points[0], upper_bridge_points[1], p) == functions.CCW(lower_bridge_points[1], lower_bridge_points[0], p):
            Hull.append(p)
    for p in convex_B:
        if functions.CCW(upper_bridge_points[0], upper_bridge_points[1], p) == functions.CCW(lower_bridge_points[1], lower_bridge_points[0], p):
            Hull.append(p)

    hull = convex_A + convex_B + upper_bridge_points + lower_bridge_points         # Briskoume thn enwsh twn shmeiwn tvn gefurwn kai twn duo KP
    hull = list(OrderedDict.fromkeys(map(tuple, hull)))                            # Afairoume ta diplotupa
    convex_hull = ConvexHull(hull)                                                 # Briksoume to kurto periblhma                                                                                    
    Hull = []
    for i in convex_hull.vertices:    
        point_index = i
        Hull.append(hull[point_index])

    return Hull                                                                    # Epistrefoume to kurto periblhma

def main():
    N = 100
    points = []
    flag = input("Press 1 if you want to use points on general position or 2 if you want to have some collinear points: ")
    if int(flag) == 1:
        points = functions.generate_points_general_position(N)                     # Ftiaxnoume shmeia se genikh thesi
    if int(flag) == 2:
        points = functions.generate_collinear_points(N)                            # Ftiaxnoume shmeia pou merika apo auta einai suneutheiaka 
    # points = [(-2, -10), (1,7), (-10, 5), (5,6), (9, 3), (11, 8), (15, -11), (18, -3), (3,4), (24,-8)]
    convex_hull = Convex_hull_Divide_Conquer(points)                               # Kaloume ton algorithmo gia thn euresh tou kurtou periblhmatos                             
    functions.Plot_Convex_Hull(points, convex_hull, 'Divide-Conquer-2D.png')       # Sxediazoume to kurto periblhma

    return

main()