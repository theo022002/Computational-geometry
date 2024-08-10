import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

def Convex_hull_3D(points):

    hull = ConvexHull(points)                                                          # Ypologizoume to kurto periblhma 

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')                                      
    ax.scatter(points[:,0], points[:,1], points[:,2], color = 'red', marker='o')       # Sxediazoume ta arxika shmeia

    for point in hull.simplices:                                                       # Sxediazoume to kurto periblhma
        ax.plot(points[point, 0], points[point, 1], points[point, 2], color = 'black')

    plt.savefig('Convex_Hull-3D.png') 

    return

def main():
    n = 85
    points = np.random.rand(n, 3)                                                      # Briskoume tuxaia shmeia se 3D
    Convex_hull_3D(points)                                                             # Kaloume thn sunarthsh gia ton upologismo tou kurtou periblhmatos
    
    return 

main()                         