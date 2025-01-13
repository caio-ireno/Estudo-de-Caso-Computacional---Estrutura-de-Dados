import pytest
from app import BST

@pytest.fixture
def setup_bst():
    """
    Configuração inicial para os testes.
    Cria uma BST e insere alguns IDs de produtos.
    """
    bst = BST()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    return bst

def test_insert_and_search(setup_bst):
    """
    Testa se os nós foram inseridos corretamente e se a busca funciona.
    """
    bst = setup_bst

    # Testando busca por IDs existentes
    assert bst.search(50) is not None
    assert bst.search(30) is not None
    assert bst.search(70) is not None
    assert bst.search(20) is not None
    assert bst.search(40) is not None
    assert bst.search(60) is not None
    assert bst.search(80) is not None

    # Testando busca por IDs não existentes
    assert bst.search(90) is None
    assert bst.search(10) is None


def test_tree_structure(setup_bst):
    """
    Testa a estrutura da árvore binária após inserções.
    """
    bst = setup_bst
    root = bst.root

    # Verificando a raiz
    assert root.key == 50

    # Verificando os filhos da raiz
    assert root.left.key == 30
    assert root.right.key == 70

    # Verificando os netos da raiz
    assert root.left.left.key == 20
    assert root.left.right.key == 40
    assert root.right.left.key == 60
    assert root.right.right.key == 80


def test_insert_duplicate():
    """
    Testa a inserção de chaves duplicadas.
    """
    bst = BST()

    # Inserindo uma chave
    bst.insert(50)

    # Inserindo novamente a mesma chave
    bst.insert(50)

    # Verificando se o nó raiz permanece o mesmo
    assert bst.root is not None
    assert bst.root.key == 50

    # Verificando se não há duplicatas
    assert bst.root.left is None
    assert bst.root.right is None


def test_empty_tree_search():
    """
    Testa a busca em uma árvore vazia.
    """
    bst = BST()
    assert bst.search(50) is None


def test_large_tree():
    """
    Testa a funcionalidade da árvore com um grande número de nós.
    """
    bst = BST()

    # Inserindo 100 nós
    for i in range(1, 101):
        bst.insert(i)

    # Verificando se todos os nós estão presentes
    for i in range(1, 101):
        assert bst.search(i) is not None

    # Verificando se nós fora do intervalo não estão presentes
    assert bst.search(101) is None
    assert bst.search(0) is None
