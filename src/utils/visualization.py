import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def _get_positions(node, x, y, gap, positions, edges, depth, max_depth, is_rb=False):
    if node is None:
        return
    if is_rb and node.key is None:
        return
    if depth > max_depth:
        return

    positions[id(node)] = (x, y, node.key, getattr(node, "color", "BLUE"))

    if node.left and (not is_rb or node.left.key is not None):
        edges.append((x, y, x - gap, y - 1))
        _get_positions(node.left, x - gap, y - 1, gap / 2,
                       positions, edges, depth + 1, max_depth, is_rb)

    if node.right and (not is_rb or node.right.key is not None):
        edges.append((x, y, x + gap, y - 1))
        _get_positions(node.right, x + gap, y - 1, gap / 2,
                       positions, edges, depth + 1, max_depth, is_rb)


def visualize_bst(tree, filename, title, is_rb=False):
    positions = {}
    edges = []

    _get_positions(tree.root, 0, 0, 8, positions, edges, 0, 5, is_rb)

    fig, ax = plt.subplots(figsize=(18, 8))
    ax.set_title(title + " (primeros 6 niveles)", fontsize=13)
    ax.axis("off")

    for x1, y1, x2, y2 in edges:
        ax.plot([x1, x2], [y1, y2], "k-", linewidth=0.8, zorder=1)

    for node_id, (x, y, key, color) in positions.items():
        if is_rb:
            bg = "#c0392b" if color == "RED" else "#2c3e50"
            text_color = "white"
        else:
            bg = "#2980b9"
            text_color = "white"

        circle = plt.Circle((x, y), 0.35, color=bg, zorder=2)
        ax.add_patch(circle)
        ax.text(x, y, str(key), ha="center", va="center",
                fontsize=6, color=text_color, zorder=3)

    if positions:
        all_x = [v[0] for v in positions.values()]
        all_y = [v[1] for v in positions.values()]
        ax.set_xlim(min(all_x) - 1, max(all_x) + 1)
        ax.set_ylim(min(all_y) - 1, max(all_y) + 1)

    plt.tight_layout()
    plt.savefig(f"results/{filename}.png", dpi=120)
    plt.close()
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


def plot_summary(promedios):
    escenarios = [
        "Escenario A\n(Aleatorio)", "Escenario B\n(Secuencial)", "Escenario C\n(Frecuente)"]
    bst_vals = [promedios["A"]["bst"],   promedios["B"]
                ["bst"],   promedios["C"]["bst"]]
    splay_vals = [promedios["A"]["splay"], promedios["B"]
                  ["splay"], promedios["C"]["splay"]]
    rb_vals = [promedios["A"]["rb"],    promedios["B"]
               ["rb"],    promedios["C"]["rb"]]

    x = range(len(escenarios))
    ancho = 0.25

    fig, ax = plt.subplots(figsize=(10, 6))

    barras_bst = ax.bar([i - ancho for i in x], bst_vals,
                        width=ancho, label="BST",        color="steelblue")
    barras_splay = ax.bar([i for i in x], splay_vals,
                          width=ancho, label="Splay",       color="orange")
    barras_rb = ax.bar([i + ancho for i in x], rb_vals,
                       width=ancho, label="Red-Black",   color="green")

    for barra in list(barras_bst) + list(barras_splay) + list(barras_rb):
        altura = barra.get_height()
        ax.text(barra.get_x() + barra.get_width() / 2, altura + 0.5,
                f"{altura:.1f}", ha="center", va="bottom", fontsize=8)

    ax.set_xticks(list(x))
    ax.set_xticklabels(escenarios)
    ax.set_ylabel("Iteraciones promedio")
    ax.set_title("Comparacion de iteraciones promedio por arbol y escenario")
    ax.legend()

    plt.tight_layout()
    plt.savefig("results/summary.png")
    plt.close()
    print("Grafica resumen guardada en results/summary.png")
