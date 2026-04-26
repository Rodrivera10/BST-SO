import random

from trees.bst import BST
from trees.splay import SplayTree
from trees.red_black import RedBlackTree

from utils.generator import generate_random, generate_sorted
from utils.metrics import average, min_val, max_val
from utils.visualization import (
    plot_scenario_A,
    plot_scenario_B,
    plot_scenario_C,
    plot_summary,
    visualize_bst
)


def scenario_A():
    print("\n=== ESCENARIO A: Llegada Aleatoria ===")

    data = generate_random(1000)

    bst = BST()
    splay = SplayTree()
    rb = RedBlackTree()

    for x in data:
        bst.insert(x)
        splay.insert(x)
        rb.insert(x)

    visualize_bst(bst, "bst_scenario_A", "BST Escenario A")
    visualize_bst(rb, "rb_scenario_A", "Red-Black Escenario A", is_rb=True)

    test = random.sample(data, 100)

    bst_steps, splay_steps, rb_steps = [], [], []

    for x in test:
        bst_steps.append(bst.search(x)[1])
        splay_steps.append(splay.search(x)[1])
        rb_steps.append(rb.search(x)[1])

    prom_bst = average(bst_steps)
    prom_splay = average(splay_steps)
    prom_rb = average(rb_steps)

    print(
        f"BST       -> promedio: {prom_bst:.2f} | min: {min_val(bst_steps)} | max: {max_val(bst_steps)}")
    print(
        f"Splay     -> promedio: {prom_splay:.2f} | min: {min_val(splay_steps)} | max: {max_val(splay_steps)}")
    print(
        f"Red-Black -> promedio: {prom_rb:.2f} | min: {min_val(rb_steps)} | max: {max_val(rb_steps)}")

    plot_scenario_A(bst_steps, splay_steps, rb_steps)

    return prom_bst, prom_splay, prom_rb


def scenario_B():
    print("\n=== ESCENARIO B: Peor Caso (Insercion Secuencial) ===")

    data = generate_sorted(1000)

    bst = BST()
    splay = SplayTree()
    rb = RedBlackTree()

    for x in data:
        bst.insert(x)
        splay.insert(x)
        rb.insert(x)

    visualize_bst(bst, "bst_scenario_B", "BST Escenario B")

    bst_result = bst.search(1000)[1]
    splay_result = splay.search(1000)[1]
    rb_result = rb.search(1000)[1]

    print(f"BST       -> iteraciones: {bst_result}")
    print(f"Splay     -> iteraciones: {splay_result}")
    print(f"Red-Black -> iteraciones: {rb_result}")

    plot_scenario_B(bst_result, splay_result, rb_result)

    return float(bst_result), float(splay_result), float(rb_result)


def scenario_C():
    print("\n=== ESCENARIO C: Acceso Frecuente ===")

    data = generate_random(1000)

    splay = SplayTree()
    rb = RedBlackTree()

    for x in data:
        splay.insert(x)
        rb.insert(x)

    target = random.choice(data)
    print(f"Proceso buscado 50 veces: {target}")

    splay_steps, rb_steps = [], []

    for _ in range(50):
        splay_steps.append(splay.search(target)[1])
        rb_steps.append(rb.search(target)[1])

    prom_splay = average(splay_steps)
    prom_rb = average(rb_steps)

    print(
        f"Splay     -> promedio: {prom_splay:.2f} | min: {min_val(splay_steps)} | max: {max_val(splay_steps)}")
    print(
        f"Red-Black -> promedio: {prom_rb:.2f} | min: {min_val(rb_steps)} | max: {max_val(rb_steps)}")

    plot_scenario_C(splay_steps, rb_steps)

    return prom_splay, prom_rb


def main():
    print("Iniciando simulacion de arboles BST, Splay y Red-Black Tree\n")

    promedios = {
        "A": {"bst": 0, "splay": 0, "rb": 0},
        "B": {"bst": 0, "splay": 0, "rb": 0},
        "C": {"bst": 0, "splay": 0, "rb": 0},
    }

    try:
        prom_bst, prom_splay, prom_rb = scenario_A()
        promedios["A"] = {"bst": prom_bst, "splay": prom_splay, "rb": prom_rb}
    except Exception as e:
        print(f"Error en Escenario A: {e}")

    try:
        prom_bst, prom_splay, prom_rb = scenario_B()
        promedios["B"] = {"bst": prom_bst, "splay": prom_splay, "rb": prom_rb}
    except Exception as e:
        print(f"Error en Escenario B: {e}")

    try:
        prom_splay, prom_rb = scenario_C()
        promedios["C"] = {"bst": 0, "splay": prom_splay, "rb": prom_rb}
    except Exception as e:
        print(f"Error en Escenario C: {e}")

    try:
        plot_summary(promedios)
    except Exception as e:
        print(f"Error generando grafica resumen: {e}")

    print("\nSimulacion completa. Revisa la carpeta results/ para ver las graficas.")


if __name__ == "__main__":
    main()
