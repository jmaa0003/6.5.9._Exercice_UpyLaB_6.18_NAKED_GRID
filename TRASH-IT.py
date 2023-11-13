"""
Joshua Mabhouma
11.11.2023
fonction naked_single(grid) qui reçoit en paramètre
une matrice 9 x 9 d’entiers représentant une grille de sudoku,
et qui renvoie un couple de valeurs.
"""
#3 étapes pour sudoku:
# 0. Hallar las 0s
# 1. Vérifier les carrées
# 2. Vérifier les lignes et les colonnes


def naked_single(grid):
    IJ_MAX, CHIFFRES, CARRE_TAILLE =\
                 len(grid), set([i for i in range(1,10)]), 3
    carre, i, j, ok, rangee = {}, 0, 0, False, 0
    
    while rangee < 3 and not ok: 
        #pour chaque carre le bloc ci dessous:   
        if i != IJ_MAX:
            carre[(i,j)] = grid[i][j]
            if isMultiple(CARRE_TAILLE, i+1) and isMultiple(CARRE_TAILLE, j+1):  
                for _ in carre:
                    if carre[_] == 0:
                        #vérification ligne colonne carre commence !
                        candidats_uniques = CHIFFRES.difference(set(carre.values())) #0 aussi
                        x,y = _[0], _[1]
                        ligne = [li for li in grid[x]]
                        colonne, col = [], 0
                        while col < IJ_MAX:
                            colonne.append(grid[col][y])
                            col += 1
                        candidats_uniques -= set(colonne).union(set(ligne))
                        # élimination de tous les chiffres présents dans la ligne, colonne et carre en même temps
                        # pour obtenir un ou des candidats uniques
                        
                        if len(candidats_uniques) > 0:
                            #prendre un candidat au hasard MAIS l'enlever du set
                            grid[x][y] = carre[_] = candidats_uniques.pop()
                        else:
                            ok = True
                carre.clear()
            if not isMultiple(CARRE_TAILLE, j+1):
                j += 1
            else:
                j = rangee*CARRE_TAILLE
                i += 1  
        else:
            rangee += 1
            i, j = 0, rangee*CARRE_TAILLE
            
    if not ok == True:
        res = (not ok, grid)
    else:
        res = (not ok, None)
        
    return res #renvoie True si 'ok' est resté à False donc aucun carré n'a causé un arrêt de la résolution du sudoku.

def isMultiple(M,b):
        if b == M or M == 1:
            res = True
        elif b < M:
            res = False
        else:
            res = isMultiple(M,b-M)
        
        return res

ez = naked_single([[0, 0, 3, 0, 2, 0, 6, 0, 0],
                    [9, 0, 0, 3, 0, 5, 0, 0, 1],
                    [0, 0, 1, 8, 0, 6, 4, 0, 0],
                    [0, 0, 8, 1, 0, 2, 9, 0, 0],
                    [7, 0, 0, 0, 0, 0, 0, 0, 8],
                    [0, 0, 6, 7, 0, 8, 2, 0, 0],
                    [0, 0, 2, 6, 0, 9, 5, 0, 0],
                    [8, 0, 0, 2, 0, 3, 0, 0, 9],
                    [0, 0, 5, 0, 1, 0, 3, 0, 0]])
print(ez ,ez == (True, [[4, 8, 3, 9, 2, 1, 6, 5, 7], [9, 6, 7, 3, 4, 5, 8, 2, 1], [2, 5, 1, 8, 7, 6, 4, 9, 3], [5, 4, 8, 1, 3, 2, 9, 7, 6], [7, 2, 9, 5, 6, 4, 1, 3, 8], [1, 3, 6, 7, 9, 8, 2, 4, 5], [3, 7, 2, 6, 8, 9, 5, 1, 4], [8, 1, 4, 2, 5, 3, 7, 6, 9], [6, 9, 5, 4, 1, 7, 3, 8, 2]]))
