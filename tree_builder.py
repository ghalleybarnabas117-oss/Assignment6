class EmployeeNode:

    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    # Delete this line and implement the class below
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
 

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    # Delete this line and implement the class below
    def __init__(self):
        self.root = None
    
    def insert(self, manager_name, employee_name, side, current_node = None):
    
    # Recursively searches for the manager and inserts employee on left or right.
    # If the tree is empty
     if self.root is None:
      print("X Cannot insert. No team lead exists - tree_builder.py:38") 
      return
 
    # Start search from root
     if current_node is None:
        current_node = self.root
        
    # manager found
     if current_node.name == manager_name:
         
        if side == "left":
            if current_node.left is None:
                current_node.left = EmployeeNode(employee_name)
                print(f"{employee_name} is added to the left of {manager_name} - tree_builder.py:51")
            else:
                print (f"Left side of {manager_name} is already occupied. - tree_builder.py:53")
            return
        
        elif side == "right":
            if current_node.right is None:
                current_node.right = EmployeeNode(employee_name)
                print(f"{employee_name}is added to the right of {manager_name} - tree_builder.py:59")
            else:
                print(f"Right side of the {manager_name} is already occupied. - tree_builder.py:61")
            return
        
        else:
            print("X side must be 'Left' or 'Right'. - tree_builder.py:65")
            return
        
        # Recursively search LEFT subtree
        if current_node.left:
            self.insert(manager_name, employee_name, side, current_node.left)
            
        # Recursively search RIGHT subtree
        if current_node.right:
            self.insert(manager_name, employee_name, side, current_node.right)    
    
            
    def print_tree(self, node = None, level = 0):
        
        # start at root
        if node is None:
            node =self.root
            if node is None:
                print("Tree is empty - tree_builder.py:83")
                return
            
        print(" " * level + "- " + node.name)
        
        if node.left:
            self.print_tree(node.left, level + 1) 
            
        if node.right:
            self.print_tree(node.right, level + 1)       
         

# Test your code here
# Testing EmployeeNode

print("Testing EmployeeNode - tree_builder.py:98")
employee_1 = EmployeeNode("Barnabas")
print(employee_1.name) # Barnabas
print(employee_1.left) # None
print(employee_1.right) # None

# Testing TeamTree Root
print("\n Testing TeamTree Root - tree_builder.py:105")
company_directory = TeamTree()
print(company_directory.root) # None

# Testing Insert
print("\n Testing Insert - tree_builder.py:110")
company_directory.root = EmployeeNode("Ms. Manager")
company_directory.insert("Ms. Manager", "Employee #1",  "right")
company_directory.insert("Ms. Manager", "Employee #2", "left")

print(company_directory.root.right.name) # Employee #1
print(company_directory.root.left.name)  # Employee #2

# Testing Print_tree
print("Testing Print_tree - tree_builder.py:119")
company_directory = TeamTree()
company_directory.root = EmployeeNode("David")
company_directory.insert("David", "Rahul","right")
company_directory.insert("David", "Sunil","left")
company_directory.insert("Sunil", "Dina", "right")
company_directory.insert("Sunil", "Morgan", "left")


company_directory.print_tree()


# CLI functionality
def company_directory():
    tree = TeamTree()

    while True:
        print("\n📋 Team Management Menu - tree_builder.py:136")
        print("1. Add Team Lead (root) - tree_builder.py:137")
        print("2. Add Employee - tree_builder.py:138")
        print("3. Print Team Structure - tree_builder.py:139")
        print("4. Exit - tree_builder.py:140")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists. - tree_builder.py:145")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead. - tree_builder.py:149")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure: - tree_builder.py:159")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye! - tree_builder.py:163")
            break
        else:
            print("❌ Invalid option. Try again. - tree_builder.py:166")
         

company_directory()
