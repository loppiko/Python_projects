# Zadanie z7.2.
#  Zaimplementuj i przetestuj operacje WSTAW, SZUKAJ, USUŃ, DRUKUJ na drzewie poszukiwań binarnych, którego kluczami/elementami są słowa (można przyjąć że zbudowane tylko ze znaków ASCII). Przyjąć, że do drzewa wstawiane są klucze o różnych wartościach, a wypisanie (DRUKUJ) wartości węzłów odbywa się np. w porządku in-order (najlepiej z zaznaczaniem przez odstępy zagłębienia węzłów w drzewie, lub jakiś inny sposób pozwalający zrozumieć strukturę drzewa).

    # 1. Zmierzyć i wypisać wysokość drzewa poszukiwań binarnych uzyskanego w wyniku wstawienia pewnej ilości słów (500, 1000, 2000) do początkowo pustego drzewa. Słowa do wstawienia można brać z dowolnego pliku tekstowego, najlepiej angielskiego, żeby nie było problemów z kodowaniem, np. można wziąć stronę manuala unixowego man python albo man less i wyciągać z takiego pliku słowa, czyli ciągi liter a pominąć pozostałe znaki. Ponadto, w celu sprawdzenia czy drzewa są poprawnie tworzone, wydrukować fragment uworzonego drzewa podobnie jak w zadaniu 7.2, ale tylko do pewnej wysokości.

    # 2. Usunąć z utworzonego drzewa 80% wstawionych słów (zaczynając od tych wstawionych na początku) po czym zmierzyć i wypisać wysokość uzyskanego drzewa. W celu sprawdzenia czy otrzymane drzewo jest poprawne, wydrukować fragment uzyskanego drzewa. 


class Key: 
    def __init__(self, currentKey):
        self.key = currentKey
        self.left = None # lewy syn
        self.right = None # prawy syn
        self.parent = None # ojciec


class BST:
    def __init__(self):
        self.root = None


    def insert(self, insertKey):
      currentKey = self.root
      parentKey = None
      while currentKey != None:
          parentKey = currentKey
          if ( insertKey.key < currentKey.key ):
              currentKey = currentKey.left
          elif (insertKey.key == currentKey.key):
            return False
          else:
              currentKey = currentKey.right
      insertKey.parent = parentKey
      if ( parentKey == None ): # drzewo puste
          self.root = insertKey
      else:
          if ( insertKey.key < parentKey.key ):
              parentKey.left = insertKey
          elif (insertKey.key == parentKey.key):
            return False
          else:
              parentKey.right = insertKey


    def search(self, keyToFind):
        currentKey = self.root
        while ( ( currentKey != None ) and ( currentKey.key != keyToFind ) ):
            if ( keyToFind < currentKey.key ):
                currentKey = currentKey.left
            else:
                currentKey = currentKey.right
        return currentKey           # (None - nie ma klucza w drzewie) 


    def minKey(self, currentKey):
        while ( currentKey.left != None ):
            currentKey = currentKey.left
        return currentKey


    def maxKey(self, currentKey):
        while ( currentKey.right != None ):
            currentKey = currentKey.right
        return currentKey


    def transplant(self, firstKey, secondKey):
        if firstKey.parent == None: 
            self.root = secondKey
        else:
            if firstKey == firstKey.parent.left: 
                firstKey.parent.left = secondKey
            else:
                firstKey.parent.right = secondKey
        if secondKey != None:
                secondKey.parent = firstKey.parent


    def delete(self, keyToDelete):
        if keyToDelete.left == None:
            self.transplant(keyToDelete, keyToDelete.right)
        elif keyToDelete.right == None:
            self.transplant(keyToDelete, keyToDelete.left)
        else:
            subTreeKey = self.minKey(keyToDelete.right)
            if subTreeKey.parent != keyToDelete:
                self.transplant(subTreeKey, subTreeKey.right)
                subTreeKey.right = keyToDelete.right
                subTreeKey.right.parent = subTreeKey
            self.transplant(keyToDelete, subTreeKey)
            subTreeKey.left = keyToDelete.left
            subTreeKey.left.parent = subTreeKey


    def printInOrder(self, currentKey, currentDepth, treeDepth):
        if currentKey == None: 
            return
        if currentDepth <= treeDepth:
            self.printInOrder(currentKey.left, currentDepth + 1, treeDepth)
            print(' ' * 4 * currentDepth, '->', currentKey.key)
            self.printInOrder(currentKey.right, currentDepth + 1, treeDepth)

    
    def depth(self):
        array = []
        def helpDepth(currentKey, depth = 0):
            if currentKey == None:
                array.append(depth)
                return           
            helpDepth(currentKey.left, depth + 1)
            helpDepth(currentKey.right, depth + 1)
        helpDepth(self.root)
        print("Depth of your tree:", max(array))




def file_managment():
    try:
        file = open("consts/hamlet.txt", encoding="utf8")
        array = []
        # print(file)
        for arg in file:
            array.append(arg.split())
        return array
    except:
        print("File does not exist")
        return []


def myFilterOfWords(word):
    result = ""
    for character in word:
        if (character.isalpha()):
            result = result + character
    return result


def insertingWords(readedArrays, amount_of_words):
    counter = 0
    for setOfWords in readedArrays: 
        for word in setOfWords:
            isInserted = True
            if (len(myFilterOfWords(word)) > 0):
                isInserted = tree.insert(Key(myFilterOfWords(word)))
                if (isInserted != False):
                    counter = counter + 1
            if (counter >= amount_of_words):
                return
            

tree = BST() 
amount_of_words = 2000

readedArrays = file_managment() 
insertingWords(readedArrays, amount_of_words)

tree.printInOrder(tree.root, 0, 3)            
tree.depth()

# usunięcie 80% wstawionych węzłów i pomiar głębokości drzewa

for _ in range(int(amount_of_words * 0.8)):
    # print("\n\n\n")
    # tree.printInOrder(tree.root, 0, 3)
    tree.delete(tree.root)

print("\n\nAfter deleting 80% of your elements...\n")
tree.printInOrder(tree.root, 0, 3)
tree.depth()

