import matplotlib.pyplot as plt


def plot_scenario_A(bst, splay, rb):
    plt.figure()
    plt.plot(bst, label="BST")
    plt.plot(splay, label="Splay")
    plt.plot(rb, label="Red-Black")

    plt.title("Escenario A - Aleatorio")
    plt.xlabel("Pruebas")
    plt.ylabel("Iteraciones")
    plt.legend()

    plt.savefig("results/scenario_A.png")
    plt.show()


def plot_scenario_B(bst, splay, rb):
    plt.figure()
    labels = ["BST", "Splay", "Red-Black"]
    values = [bst, splay, rb]

    plt.bar(labels, values)

    plt.title("Escenario B - Peor Caso")
    plt.ylabel("Iteraciones")

    plt.savefig("results/scenario_B.png")
    plt.show()


def plot_scenario_C(splay, rb):
    plt.figure()
    plt.plot(splay, label="Splay")
    plt.plot(rb, label="Red-Black")

    plt.title("Escenario C - Acceso Frecuente")
    plt.xlabel("Intento")
    plt.ylabel("Iteraciones")
    plt.legend()

    plt.savefig("results/scenario_C.png")
    plt.show()