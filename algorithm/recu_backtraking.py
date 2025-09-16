# recu_backtracking.py - Algorithme Recursive Backtracking pour résoudre des labyrinthes
from typing import List, Tuple, Optional, Set
import time


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


def recu_backtracking_solver(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> Optional[List[Tuple[int, int]]]:
    """
    Implémente l'algorithme Recursive Backtracking pour trouver un chemin
    
    Args:
        maze: Le labyrinthe sous forme de matrice
        start: Position de départ (row, col)
        end: Position d'arrivée (row, col)
    
    Returns:
        Liste des positions d'un chemin trouvé, ou None si aucun chemin n'existe
    """
    
    # Variables pour les statistiques
    nodes_explored = 0
    max_depth = 0
    
    def backtrack(current_pos: Tuple[int, int], path: List[Tuple[int, int]], visited: Set[Tuple[int, int]], depth: int) -> bool:
        """
        Fonction récursive de backtracking
        
        Args:
            current_pos: Position actuelle
            path: Chemin actuel
            visited: Ensemble des positions visitées
            depth: Profondeur actuelle de récursion
        
        Returns:
            True si un chemin vers la sortie a été trouvé, False sinon
        """
        nonlocal nodes_explored, max_depth
        
        nodes_explored += 1
        max_depth = max(max_depth, depth)
        
        # Afficher le progrès de temps en temps
        if nodes_explored % 100 == 0:
            print(f" Exploration... Nœuds visités: {nodes_explored}, Profondeur max: {max_depth}")
        
        # Si on a atteint la destination
        if current_pos == end:
            return True
        
        # Marquer la position actuelle comme visitée
        visited.add(current_pos)
        
        # Explorer tous les voisins
        neighbors = get_neighbors(current_pos, maze)
        
        for neighbor_pos in neighbors:
            # Si le voisin n'a pas été visité
            if neighbor_pos not in visited:
                # Ajouter le voisin au chemin
                path.append(neighbor_pos)
                
                # Récursion : explorer ce voisin
                if backtrack(neighbor_pos, path, visited, depth + 1):
                    return True  # Chemin trouvé !
                
                # Backtrack : retirer le voisin du chemin si ça n'a pas marché
                path.pop()
        
        # Retirer la position actuelle des visitées (backtrack)
        visited.remove(current_pos)
        return False
    
    # Initialiser le chemin avec la position de départ
    path = [start]
    visited = set()
    
    print(" Début de l'exploration par Recursive Backtracking...")
    start_time = time.time()
    
    # Lancer l'algorithme
    if backtrack(start, path, visited, 0):
        end_time = time.time()
        print(f" Chemin trouvé ! Longueur: {len(path)} cases")
        print(f" Nœuds explorés: {nodes_explored}")
        print(f" Profondeur maximale: {max_depth}")
        print(f"  Temps d'exécution: {end_time - start_time:.3f} secondes")
        return path
    else:
        end_time = time.time()
        print(f" Aucun chemin trouvé après avoir exploré {nodes_explored} nœuds")
        print(f"  Temps d'exécution: {end_time - start_time:.3f} secondes")
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
            visual_maze[row][col] = '*'  # Chemin trouvé
    
    return '\n'.join(''.join(row) for row in visual_maze)


def solve_maze_backtracking(filename: str) -> bool:
    """
    Fonction principale pour résoudre un labyrinthe avec Recursive Backtracking
    
    Args:
        filename: Nom du fichier contenant le labyrinthe (sans extension)
    
    Returns:
        True si le labyrinthe a été résolu avec succès, False sinon
    """
    print(f"\n === RÉSOLUTION AVEC RECURSIVE BACKTRACKING === ")
    print(f" Chargement du fichier: {filename}.txt")
    
    # Charger le labyrinthe
    maze = load_maze_from_file(filename)
    if maze is None:
        return False
    
    print(f"📏 Labyrinthe chargé: {len(maze)}x{len(maze[0])}")
    
    # Trouver le début et la fin
    start, end = find_start_and_end(maze)
    if start is None or end is None:
        print(" Erreur: Impossible de trouver l'entrée ou la sortie du labyrinthe")
        return False
    
    print(f" Départ: {start}")
    print(f" Arrivée: {end}")
    print(" Résolution en cours...")
    
    # Résoudre avec Recursive Backtracking
    path = recu_backtracking_solver(maze, start, end)
    
    if path:
        print(f"\n LABYRINTHE RÉSOLU AVEC SUCCÈS !")
        print(f" Longueur du chemin trouvé: {len(path)} cases")
        
        # Créer la visualisation
        solution_visual = visualize_solution(maze, path)
        
        # Sauvegarder la solution
        solution_filename = f"{filename}_solution_backtracking"
        try:
            with open(f"labyrinth/{solution_filename}.txt", 'w') as file:
                file.write(solution_visual)
            print(f" Solution sauvegardée dans: labyrinth/{solution_filename}.txt")
        except Exception as e:
            print(f"  Erreur lors de la sauvegarde: {e}")
        
        # Afficher un aperçu de la solution
        print(f"\n  APERÇU DE LA SOLUTION:")
        print(f"   S = Départ | E = Arrivée | * = Chemin trouvé")
        print("=" * 60)
        print(solution_visual)
        print("=" * 60)
        
        # Note sur l'algorithme
        print(f"\n📝 NOTE: Le Recursive Backtracking trouve UN chemin valide,")
        print(f"   mais pas nécessairement le plus court (contrairement à A*).")
        
        return True
    else:
        print(" Aucune solution trouvée pour ce labyrinthe")
        return False


# Test de l'algorithme si le fichier est exécuté directement
if __name__ == "__main__":
    print("🧪 Mode test de l'algorithme Recursive Backtracking")
    filename = input("Entrez le nom du fichier de labyrinthe à résoudre: ")
    if filename.strip():
        solve_maze_backtracking(filename)
    else:
        print(" Nom de fichier invalide")