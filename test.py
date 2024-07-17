import unittest as ut
from unittest import TestCase as Test

from tree import Node


class TestTree(Test):
    tree_1: Node
    tree_2: Node
    J: Node

    def setUp(self):
        self.tree_1 = Node("A")
        B = self.tree_1.insert_left("B")
        C = self.tree_1.insert_right("C")
        D = C.insert_left("D")
        E = D.insert_left("E")
        F = E.insert_right("F")
        G = F.insert_right("G")
        self.G = G
        H = G.insert_left("H")
        I = H.insert_left("I")
        J = H.insert_right("J")
        self.J = J
        K = G.insert_right("K")
        L = K.insert_right("L")
        M = K.insert_left("M")

        self.tree_2 = Node("0")
        n1 = self.tree_2.insert_left("1")
        n2 = self.tree_2.insert_right("1")
        n3 = n1.insert_left("2")
        n4 = n1.insert_right("2")
        n5 = n2.insert_left("2")
        n6 = n2.insert_right("2")
        n7 = n3.insert_left("3")
        n8 = n3.insert_right("3")
        n9 = n4.insert_left("3")
        n10 = n4.insert_right("3")
        n11 = n5.insert_left("3")
        n12 = n5.insert_right("3")
        n13 = n6.insert_left("3")
        n14 = n6.insert_right("3")

    def test_depth(self):
        self.assertEqual(self.tree_1.depth(), 0)
        self.assertEqual(self.J.depth(), 7)
        print("\nTest depth is correct.")
    
    def test_height(self):
        self.assertEqual(self.tree_1.height(), 7)
        self.assertEqual(self.J.height(), 0)
        print("\nTest height is correct.")

    def test_eq(self):
        self.assertEqual(self.tree_1, self.tree_1)
        print("\nTest eq is correct.")

    def test_print_1(self):
        print("\n")
        print("TEST 1:")
        print(self.G)

    def test_print_2(self):
        print("\n")
        print("TEST 2:")
        print(self.tree_1)
    
    def test_print_3(self):
        print("\n")
        print("TEST 3:")
        print(self.tree_2)

    def test_print_4(self):
        print("\n")
        print("TEST 4:")
        root = Node("X")
        root.left = self.tree_2
        root.insert_right("Y")
        print(root)

    def test_print_5(self):
        print("\n")
        print("TEST 5:")
        root = Node("X")
        root.left = self.tree_1
        root.right = self.tree_2
        print(root)
    
    def test_print_6(self):
        print("\n")
        print("TEST 6:")
        root = Node("X")
        root.left = self.tree_2
        root.right = self.tree_1
        print(root)


if __name__ == "__main__":
    ut.main()