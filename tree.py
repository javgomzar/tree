from typing import Any, Self


def intersect_strings(left: list[str], right: list[str], shift: int):
    if len(left) != len(right):
        raise Exception("Left and right should have the same height")
    
    height = len(left)
    left_width = len(left[0])
    right_width = len(right[0])
    
    if shift == 0:
        return "\n".join([left[i] + " " + right[i] for i in range(0, height)])
    else:
        # Horizontal padding
        while shift > left_width:
            left = [" " + s for s in left]
            left_width += 1
        while shift > right_width:
            right = [s + " " for s in right]
            right_width += 1
    
    result = []
    for left_line, right_line in zip(left, right):
        line = ""
        line += left_line[:left_width - shift]
        for j in range (0, shift):
            left_char = left_line[left_width-shift+j]
            right_char = right_line[j]
            if right_char != " ":
                line += right_char
            else:
                line += left_char
        line += right_line[shift:]
        result.append(line)
    return "\n".join(result)


class Node:
    """
    Class that represents a tree of binary nodes.

    ----------
    **Attributes**:\n
    `data: Any` Data contained in the node (usually a label).  
    `parent: Node` Parent Node.  
    `left: Node` Left child of the node.  
    `right: Node` Right child of the node.  
    """
    data: Any
    parent: Self
    left: Self
    right: Self

    def __init__(self, data: Any) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
    def depth(self) -> int:
        """
        Returns number of nodes between this node and the root of the tree.
        """
        parent = self.parent
        result = 0
        while parent:
            result += 1
            parent = parent.parent
        return result

    def height(self) -> int:
        """
        Returns length of the longest downward chain of nodes.
        """
        left = self.left.height() if self.left else -1
        right = self.right.height() if self.right else -1
        return max(left, right) + 1

    def insert_left(self, data: Any) -> Self:
        """
        Creates a new node with the data provided and attaches it to the left.
        """
        if self.left:
            raise Exception(f"Node {data} alredy has a left child.")
        else:
            child = Node(data)
            self.left = child
            child.parent = self
            return child

    def insert_right(self, data: Any) -> Self:
        """
        Creates a new node with the data provided and attaches it to the right.
        """
        if self.right:
            raise Exception(f"Node {data} alredy has a right child.")
        else:
            child = Node(data)
            self.right = child
            child.parent = self
            return child

    def children(self) -> list[Self]:
        """
        Returns a list with left and right if they exist
        """
        if self.left and self.right:
            return [self.left, self.right]
        elif self.left:
            return [self.left]
        elif self.right:
            return [self.right]
        else:
            return []
    
    def __eq__(self, other: Self) -> bool:
        return self.data == other.data and self.left == other.left and self.right == other.right

    def __repr__(self) -> str:
        """
        Builds a graphical representation of the binary tree drawing nodes recursively.
        """

        # Build left part of the tree
        if self.left:
            left = self.left.__repr__().split("\n")
            left_width = len(left[0])
            left_height = len(left)
            for i, char in enumerate(left[0]):
                if char != " ":
                    left_root = i
                    break

        # Build right part of the tree
        if self.right:
            right = self.right.__repr__().split("\n")
            right_width = len(right[0])
            right_height = len(right)
            for i, char in enumerate(right[0]):
                if char != " ":
                    right_root = i
                    break
        
        if self.left and self.right:
            # Adding spaces so that both sides have the same height
            max_height = max(left_height, right_height)
            while len(left) < max_height:
                left.append(" "*left_width)
            while len(right) < max_height:
                right.append(" "*right_width)
            
            # Trees of depth 1 are easy
            if max_height == 1:
                return "  " + self.data + "  \n / \\ \n" + left[0] + "   " + right[0]

            # If trees are more complex, this code optimizes the spaces for prettyness
            shift = 0
            gap = left_width + right_root - left_root - 3
            if self.left.right:
                last_edge = left[1].rfind("\\")
            else:
                last_edge = -1000
            
            left_cols = [left_width - 1]
            right_cols = [0]
            check_width = 1
            extra_lmargin = 0
            while gap > 1 and left_root + gap > last_edge:
                for j in range(0, check_width):
                    for i in range(0, max_height):
                        left_char = left[i][left_cols[j]]
                        right_char = right[i][right_cols[j]]
                        if left_char != " " and right_char != " ":
                            if shift > 1:
                                shift -= 2
                                gap += 2
                            elif shift == 1:
                                shift -= 1
                                gap += 1
                            break
                    else:
                        continue
                    break
                else:
                    shift += 1
                    gap -= 1
                    if check_width + 1 < left_width and check_width + 1 < right_width:
                        check_width += 1
                        left_cols.insert(0, left_cols[0] - 1)
                        right_cols.append(right_cols[-1] + 1)
                    elif check_width + 1 < left_width:
                        left_cols = [col - 1 for col in left_cols]
                    elif check_width + 1 < right_width:
                        extra_lmargin += 1
                        right_cols = [col + 1 for col in right_cols]
                    else:
                        break
                    continue
                break
            
            # First line
            if shift == 0:
                total_width = left_width + right_width + 1
            elif shift < left_width and shift < right_width:
                total_width = left_width + right_width - shift
            else:
                total_width = max(left_width, right_width)
                if extra_lmargin > 0:
                    extra_lmargin -= 1

            root_line = (" "*(left_root + 2 + extra_lmargin + gap // 2) + str(self.data)).ljust(total_width) + "\n"
            # Second line
            if gap <= 0:
                gap = 1
            edges_line = (" "*(left_root + 1 + extra_lmargin) + "/" + " "*gap + "\\").ljust(total_width) + "\n"

            rest = intersect_strings(left, right, shift)

            result = root_line + edges_line + rest
            debug_result = result.split("\n")
            return result
        elif self.right:
            top_margin = min(2, right_root)
            margin = 2 - top_margin

            root_line = " "*(right_root - top_margin) + str(self.data) + " "*(right_width - right_root + top_margin - 1) + "\n"
            edges_line = " "*(right_root - top_margin + 1) + "\\" + " "*(right_width - right_root + top_margin - 2) + "\n"
            result = root_line + edges_line + ("\n" + margin*" ").join(right)
            debug_result = result.split("\n")

            return result
        elif self.left:
            margin = max(left_root - left_width + 3, 0)

            root_line = " "*(left_root + 2) + str(self.data) + " "*(left_width + margin - left_root - 3) + "\n"
            edges_line = " "*(left_root + 1) + "/" + " "*(left_width + margin - left_root - 2) + "\n"
            result = root_line + edges_line + (margin*" " + "\n").join(left)
            debug_result = result.split("\n")

            return result
        else:
            return str(self.data)
