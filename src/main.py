import random

from trees.bst import BST
from trees.splay import SplayTree
from trees.red_black import RedBlackTree

from utils.generator import generate_random, generate_sorted
from utils.metrics import average
from utils.visualization import (
    plot_scenario_A,
    plot_scenario_B,
    plot_scenario_C
)


# ---------------- ESCENARIO A ---------------- #
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

    test = random.sample(data, 100)

    bst_steps, splay_steps, rb_steps = [], [], []

    for x in test:
        bst_steps.append(bst.search(x)[1])
        splay_steps.append(splay.search(x)[1])
        rb_steps.append(rb.search(x)[1])

    print(f"BST promedio: {average(bst_steps):.2f}")
    print(f"Splay promedio: {average(splay_steps):.2f}")
    print(f"Red-Black promedio: {average(rb_steps):.2f}")

    plot_scenario_A(bst_steps, splay_steps, rb_steps)


# ---------------- ESCENARIO B ---------------- #
def scenario_B():
    print("\n=== ESCENARIO B: Peor Caso ===")

    data = generate_sorted(1000)

    bst = BST()
    splay = SplayTree()
    rb = RedBlackTree()

    for x in data:
        bst.insert(x)
        splay.insert(x)
        rb.insert(x)

    bst_result = bst.search(1000)[1]
    splay_result = splay.search(1000)[1]
    rb_result = rb.search(1000)[1]

    print(f"BST iteraciones: {bst_result}")
    print(f"Splay iteraciones: {splay_result}")
    print(f"Red-Black iteraciones: {rb_result}")

    plot_scenario_B(bst_result, splay_result, rb_result)


# ---------------- ESCENARIO C ---------------- #
def scenario_C():
    print("\n=== ESCENARIO C: Acceso Frecuente ===")

    data = generate_random(1000)

    splay = SplayTree()
    rb = RedBlackTree()

    for x in data:
        splay.insert(x)
        rb.insert(x)

    target = random.choice(data)
    print(f"Proceso elegido: {target}")

    splay_steps, rb_steps = [], []

    for _ in range(50):
        splay_steps.append(splay.search(target)[1])
        rb_steps.append(rb.search(target)[1])

    print(f"Splay promedio: {average(splay_steps):.2f}")
    print(f"Red-Black promedio: {average(rb_steps):.2f}")

    plot_scenario_C(splay_steps, rb_steps)


# ---------------- MAIN ---------------- #
def main():
    scenario_A()
    scenario_B()
    scenario_C()


if __name__ == "__main__":
    main()