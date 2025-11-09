# 🌀 Amazing Mazes - Les Labyrinthes du Minotaure

## 📖 Contexte
Ce projet s’inspire de la légende du labyrinthe de Dédale et du Minotaure.  
L’objectif est de concevoir un **générateur** et un **explorateur** de labyrinthes parfaits, c’est-à-dire avec un **unique chemin reliant deux points**.  
Il combine **algorithmique**, **visualisation** et **résolution automatique**.

---

## ⚙️ Fonctionnalités principales

### Génération de labyrinthes

| Algorithme          | Fonctionnalité              | Sortie                  |
|---------------------|----------------------------|-------------------------|
| DFS (Backtracking)  | Génération du labyrinthe   | ASCII ou image (JPG)    |
| Kruskal             | Génération du labyrinthe   | ASCII ou image (JPG)    |

- Les murs sont représentés par : `#`
- Les espaces vides par : `.`
- Conversion possible en image pour visualisation.

### Exploration et résolution

| Solveur               | Fonctionnalité                 | Visualisation                |
|-----------------------|-------------------------------|------------------------------|
| Recursive Backtracking| Parcours et résolution        | `o` (chemin), `*` (exploré)  |
| A*                    | Parcours optimal              | `o` (chemin), `*` (exploré)  |

### Visualisation

- Labyrinthes ASCII convertis en images (PIL/Pillow)
- Tests de performance jusqu’à des tailles de **4500**
- Comparaison des temps des algorithmes

---

## 📊 Résultats observés

### Génération

| Algorithme | Caractéristique    | Remarque                                     |
|------------|--------------------|----------------------------------------------|
| Kruskal    | Mémoire plus haute | Génère de très grands labyrinthes            |
| DFS        | Mémoire modérée    | Vitesse similaire, tailles toujours impaires |

### Résolution

| Algorithme              | Rapidité     | Mémoire | Remarque                              |
|-------------------------|-------------|---------|---------------------------------------|
| A*                      | Plus rapide | Modérée | Peut résoudre des labyrinthes < 1000  |
| Recursive Backtracking  | Plus lent   | Haute   | Moins efficace sur grands labyrinthes |

---

## 🛠️ Technologies Utilisées

- **Python**
- **PIL / Pillow** (image processing)
- **Algorithmes :** Backtracking, Kruskal, A*
