# 🌀 Amazing Mazes - Les Labyrinthes du Minotaure

## 📖 Contexte
Ce projet s’inspire de la légende du labyrinthe de Dédale et du Minotaure.  
L’objectif est de concevoir un **générateur** et un **explorateur** de labyrinthes parfaits, c’est-à-dire avec un **unique chemin reliant deux points**.  
Il combine **algorithmique**, **visualisation** et **résolution automatique**.

---

## ⚙️ Fonctionnalités principales

### 🔹 Génération de labyrinthes
- Implémentation de **deux algorithmes de génération** :
  - **DFS (Backtracking)**
  - **Kruskal**
- Production d’un fichier texte représentant :
  - `#` = murs  
  - `.` = espaces vides
- Conversion possible en **image (JPG)** pour une meilleure visualisation.

### 🔹 Exploration et résolution
- Implémentation de **deux solveurs automatiques** :
  - **Recursive Backtracking**
  - **A\***
- Visualisation de la solution :
  - `o` = chemin optimal trouvé
  - `*` = cases explorées

### 🔹 Visualisation avancée
- Conversion des labyrinthes ASCII en images (via **PIL / Pillow**).
- Tests de performances sur des tailles croissantes (jusqu’à **4500**).
- Comparaison des temps de génération et de résolution entre les algorithmes.

---

## 📊 Résultats observés

### Génération
- Les tailles de labyrinthe sont toujours ajustées en **impair** pour garantir une meilleure qualité.  
- **Kruskal** a un pic de mémoire plus élevé mais génère des labyrinthes de très grande taille.  
- **DFS (Backtracking)** et **Kruskal** prennent un temps globalement similaire.

### Exploration
- **A\*** résout les labyrinthes **plus rapidement** que le Backtracking récursif.  
- Le **Recursive Backtracking** consomme souvent plus de mémoire et prend plus de temps.  
- **A\*** parvient à résoudre des labyrinthes de taille plus importante (**< 1000**).