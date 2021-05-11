"""
Le but de l'algorithme est de trouver le chemin le moins couteux en terme de
distance en prenant en considération tout les arrêts demandés.

l'idée est la suivante:
On doit en realité réussir à faire le polynome qui possède le moins de côtés
avec tout les sommets demandés, ce qui en fait revient à vouloir avoir la forme
géométrique qui possède le plus petit périmètre pour le nombre de sommets
demandé. Pour ce faire il faut procéder comme suit:

1 - Ressencer dans une liste tout les cerlcles du plus grand au plus petit
possèdant le même centre (notre point de départ).

2 - On réalise ensuite un triangle que l'on matérialisera par une liste des
trois premiers points de la liste initale dont les trois sommets sont confondus
avec les trois premiers cercles de notre liste de départ. On désignera cette
liste comme la liste de fin. On retire donc les trois premiers points de la
liste de départ.

3 - On prend ensuite le premier point de la liste de départ (qui était le 4ème)
et on réalise le cercle le plus petit ayant pour centre ce point avec le point
de la liste obtenue grace à notre triangle. On regarde ensuit le cercle qui est
juste après en terme de grandeur. Une fois les cercles obtenue on place
ce quatrième point extrait de la liste de départ pour le placer dans la liste
de fin entre les deux points qui ont servis à tracer les deux cercles précédants.

4 - On prend ensuite le premier point de la liste de départ (qui était le 5ème)
pour repeter la même opération jusqu'à épuisement des points de la liste de
départ. On obtient donc, grâce à notre liste de fin si on traçait les
droites qui relient dans l'ordre des points, ce polynome qui possède pour sommets
tout ces points de la liste et ayant le périmètre le plus petit.

"""
################################################################################


