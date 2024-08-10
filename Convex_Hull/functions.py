import random
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def generate_point():                                                              # Dhmiourgoume ena tuxaio shmeio
    return random.uniform(-1000, 1000), random.uniform(-1000, 1000)

def generate_points_general_position(n):                                           # Dhmiourgoume n tuxaia shmeia se genikh thesi 
    points = []
    while len(points) < n:
        new_point = generate_point()
        if not any(CCW(p1, p2, new_point) == 0 for p1 in points for p2 in points if p1 != p2):
            points.append(new_point)
    return points                                                                  # Epistrefoume to sunolo twn n shmeiwn se genikh thesi

def generate_collinear_points(n):
    points = generate_points_general_position(n) 
    hull = ConvexHull(points)

    point_index1 = hull.vertices[random.randint(0, len(hull.vertices)-1)]
    first_point = points[point_index1]
    point_index2 = hull.vertices[random.randint(0, len(hull.vertices)-1)]
    last_point = points[point_index2]
    
    first_collinear_points = [(first_point[0]+i, first_point[1]) for i in range(5, 10,100)]
    last_collinear_points = [(last_point[0]+i, last_point[1]) for i in range(5, 10, 100)]
    
    return (points+last_collinear_points+first_collinear_points)

##################################################################################################################################################################################

def CCW(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:                                                                   # Suneutheiaka shmeia
        return 0
    if val > 0:                                                                    # Deksia strofh                                           
        return 1  
    else:                                                                          # Aristerh strofh
        return 2  

def Plot_Convex_Hull(S, convex_hull_points, f_name):                               # Sxediazei sto epipedo to kurto periblhma
    
    x_coords = [point[0] for point in S]                                           
    y_coords = [point[1] for point in S]

    plt.scatter(x_coords, y_coords, color='black')                                 # Sxediazei ta shmeia

    for i in range(len(convex_hull_points)):                                       # Sxediazoume to kurto periblhma
        plt.plot([convex_hull_points[i][0], convex_hull_points[(i+1) % len(convex_hull_points)][0]], [convex_hull_points[i][1], convex_hull_points[(i+1) % len(convex_hull_points)][1]], color = 'red')

    convex_x = [point[0] for point in convex_hull_points]
    convex_y = [point[1] for point in convex_hull_points]
    plt.scatter(convex_x, convex_y, color = 'red')                                 # Sxediazoume ta shmeia tou kurtou periblhmatos

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig(f_name)

    return