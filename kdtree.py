class Node:
    def _init_(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kdtree(points, depth=0, balanced=True):
    if not points:
        return None
    k = len(points[0])
    axis = depth % k

    if balanced:
        points.sort(key=lambda x: x[axis])
        median = len(points) // 2
        return Node(
            points[median],
            left=build_kdtree(points[:median], depth + 1, balanced),
            right=build_kdtree(points[median + 1:], depth + 1, balanced)
        )
    else:
        pivot_index = 0
        pivot = points[pivot_index]
        left_points = [p for p in points if p[axis] < pivot[axis]]
        right_points = [p for p in points if p[axis] > pivot[axis]]
       
        return Node(
            pivot,
            left=build_kdtree(left_points, depth + 1, balanced),
            right=build_kdtree(right_points, depth + 1, balanced)
        )

def display_kdtree(root, depth=0):
    if root is None:
        return
    indent = "  " * depth
    print(indent + str(root.point))
    print(indent + "Left:")
    display_kdtree(root.left, depth + 1)
    print(indent + "Right:")
    display_kdtree(root.right, depth + 1)

def main():
    num_elements = int(input("Enter the number of elements: "))
    dimension = int(input("Enter the dimension: "))
    balanced_input = input("Enter 'balanced' for a balanced tree or 'unbalanced' for an unbalanced tree: ").lower() == 'balanced'
    if balanced_input == 'balanced':
        balanced = True
    else:
        balanced = False
    points = []
    for i in range(num_elements):
        point_str = input(f"Enter coordinates for point {i + 1} (in the format '(x, y)'): ")
        point_str = point_str.strip('()')  
        coords = [float(coord) for coord in point_str.split(',')]  
        points.append(coords)

    root = build_kdtree(points, balanced=balanced)
    if balanced_input == 'balanced':
        print("\n Balanced KD Tree:")
    else:
        print("\n Unbalanced KD Tree:")
 
    display_kdtree(root)

if _name_ == "_main_":
    main()

def display_kdtree(root, depth=0):
    if root is None:
        return
    indent = "  " * depth
    print(indent + "Level", depth, ":", root.point)
    print(indent + "├─ Left:")
    display_kdtree(root.left, depth + 1)
    print(indent + "└─ Right:")
    display_kdtree(root.right, depth + 1)