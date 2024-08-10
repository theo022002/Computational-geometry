import matplotlib.pyplot as plt
import scipy.spatial as spatial
import numpy as np
import random
import time

def InCircle(point, tri_points):                                                    # Ypologizei to kathgorhma In Circle
    A = np.array([
        [tri_points[0][0], tri_points[0][1], tri_points[0][0]**2 + tri_points[0][1]**2, 1],
        [tri_points[1][0], tri_points[1][1], tri_points[1][0]**2 + tri_points[1][1]**2, 1],
        [tri_points[2][0], tri_points[2][1], tri_points[2][0]**2 + tri_points[2][1]**2, 1],
        [point[0], point[1], point[0]**2 + point[1]**2, 1]
    ])
    # Epistrefei 1 an to shmeio einai ekswteriko tou kuklou kai mhden alliws 
    if np.linalg.det(A) > 0:
        return 1
    else:
        return 0                                            

def Plot_Triangulation(points, simplices):                                          # Sxediazoume thn trigwnopoihsh sto epipedo
    plt.figure(figsize=(10, 10))
    plt.triplot(points[:, 0], points[:, 1], simplices, color='blue', linewidth=1.5) # Sxediazoume ta trigwna
    plt.plot(points[:, 0], points[:, 1], 'o', color='black', markersize=6.0)        # Sxediazoume ta shmeia
   
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Triangulation Delaunay')
    plt.savefig('Delaunay.png')                                                     # Apothikeuoume thn trigwnopoihsh sto antistoixo arxeio

    return

##################################################################################################################################################################################

# Dexetai san orisma N shmeia kai prosthetei 3 nees korufes pou sxhmatizoun ena trigwno to opoio periexei ola ta shmeia
def Create_Bigger_Triangle(points):                                                     
    min_coord = np.min(points, axis=0)                                              # Briskoume to elaxisto x kai y twn shmeiwn
    max_coord = np.max(points, axis=0)                                              # Briskoume to megisto x kai y twn shmeiwn
    delta = max(max_coord - min_coord)                                              # Briskoume thn megaluterh apostash twn shmeiwn 

    # Ftiaxnoume tis 3 korufes tou trigwnou 
    p1 = min_coord - delta * np.array([1, 1])     
    p2 = max_coord + delta * np.array([1, 0])
    p3 = max_coord + delta * np.array([0, 1])

    return np.vstack([points, p1, p2, p3])                                          # Epistrefoume ta arxika shmeia + ta 3 nea pou dhmiourghsame

def Triangulation_Delaunay(Points):                                                 # Ektelei thn trigwnopoihsh Delaunay
    n = len(Points)                                                                 # Briskoume ton arithmo twn shmeiwn 
    points = Create_Bigger_Triangle(Points)
    triangulation = spatial.Delaunay(points)
    simplices = triangulation.simplices.copy()

    for i in range(n):                                                              # Gia kathe shmeio
        for simplex in simplices:                                              
            if i in simplex:                                                        # Elegxoume an to shmeio anhkei se kapoio trigwno 
                break                                                               # An anhkei stamatame to eswteriko loop 
        else:                                                                       # An to shmeio i den anhkei se kapoio trigwno elegxoume to epomeno shmeio i+1 
            continue

        # An to shmeio anhkei se kapoio trigwno 
        simplex_idx = np.where(np.any(simplices == i, axis=1))[0][0]                # Briskoume to index apo to geitoniko trigwno
        simplex = simplices[simplex_idx]                                            # Briskoume to akribes trigwno

        for j in range(3):                                                          # Elegxoume kathe geitona 
            neighbor_idx = triangulation.neighbors[simplex_idx, j]                  # Briskoume ta indexes twn geitwnikvn trigwnwn
            if neighbor_idx == -1:                                                  # An den uparxei geitonas
                continue                                                            # Proxwrame 

            neighbor = simplices[neighbor_idx]                                      # Briskoume to geitoniko trigwno
            common_vertex_index = np.where(neighbor == simplex[(j + 1) % 3])[0]     # Briksoume to index ths koinhs akmhs

            if len(common_vertex_index) == 0:                                       # An den uparxei koinh akmh 
                continue                                                            # Proxwrame ston epomeno geitona
            if InCircle(points[i], points[neighbor]):                               # Elegxoume an to shmeio einai mesa ston kuklo pou sxhmatizoun oi korufes tou geitonikoi trigwnou 
                simplices[simplex_idx] = np.roll(simplex, -j)                       # Prosarmozoume to trexon trigwno 
                simplices[neighbor_idx] = np.roll(neighbor, -common_vertex_index[0])# Prosarmozoume to geitoniko trigwno

    simplices = simplices[np.all(simplices < n, axis=1)]                            # Afairoume ta trigwna pou periexoun ta shmeia pou upologisame me thn sunarthsh Create_Super_Triangle

    return simplices

##################################################################################################################################################################################

def main():
    min = -10
    max = 10
    N = 80
    
    points = np.array([[round(random.uniform(min, max), 3), round(random.uniform(min, max), 3)] for _ in range(N)])    # Ftiaxnoume N tuxaia shmeia sto epipedo
    start_time = time.time()                                                        # Ypologizoume ton xrono ekteleshs tou algorithmou 
    simplices = Triangulation_Delaunay(points)                                      # Kaloume thn sunarthsh gia thn trigwnopoihsh
    end_time = time.time()
    
    Plot_Triangulation(points, simplices)                                           # Sxediazoume thn trigwnopoihshs Delaunau
    execution_time = end_time - start_time
    print(f"Execution time of triangulation delaunay with {N} points is: {execution_time:.5f} seconds")                # Tupwnoume ton xrono pou xreiasthke o algorithmos

    return

main()