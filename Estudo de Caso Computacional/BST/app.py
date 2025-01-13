class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:  # Se o ID for menor, vai para a esquerda
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_recursive(current.left, key)
        if key > current.key:  # Se o ID for maior ou igual, vai para a direita
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_recursive(current.right, key)
        else:
            print("ID já existente. Não é possível inserir.")
            return

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if current is None or current.key == key:
            return current
        if key < current.key:
            return self._search_recursive(current.left, key)
        return self._search_recursive(current.right, key)

# Criando a árvore de produtos
product_tree = BST()

# Inserindo IDs de produtos
product_tree.insert(50)  # Produto com ID 50
product_tree.insert(30)  # Produto com ID 30
product_tree.insert(70)  # Produto com ID 70
product_tree.insert(20)  # Produto com ID 20
product_tree.insert(40)  # Produto com ID 40
product_tree.insert(60)  # Produto com ID 60
product_tree.insert(80)  # Produto com ID 80

# Testando a busca por um ID
produto_procurado = 60
resultado = product_tree.search(produto_procurado)

if resultado:
    print(f"Produto com ID {produto_procurado} encontrado.")
else:
    print(f"Produto com ID {produto_procurado} não encontrado.")
