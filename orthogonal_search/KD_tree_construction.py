import matplotlib.pyplot as plt
import random

class Node:                                                                         # Klash gia na apothikeuoume plhrofories gia enan kombo
    def __init__(self, split_dim=None, split_val=None, left=None, right=None, points=None):
        self.split_dim = split_dim                                                  # Diastash sthn opoia o kombos diaxwrizetai
        self.split_val = split_val                                                  # Diaxwristikh timh 
        self.left = left                                                            # Aristero paidi tou kombou 
        self.right = right                                                          # Deksi paidi tou kombou
        self.points = points                                                        # Suntetagmenes shmeiou

def KD_tree_construction(P, depth=0):                                               # Sunarthsh pou ftiaxnei to Kd-tree
    if len(P) == 0:                                                                 # An den exoume kapoio shmeio
        return None                                                                 # Den epistrefoume kati
    if len(P) == 1:                                                                 # An exoume ena shmeio 
        return Node(points=P[0])                                                    # Epistrefoume ena fullo pou periexei auto to shmeio
    
    dim = depth % 2                                                                 # Diastash pou ginetai to split
    P.sort(key=lambda x: x[dim])                                                    # Taksinomoume ta shmeia me bash thn diastash

    mid = len(P) // 2                                                               # Briskoume thn thesh tou mesaiou shmeiou
    median_point = P[mid]                                                           # Briskoume to mesaio shmeio

    # Xwrizoume ta shmeia se duo sunola
    P1 = P[:mid]                                                                    # P1 = shmeia aristera apo to mesaio shmeio
    P2 = P[mid + 1:]                                                                # P2 = shmeia deksia apo to mesaio shmeio

    left_subtree = KD_tree_construction(P1, depth + 1)                              # Ftiaxnoume anadromika to aristero upodendro 
    right_subtree = KD_tree_construction(P2, depth + 1)                             # Ftiaxnoume anadromika to deksio upodendro 

    # Ftiaxnoume enan kombo gia na apothikeuoume thn diaxwristikh eutheia, ta upodendra
    node = Node(split_dim=dim, split_val=median_point[dim], left=left_subtree, right=right_subtree, points=median_point)
    return node                                                                     # Epistrefoume ton kombo auto

def Plot_splitting_lines(node, min_x, max_x, min_y, max_y, depth=0):                # Sxediazei tis diaxwristikes eutheies      
    if node is None:
        return

    dim = node.split_dim
    split_val = node.split_val

    if dim == 0:                                                                    # Kathetes eutheies
        plt.plot([split_val, split_val], [min_y, max_y], 'r--')                     # Sxediazoume tis kathetes eutheies me kokkino
        Plot_splitting_lines(node.left, min_x, split_val, min_y, max_y, depth + 1)  # Kaloume thn sunarthsh gia na kanei to idio gia to aristero upodendro
        Plot_splitting_lines(node.right, split_val, max_x, min_y, max_y, depth + 1) # Kaloume thn sunarthsh gia na kanei to idio gia to deksi upodendro
    else:                                                                           # Orizonties eutheies
        plt.plot([min_x, max_x], [split_val, split_val], 'b--')                     # Sxediazoume tis orizonties eutheies me mple
        Plot_splitting_lines(node.left, min_x, max_x, min_y, split_val, depth + 1)  # Kaloume anadromika thn sunarthsh gia to aristero upodendro
        Plot_splitting_lines(node.right, min_x, max_x, split_val, max_y, depth + 1) # Kai to idio gia to deksi upodendro
    
    return

def Plot_KD_tree(kd_tree, P, min, max):                                             # Sxediazei to kd-tree                            
    plt.figure(figsize=(10, 10))
    x_coordsP = [point[0] for point in P]                                           
    y_coordsP = [point[1] for point in P]
    plt.scatter(x_coordsP, y_coordsP, color='black')                                # Sxediazoume ta shmeia 

    Plot_splitting_lines(kd_tree, min, max, min, max)                               # Sxediazoume tis diaxwristikes eutheies me thn katallhlh sunarthsh

    plt.xlim(min, max)
    plt.ylim(min, max)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.savefig('KD-tree.png')                                                      # Apothikeuoume thn grafikh parastash

    return

def main():
    # P = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
    min = -10
    max = 10
    N = 80
    P = [[round(random.uniform(min, max), 3), round(random.uniform(min, max), 3)] for _ in range(N)]    # Ftiaxnoume N tuxaia shmeia sto diasthma (min,max)
    kd_tree = KD_tree_construction(P)                                               # Ftiaxnooume to kd-tree
    Plot_KD_tree(kd_tree, P, min, max)                                              # Sxediazoume to kd-tree

    return 

main()