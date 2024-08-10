from KD_tree_construction import KD_tree_construction 
import matplotlib.pyplot as plt
import random

def search_kd_tree(node, R, depth=0):                                               # Ektelei ton algorithmo orthogwnias anazhthshs
    if node is None:                                                                 
        return []
    
    points_inside_R = []                                                            # Se auth thn lista tha apothikeuoume ta shmeia pou einai mesa sthn R
                                           
    if node.left is None and node.right is None:                                    # Elegxoume an o kombos einai fullo
        if R[0][0] <= node.points[0] <= R[1][0] and R[0][1] <= node.points[1] <= R[1][1]:     # Elegxoume an einai mesa sthn perioxh R
            points_inside_R.append(node.points)                                     # An einai mesa sthn R tote to prosthetoume sth lista twn shmeiwn
        return points_inside_R                                                      # Episrtrefoume ta shmeia

    if node.left:                                                                   # Elegxoume to aristero upodendro
        points_inside_R += search_kd_tree(node.left, R, depth + 1)

    if node.right:                                                                  # Elegxoume to deksi upodendro
            points_inside_R += search_kd_tree(node.right, R, depth + 1)

    if R[0][0] <= node.points[0] <= R[1][0] and R[0][1] <= node.points[1] <= R[1][1]:         # Elegxoume an h riza anhkei sthn perioxh R
        points_inside_R.append(node.points)                                         # Prosthetoume thn riza sta shmeia

    return points_inside_R                                                          # Epistrefoume ta shmeia 

def Plotting(P, R, found_points):                                                   # Sxeidiazei ta shmeia kai thn perioxh R

    plt.clf()
    x_coordsP = [point[0] for point in P]                                           
    y_coordsP = [point[1] for point in P]
    for i in range (0, len(P)):
        if P[i] in found_points:
            plt.scatter(x_coordsP[i], y_coordsP[i], color='red')                    # Sxediazoume ta shmeia tou P pou anhkoun sthn perioxh R me kokkino
        elif P[i] not in found_points:
            plt.scatter(x_coordsP[i], y_coordsP[i], color='black')                  # Sxediazoume ta upoloipa shmeia tou P me mauro 

    x_coordsR = [point[0] for point in R]                                           
    y_coordsR = [point[1] for point in R]
    plt.scatter(x_coordsR, y_coordsR, color='blue')                                 # Sxediazoume ta shmeia ths perioxhs R me mple

    # Sxediazoume tis grammes tou orthogwniou ths perioxhs R
    plt.plot([R[0][0], R[1][0]], [R[0][1], R[0][1]], 'b--', linewidth=1)            
    plt.plot([R[0][0], R[1][0]], [R[1][1], R[1][1]], 'b--', linewidth=1)
    plt.plot([R[0][0], R[0][0]], [R[0][1], R[1][1]], 'b--', linewidth=1)
    plt.plot([R[1][0], R[1][0]], [R[0][1], R[1][1]], 'b--', linewidth=1)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Orthogonal Search')
    plt.savefig('Orthogonal Search.png')                                            # Apothikeuoume thn eikona

def main():
    # P = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
    min = -10
    max = 10
    N = 100
    P = [[round(random.uniform(min, max), 3), round(random.uniform(min, max), 3)] for _ in range(N)]    # Apothikeuoume sto P N tuxaia shmeia sto diasthma (min,max)
    R = [[-4, 1], [8, 6]]  

    kd_tree = KD_tree_construction(P)                                               # Ftiaxnoume to kd-tree kallwntas thn antistoixh sunarthsh
    found_points = search_kd_tree(kd_tree, R)                                       # Psaxnoume sto kd-tree

    print("Points within region R =", R[0], "x", R[1], ":\n")                       # Tupwnoume ta shmeia pou einai mesa sthnn perioxh R
    for point in found_points:
        print(point)
    print("\nWe have found", len(found_points), "points within region R =", R[0], "x", R[1])
    Plotting(P, R, found_points)                                                    # Sxediazoume ta shmeia kai thn perioxh R

main()