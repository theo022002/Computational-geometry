import numpy as np
from scipy.optimize import linprog

def concatenation_A(A,i,j):                          # Ypologizoume tous suntelestes tou neou periorrismou ths suzeukshs tou Hi = 0, Hj
    a = -A[i][1] / A[i][0]
    a = a*A[j][0] + A[j][1]
    return a

def new_b(b,A,i):                                    # Ypologizoume tous suntelestes tou neou b meta th suzeuksh tou Hi = 0 me tous allous periorismous
    b_new = []
    for k in range(0,i):
        b_new.append(b[k] - A[k][0]*b[i]/A[i][0])
    return b_new

def seidel_algorithm(A, b, f, flag_function):        # Ektelei ton algorithmo Seidel 
    try:
        d = len(f)                                   # Arithmos metablhtwn
        n = len(A)                                   # Arithmos periorismwn

        x0_bounds = (0, None)                        # x0 >= 0
        x1_bounds = (0, None)                        # x1 >= 0

        b_init = []
        A_init = []
        i = 0
        for i in range(d+1):                         # Apothikeuoume sto b_init, A_init tous suntelestes twn prwtwn d+1 periorismwn
            b_init.append(b[i])
            A_init.append([0, 0])
            A_init[i][0] = A[i][0]
            A_init[i][1] = A[i][1]

        if flag_function == "max":                   # An h f einai max(z) tha prepei na antistrepsoume ta proshma giati h sunarthsh linprog lunei problhma elaxistopoihshs
            f[0] = -f[0]
            f[1] = -f[1]
        x_init = linprog(f, A_ub=A_init, b_ub=b_init, bounds=[x0_bounds, x1_bounds])   # Lunei problhma LP elaxistopoihshs => briskoume to x*_(d+1) = x*_(3)

        i = d + 1
        x = []
        while len(x) < n+1:                          # Arxikopoioume to dianusma x sto opoio tha apothikeuoume tis luseis twn problhmatwn grammikou programmatismou 
            x.append(None)
        x[i-1] = (x_init.x)                          # Stis thesis 0-d-1 to x tha einai = None, sth thesi d tha exei to x*3
        
        if d+1 == n:
            return x[i-1]
        
        flag = 0
        for i in range(d+1,n):                       # Gia tous upoloipous periorismous d+1,..,n-1
            A_new = []                               # Sto A_new tha apothikeuoume tous suntelestes twn periorismwn H'_j
            if x[i-1] != None:                       
                if (x[i-1][0]*A[i][0] + x[i-1][1]*A[i][1]) <= b[i]:                    # An to x[i-1] ikanopoiei ton periorismo H[i]
                    x[i] = x[i-1]                                                      # Apla thetoume x[i] = x[i-1]
                    flag = 1
            if flag == 0:                            # An to x[i-1] den ikanopoiei ton periorismo H[i]
                for j in range(0, i):                # Gia tous periorismous j = 0,..,i-1
                    A_new.append([concatenation_A(A,i,j)])                             # Ypologizoume tous suntelestes twn newn periorismwn A'_j
                b_init = new_b(b,A,i)                # Ypologizoume to neo dianusma b'
                f_new = f[1] - f[0]*A[i][1]/A[i][0]  # Briskoume thn nea antikeimenikh sunarthsh

                x_new = linprog(f_new, A_ub=A_new, b_ub=b_init, bounds=[x1_bounds])    # Lunoume to neo problhma grammikou programmatismou me d-1 (=1) metablhtes 
                x_1 = np.array(x_new.x)                                                # To x_1 tha periexei thn lush x_1 tou grammikou programmatismou 
                x[i] = (b[i]/A[i][0] - A[i][1]/A[i][0]*x_1[0], x_1[0])                 # Apothikeoume sto x[i] to (x_0,x_1) lush tou problhmatos grammikou programmatismou me i-1 periorismous 
        return x[i]                               
    
    except Exception as e:
        print("Error occurred:", e)
        return None

def main():
    A = np.array([[1, -2], [2, -3], [-1, 3], [-1, 6], [4, -9]])
    b = np.array([1, 6, 0, 12, 27])
    f = np.array([-3, 12])
    L = [">=", ">=", "<=", "<="]
    Flag_function = "max"
    
    # A = np.array([[1, 1], [1, 0], [2, 1]])
    # b = np.array([350, 125, 600])
    # f = np.array([2, 3])
    # L = [">=", ">=", "<="]
    # Flag_function = "min"

    i = 0
    for i, element in enumerate(L):                  # Se periptwsh pou to problhma den einai sthn tupikh morfh to metatrepoume
        if element == ">=":
            L[i] = "<="
            A[i][0] = -A[i][0]
            A[i][1] = -A[i][1]
            b[i] = -b[i]

    res = seidel_algorithm(A, b, f, Flag_function)   # Lunoume to problhma me thn methodo Seidel
    f_value = res[0]*f[0]+res[1]*f[1]                # Ypologizoume thn beltisth timh ths antikeimenikhs sunarthshs 

    if res is not None and None not in res:          # An to problhma den einai anefikto 
        print("Optimal solution: (x1, x2) = (", float(res[0]), ",", float(res[1]), ")")  # Tupwnoume thn domh ths beltisths lushs 
        if Flag_function == "max":
            print("Optimal value of the objective function:", float(-f_value))           
        elif Flag_function == "min":
            print("Optimal value of the objective function:", float(f_value))            
    else:                                            # Alliws tupwnoume oti to problhma einai anefikto
        print("The problem is infeasible.")

    return

main()