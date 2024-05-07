import numpy as np

class Node:
    def __init__(self, point, left=None, right=None, parent=None):
        self.point = point
        self.left = left
        self.right = right
        self.parent = parent

def build_unbalanced_kd_tree(points, depth=0, parent=None):
    if len(points) == 0:
        return None

    axis = depth % len(points[0])
    root_point = points[0]
    root = Node(root_point, parent=parent)

    left_points = [p for p in points[1:] if p[axis] < root_point[axis]]
    right_points = [p for p in points[1:] if p[axis] >= root_point[axis]]

    root.left = build_unbalanced_kd_tree(left_points, depth + 1, root)
    root.right = build_unbalanced_kd_tree(right_points, depth + 1, root)

    return root

def build_balanced_kd_tree(points, depth=0, parent=None):
    if len(points) == 0:
        return None

    axis = depth % len(points[0])
    points_sorted = points[np.argsort(points[:, axis])]
    median_index = (len(points_sorted)-1) // 2

    median_point = points_sorted[median_index]
    root = Node(median_point, parent=parent)

    root.left = build_balanced_kd_tree(points_sorted[:median_index], depth + 1, root)
    root.right = build_balanced_kd_tree(points_sorted[median_index + 1:], depth + 1, root)

    return root

def print_tree(node):
    if node is None:
        return

    parent_point = node.parent.point if node.parent else None
    left_point = node.left.point if node.left else None
    right_point = node.right.point if node.right else None

    print(f"Point: {node.point}, Parent: {parent_point}, Left: {left_point}, Right: {right_point}")

    print_tree(node.left)
    print_tree(node.right)

def main():
    points = np.array([[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]])
    print("Select KD tree type:")
    print("1. Unbalanced KD Tree")
    print("2. Balanced KD Tree")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Unbalanced KD Tree:")
        kd_tree = build_unbalanced_kd_tree(points)
    elif choice == 2:
        print("Balanced KD Tree:")
        kd_tree = build_balanced_kd_tree(points)
    else:
        print("Invalid choice.")
        return

    print_tree(kd_tree)

if __name__ == "__main__":
    main()
