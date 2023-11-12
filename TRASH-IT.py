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
    carre, i, j, ok = {}, 0, 0, False
    
    def isMultiple(M,b):
        if b == M or M == 1:
            res = True
        elif b < M:
            res = False
        else:
            res = isMultiple(M,b-M)
        
        return res
    while i < IJ_MAX and not ok: 
        #pour chaque carre le bloc ci dessous:
        while not isMultiple(CARRE_TAILLE, i):
            carre[(i,j)] = grid[i][j]
            if not isMultiple(CARRE_TAILLE-1, j):
                j += 1
            else:
                j = 0
                i += 1

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
                    grid[x][y] = carre[_] = candidats_uniques.pop() #prendre un candidat au hasard MAIS l'enlever du set
                else:
                    ok = True
    
    if not ok == True:
        res = (not ok, grid)
    else:
        res = (not ok, None)
        
    return res #renvoie True si 'ok' est resté à False donc aucun carré n'a causé un arrêt de la résolution du sudoku. 
