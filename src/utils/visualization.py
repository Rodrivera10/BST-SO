import matplotlib.pyplot as plt
from graphviz import Digraph


def visualize_bst(tree, filename, title, is_rb=False):
    dot = Digraph(comment=title)
    dot.attr(rankdir="TB")

    def add_nodes(node, depth=0):
        if node is None:
            return
        if is_rb and node.key is None:
            return
        if depth > 5:
            return

        label = str(node.key)
        if is_rb:
            color = "red" if node.color == "RED" else "black"
            font_color = "white"
            dot.node(str(id(node)), label, style="filled",
                     fillcolor=color, fontcolor=font_color)
        else:
            dot.node(str(id(node)), label)

        if node.left:
            if not is_rb or node.left.key is not None:
                dot.edge(str(id(node)), str(id(node.left)))
                add_nodes(node.left, depth + 1)

        if node.right:
            if not is_rb or node.right.key is not None:
                dot.edge(str(id(node)), str(id(node.right)))
                add_nodes(node.right, depth + 1)

    add_nodes(tree.root)
    dot.render(f"results/{filename}", format="png", cleanup=True)
    print(f"Arbol guardado en results/{filename}.png")


def plot_scenario_A(bst, splay, rb):
    plt.figure()
    plt.plot(bst, label="BST")
    plt.plot(splay, label="Splay")
    plt.plot(rb, label="Red-Black")

    plt.title("Escenario A - Llegada Aleatoria")
    plt.xlabel("Busqueda (1-100)")
    plt.ylabel("Iteraciones")
    plt.legend()

    plt.savefig("results/scenario_A.png")
    plt.close()


def plot_scenario_B(bst, splay, rb):
    plt.figure()
    labels = ["BST", "Splay", "Red-Black"]
    values = [bst, splay, rb]

    bars = plt.bar(labels, values, color=["steelblue", "orange", "green"])
    for bar, val in zip(bars, values):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5,
                 str(val), ha="center", va="bottom")

    plt.title("Escenario B - Peor Caso (Insercion Secuencial)")
    plt.ylabel("Iteraciones para encontrar proceso 1000")

    plt.savefig("results/scenario_B.png")
    plt.close()


def plot_scenario_C(splay, rb):
    plt.figure()
    plt.plot(splay, label="Splay", marker="o")
    plt.plot(rb, label="Red-Black", marker="s")

    plt.title("Escenario C - Acceso Frecuente al Mismo Proceso")
    plt.xlabel("Intento (1-50)")
    plt.ylabel("Iteraciones")
    plt.legend()

    plt.savefig("results/scenario_C.png")
    plt.close()
