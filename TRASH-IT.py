"""
Joshua Mabhouma
11.11.2023
fonction naked_single(grid) qui reçoit en paramètre
une matrice 9 x 9 d’entiers représentant une grille de sudoku,
et qui renvoie un couple de valeurs.
"""
#3 étapes pour sudoku:
# 1. Itérer jusqu'à trouver des 0

def naked_single(grid):
    i,i_max,j,j_max, chiffres  = 0,len(grid),0,len(grid[-1]), [i for i in range(1,10)]
---    
    while i < i_max:
        colonne, ligne = grid[j][i], grid[i]
        
        
        if j < i_max-1:
            j += 1
        else:
            j = 0
            i += 1
---       
    
    
    