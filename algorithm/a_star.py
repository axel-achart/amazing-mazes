# a_star.py - Algorithme A* pour résoudre des labyrinthes
import heapq
from typing import List, Tuple, Optional, Set


class Node:
    """Classe représentant un nœud dans l'algorithme A*"""
    
    def __init__(self, position: Tuple[int, int], g_cost: float = 0, h_cost: float = 0, parent=None):
        self.position = position
        self.g_cost = g_cost      # Coût depuis le début
        self.h_cost = h_cost      # Heuristique (estimation vers la fin)
        self.f_cost = g_cost + h_cost  # Coût total f = g + h
        self.parent = parent      # Nœud parent pour reconstruire le chemin

    def __lt__(self, other):
        """Comparaison pour la priority queue"""
        return self.f_cost < other.f_cost

    def __eq__(self, other):
        """Égalité basée sur la position"""
        return self.position == other.position

    def __hash__(self):
        """Hash basé sur la position"""
        return hash(self.position)


def load_maze_from_file(filename: str) -> Optional[List[List[str]]]:
    """
    Charge un labyrinthe depuis un fichier texte
    
    Args:
        filename: Nom du fichier (sans extension .txt)
    
    Returns:
        Matrice représentant le labyrinthe ou None si erreur
    """
    try:
        with open(f"labyrinth/{filename}.txt", 'r') as file:
            content = file.read().strip()
            return [list(row) for row in content.split('\n')]
    except FileNotFoundError:
        print(f" Erreur : Le fichier 'labyrinth/{filename}.txt' n'existe pas.")
        return None
    except Exception as e:
        print(f" Erreur lors du chargement : {e}")
        return None


def find_start_and_end(maze: List[List[str]]) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
    """
    Trouve les positions de départ et d'arrivée dans le labyrinthe
    
    Args:
        maze: Matrice du labyrinthe
    
    Returns:
        Tuple (start_position, end_position)
    """
    start = None
    end = None
    rows, cols = len(maze), len(maze[0]) if maze else 0
    
    # Chercher l'entrée (première ligne)
    for col in range(cols):
        if maze[0][col] == '.':
            start = (0, col)
            break
    
    # Chercher la sortie (dernière ligne)
    for col in range(cols):
        if maze[rows-1][col] == '.':
            end = (rows-1, col)
            break
    
    return start, end


def heuristic(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
    """
    Calcule la distance de Manhattan entre deux positions
    
    Args:
        pos1: Position 1 (row, col)
        pos2: Position 2 (row, col)
    
    Returns:
        Distance de Manhattan
    """
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def get_neighbors(position: Tuple[int, int], maze: List[List[str]]) -> List[Tuple[int, int]]:
    """
    Retourne les voisins valides d'une position
    
    Args:
        position: Position actuelle (row, col)
        maze: Matrice du labyrinthe
    
    Returns:
        Liste des positions voisines accessibles
    """
    row, col = position
    rows, cols = len(maze), len(maze[0])
    neighbors = []
    
    # Directions : haut, bas, gauche, droite
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        
        # Vérifier les limites et si la case n'est pas un mur
        if (0 <= new_row < rows and 
            0 <= new_col < cols and 
            maze[new_row][new_col] == '.'):
            neighbors.append((new_row, new_col))
    
    return neighbors


def reconstruct_path(node: Node) -> List[Tuple[int, int]]:
    """
    Reconstruit le chemin depuis le nœud final vers le début
    
    Args:
        node: Nœud final contenant le chemin via les parents
    
    Returns:
        Liste des positions du chemin du début vers la fin
    """
    path = []
    current = node
    while current:
        path.append(current.position)
        current = current.parent
    return path[::-1]  # Inverser pour avoir le chemin du début vers la fin


def a_star_solver(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Implémente l'algorithme A* pour trouver le chemin le plus court
    
    Args:
        maze: Le labyrinthe sous forme de matrice
        start: Position de départ (row, col)
        end: Position d'arrivée (row, col)
    
    Returns:
        Liste des positions du chemin optimal, ou None si aucun chemin n'existe
    """
    
    # Initialisation des structures de données
    open_set = []  # Priority queue des nœuds à explorer
    closed_set: Set[Tuple[int, int]] = set()  # Nœuds déjà explorés
    
    # Créer le nœud de départ
    start_node = Node(start, 0, heuristic(start, end))
    heapq.heappush(open_set, start_node)
    
    # Dictionnaire pour garder trace des meilleurs coûts g pour chaque position
    g_costs = {start: 0}
    
    nodes_explored = 0
    
    while open_set:
        # Récupérer le nœud avec le plus faible f_cost
        current_node = heapq.heappop(open_set)
        current_pos = current_node.position
        
        # Si on a atteint la destination
        if current_pos == end:
            path = reconstruct_path(current_node)
            print(f" Chemin trouvé ! Longueur: {len(path)} cases")
            print(f" Nœuds explorés: {nodes_explored}")
            return path
        
        # Marquer ce nœud comme exploré
        closed_set.add(current_pos)
        nodes_explored += 1
        
        # Explorer tous les voisins
        for neighbor_pos in get_neighbors(current_pos, maze):
            if neighbor_pos in closed_set:
                continue
            
            # Calculer le nouveau coût g (distance depuis le début)
            tentative_g = current_node.g_cost + 1
            
            # Si on a trouvé un meilleur chemin vers ce voisin
            if neighbor_pos not in g_costs or tentative_g < g_costs[neighbor_pos]:
                g_costs[neighbor_pos] = tentative_g
                h_cost = heuristic(neighbor_pos, end)
                neighbor_node = Node(neighbor_pos, tentative_g, h_cost, current_node)
                heapq.heappush(open_set, neighbor_node)
    
    print(f" Aucun chemin trouvé après avoir exploré {nodes_explored} nœuds")
    return None


def visualize_solution(maze: List[List[str]], path: List[Tuple[int, int]]) -> str:
    """
    Crée une représentation visuelle du labyrinthe avec le chemin de solution
    
    Args:
        maze: Le labyrinthe original
        path: Le chemin de solution
    
    Returns:
        String représentant le labyrinthe avec le chemin marqué
    """
    # Créer une copie du labyrinthe
    visual_maze = [row[:] for row in maze]
    
    # Marquer le chemin
    for i, (row, col) in enumerate(path):
        if i == 0:
            visual_maze[row][col] = 'S'  # Start
        elif i == len(path) - 1:
            visual_maze[row][col] = 'E'  # End
        else:
            visual_maze[row][col] = '*'  # Chemin optimal
    
    return '\n'.join(''.join(row) for row in visual_maze)


def solve_maze_astar(filename: str) -> bool:
    """
    Fonction principale pour résoudre un labyrinthe avec A*
    
    Args:
        filename: Nom du fichier contenant le labyrinthe (sans extension)
    
    Returns:
        True si le labyrinthe a été résolu avec succès, False sinon
    """
    print(f"\n === RÉSOLUTION AVEC A* === ")
    print(f" Chargement du fichier: {filename}.txt")
    
    # Charger le labyrinthe
    maze = load_maze_from_file(filename)
    if maze is None:
        return False
    
    print(f" Labyrinthe chargé: {len(maze)}x{len(maze[0])}")
    
    # Trouver le début et la fin
    start, end = find_start_and_end(maze)
    if start is None or end is None:
        print(" Erreur: Impossible de trouver l'entrée ou la sortie du labyrinthe")
        return False
    
    print(f" Départ: {start}")
    print(f" Arrivée: {end}")
    print(" Résolution en cours...")
    
    # Résoudre avec A*
    path = a_star_solver(maze, start, end)
    
    if path:
        print(f"\n LABYRINTHE RÉSOLU AVEC SUCCÈS !")
        print(f" Longueur du chemin optimal: {len(path)} cases")
        
        # Créer la visualisation
        solution_visual = visualize_solution(maze, path)
        
        # Sauvegarder la solution
        solution_filename = f"{filename}_solution_astar"
        try:
            with open(f"labyrinth/{solution_filename}.txt", 'w') as file:
                file.write(solution_visual)
            print(f" Solution sauvegardée dans: labyrinth/{solution_filename}.txt")
        except Exception as e:
            print(f"  Erreur lors de la sauvegarde: {e}")
        
        # Afficher un aperçu de la solution
        print(f"\n  APERÇU DE LA SOLUTION:")
        print(f"   S = Départ | E = Arrivée | * = Chemin optimal")
        print("=" * 60)
        print(solution_visual)
        print("=" * 60)
        
        return True
    else:
        print(" Aucune solution trouvée pour ce labyrinthe")
        return False


# Test de l'algorithme si le fichier est exécuté directement
if __name__ == "__main__":
    print(" Mode test de l'algorithme A*")
    filename = input("Entrez le nom du fichier de labyrinthe à résoudre: ")
    if filename.strip():
        solve_maze_astar(filename)
    else:
        print(" Nom de fichier invalide")