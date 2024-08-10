import functions

def Wrapping(S):                                                                   # Ekteloume ton algorithmo perituligmatos gia thn euresh tou kurtou periblhmatos
    n = len(S)
    if n < 3:
        return "Infeasible"
    l = min(S, key=lambda p: (p[1], p[0]))                                         # Briskoume to aristerotero shmeio 

    r = l                                                                          # Arxikopoioume thn trexousa korufh 
    convex_hull_points = [r]                                                       # Arxikopoihsh tou kurtou periblhmatos 

    while True:                                                                    # Epanalambanoume mexri na ftasoume sto arxiko shmeio 
        u = S[0]  
        for t in S[1:]:                                                            # Gia ola ta upoloipa shmeia
            if u == r or functions.CCW(r, u, t) == 1 or (functions.CCW(r, u, t) == 0 and (u == t or functions.CCW(r, t, u) == 1)):
                u = t
        if u == l:                                                                 # An ftasoume sto arxiko shmeio 
            break                                                                  # Stamatame
        convex_hull_points.append(u)
        S.remove(u)                                                                # Afairoume to u apo to S
        r = u                                                                      # Allazoume thn trexousa korufh

    return convex_hull_points                                                      # Epistrefoume to kurto periblhma

def main():
    
    N = 100
    S = []
    convex_hull = []
    # S = [(-2, -10), (1,7), (-10, 5), (5,6), (9, 3), (11, 8), (15, -11), (18, -3), (24,-8)]
    flag = input("Press 1 if you want to use points on general position or 2 if you want to have some collinear points: ")
    if int(flag) == 1:
        S = functions.generate_points_general_position(N)                          # Ftiaxnoume shmeia se genikh thesi
    if int(flag) == 2:
        S = functions.generate_collinear_points(N)                                 # Ftiaxnei shmeia pou merika apo auta einai suneutheiaka 
    convex_hull = Wrapping(S)                                                      # Kaloume ton algorithmo gia thn euresh tou kurtou periblhmatos
    functions.Plot_Convex_Hull(S, convex_hull, 'Wrapping-2D.png')                  # Sxediazoume to kurto periblhma

    return
 
main()