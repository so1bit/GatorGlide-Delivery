import sys
class OrderManagementSystem:
    def __init__(self, order_id, current_system_time, orderValue, newDeliveryTime):
        #Initializes an instance of the OrderManagementSystem class.
        self.order_id = order_id
        self.current_system_time = current_system_time
        self.orderValue = orderValue
        self.time = newDeliveryTime
        self.ETA = 0
        self.priority = self.Priority()


    def Priority(self):
        
        #Calculates the priority of the order based on order orderValue and current system time.
        valW, timW = 0.3, 0.7
        N = self.orderValue/50
        priority = valW * N - timW * self.current_system_time
        return priority


class Node:
    def __init__(self, k, orderValue):
        #Initializes an instance of the Node class.
       
        self.k = k
        self.order = orderValue 
        self.left = None
        self.right = None
        self.ht = 1




# Initialize system time
sysT = 0


# Global output ip list
op = []

# Function to create a new order
def createOrder(order_id, current_system_time, orderValue, time):
    global op, sysT, delI
    sysT = current_system_time
    nO = OrderManagementSystem(order_id, current_system_time, orderValue, time)
    nO = calculateETA(nO) 
    if delI is None:
        delI = nO 
    if nO.current_system_time >= delI.ETA:
        Del(1)

# Function to calculate ETA for a new order
def calculateETA(nO):
    global op


    # Get the ino traversal of T1
    ino = T1.traversal(T1.root)

    # If T1 is empty, set ETA based on current system time and delivery time
    if T1.root is None:
        nO.ETA = nO.current_system_time + nO.time


    # If T1 has only one node, set ETA based on the root node's ETA and delivery time
    elif T1.root.left is None and T1.root.right is None:
        nO.ETA = T1.root.order.ETA + T1.root.order.time + nO.time

    # If the new order has higher priority than the first node in T1, set ETA accordingly
    elif float(ino[0][0]) > float(nO.priority):
        nO.ETA = nO.time + ino[0][1].ETA + ino[0][1].time


    # Otherwise, find the correct position to insert the new order in T1 and update ETAs
    else:
        j = 0
        x = ino[::-1]
        i = 0
        while i < len(x):
            if float(nO.priority) > float(x[i][0]):
                if x[i][1].order_id == delI.order_id:
                    i += 1
                    continue
                x.insert(i, (float(nO.priority), nO))
                j = i
                break
            i += 1

        # Update the ETA of the new order and the following OrderManagementSystem in T1
        if j != 0:
            nO.ETA = nO.time + x[j-1][1].ETA + x[j-1][1].time
            x[j][1].ETA = nO.ETA
            j += 1


        # Insert the new order in T1 and T2
        T1.keyval(float(nO.priority), nO)
        T2.keyval(nO.ETA, nO)

        # Append the print string to global output ip
        prt = "Order " + str(nO.order_id) + " has been created - ETA: " + str(nO.ETA)
        op.append(prt)


        # Update ETAs for the remaining OrderManagementSystem in T1
        ls = []
        k = j
        while k < len(x):
            t1 = T1.AVLTree_1(T1.root, x[k][0], x[k][1].order_id)
            t2 = T2.AVLTree_2(T2.root, x[k][1].ETA)
            x[k][1].ETA = x[k-1][1].ETA + x[k-1][1].time + x[k][1].time

            T1.delNode(T1.root, t1.k, t1.order.order_id)
            T2.delNode(T2.root, t2.k, t2.order.order_id)

            T1.keyval(float(x[k][1].priority), x[k][1])
            T2.keyval(x[k][1].ETA, x[k][1])

            ls.append(str(x[k][1].order_id) + ":" + str(x[k][1].ETA))
            k += 1

        # Append the updated ETAs print string to global output ip
        prt = "Updated ETAs: ["
        if len(ls) == 1:
            prt += ls[0]
        else:
            for i in ls:
                if i == ls[-1]:
                    prt += i
                else:
                    prt += i + ","
        prt += "]"
        op.append(prt)

        return nO

    # If T1 is empty, set ETA based on current system time and delivery time
    T1.keyval(float(nO.priority), nO)
    T2.keyval(nO.ETA, nO)

    # Append the print string to global output ip
    prt = "Order " + str(nO.order_id) + " has been created - ETA: " + str(nO.ETA)
    op.append(prt)

    return nO

# Initialize last delivered order and delivery item
last = None
delI = None

# Dictionary to store delivered OrderManagementSystem
delivered = {}

# Function to flush delivery based on the given flag
def Del(flag):
    global delI, last, op
    
    actions = {
        1: lambda: deliver_single_order(),
        0: lambda: deliver_all_OrderManagementSystem(),
        2: lambda: deliver_overdue_OrderManagementSystem()
    }
    
    action = actions.get(flag, lambda: None)
    action()

# Function to deliver a single order
def deliver_single_order():
    global delI, last, op
    
    if delI:
        order_order_id = delI.order_id
        eta = delI.ETA
        op.append(f"Order {order_order_id} has been delivered at time {eta}")
        delivered[int(order_order_id)] = delI
        last = order_order_id
        T1.delNode(T1.root, float(delI.priority), order_order_id)
        T2.delNode(T2.root, eta, order_order_id)
        delI = T1.getMax(T1.root).order

# Function to deliver all OrderManagementSystem
def deliver_all_OrderManagementSystem():
    global delI, last, op
    
    for node in T2.traversal(T2.root):
        order_order_id = int(node[1].order_id)
        eta = int(node[1].ETA)
        op.append(f"Order {order_order_id} has been delivered at time {eta}")

# Function to deliver overdue OrderManagementSystem
def deliver_overdue_OrderManagementSystem():
    global delI, last, op
    
    for node in T2.traversal(T2.root):
        if node[1].ETA <= sysT:
            order_order_id = int(delI.order_id)
            eta = int(delI.ETA)
            op.append(f"Order {order_order_id} has been delivered at time {eta}")
            delivered[int(delI.order_id)] = delI
            last = delI.order_id
            T1.delNode(T1.root, float(delI.priority), order_order_id)
            T2.delNode(T2.root, delI.ETA, order_order_id)
            delI = T1.getMax(T1.root).order

# Function to print order details
def printOrdersID(order_id):
    print(order_id)

# Function to print order delivery times within a given time range
def printOrdersT(time1, time2):
    ans = [str(i[1].order_id) for i in T2.traversal(T2.root) if int(i[0]) >= int(time1) and int(i[0]) <= int(time2)]
    prt = f"[{','.join(ans)}]" if ans else "There are no orders in that time period"
    op.append(prt)

# Function to cancel an order
def cancelOrder(order_id, current_system_time):
    global op, sysT
    sysT = current_system_time

    # Check if the order has already been delivered
    if int(order_id) in delivered:
        op.append("Cannot cancel. Order {} has already been delivered".format(order_id))
        return
    
    # Check if the order is currently being delivered
    if int(order_id) == int(delI.order_id) and sysT < delivered[last].ETA + delivered[last].time:
        op.append("Cannot cancel. Order {} has already been delivered".format(order_id))
        return

    # Search for the order in T1
    ino = T1.traversal(T1.root)
    order = next((i[1] for i in ino if order_id == i[1].order_id), None)
    if not order:
        return op.append("No order found with order_id {} in that time period".format(order_id))
    
    # Find the position of the order in the ino traversal
    x = ino[::-1]
    j = 0
    while j < len(x):
        if float(order.priority) == float(x[j][0]) and order.order_id == x[j][1].order_id:
            break
        j += 1
    
    # Delete the order from T1 and T2
    T1.delNode(T1.root, x[j][0], x[j][1].order_id)
    T2.delNode(T2.root, x[j][1].ETA, x[j][1].order_id)
    x.pop(j)

    op.append("Order {} has been canceled".format(order_id))

    # Update the ETAs of the remaining OrderManagementSystem
    if j < len(x):
        if j == 0:
            flagETA = x[0][1].time + delI.ETA + delI.time
            T1.delNode(T1.root, x[0][0], x[0][1].order_id)
            T2.delNode(T2.root, x[0][1].ETA, x[0][1].order_id)
            x[0][1].ETA = flagETA
            T1.insertkorderValue(x[0][0], x[0][1])
            T2.insertkorderValue(x[0][1].ETA, x[0][1])
            j += 1
        
        # Initialize an empty list
        ls = []
        i = j
        while i < len(x):
            # Search for the node in T1 and T2
            t1 = T1.AVLTree_1(T1.root, x[i][0], x[i][1].order_id)
            t2 = T2.AVLTree_2(T2.root, x[i][1].ETA)
            
            # Update the ETA of the current order
            x[i][1].ETA = x[i-1][1].ETA + x[i-1][1].time + x[i][1].time
            
            # Delete the node from T1 and T2
            T1.delNode(T1.root, t1.k, t1.order.order_id)
            T2.delNode(T2.root, t2.k, t2.order.order_id)
            
            # Insert the updated order into T1 and T2
            T1.keyval(float(x[i][1].priority), x[i][1])
            T2.keyval(x[i][1].ETA, x[i][1])

            # Append the order order_id and ETA to the list
            ls.append("{}: {}".format(x[i][1].order_id, x[i][1].ETA))
            i += 1
        
        # Append the updated ETAs to the global output ip
        op.append("Updated ETAs: [{}]".format(",".join(ls)))


# Function to get the rank of an order in the delivery sequence
def getRankOfOrder(order_id):
    global op
    if order_id in delivered:
        return
    if order_id == delI.order_id:
        op.append(f"Order {order_id} will be delivered after 0 Order.")
        return
    ans = [node[1].order_id for node in T1.traversal(T1.root)][::-1]
    try:
        c = ans.index(order_id)
        op.append(f"Order {order_id} will be delivered after {c} orders.")
    except ValueError:
        pass

# Function to update the delivery time of an order
def updateTime(order_id, current_system_time, newtime):
    # Initialize variables
    global op, sysT, delivered, delI, last, T1, T2

    sysT = current_system_time

    # Check if the order has already been delivered
    if int(order_id) in delivered:
        op.append(f"Cannot update. Order {order_id} has already been delivered")
        return
    
    # Check if the order is currently being delivered
    if int(order_id) == int(delI.order_id):
        x1 = delivered[last].ETA
        x2 = delivered[last].time
        if sysT >= x1 + x2:
            op.append(f"Cannot update. Order {order_id} has already been delivered")
            return

    # Search for the order in T1
    ino = T1.traversal(T1.root)
    order = next((i[1] for i in ino if order_id == i[1].order_id), None)
    
    # Find the position of the order in the ino traversal
    x = ino[::-1]
    j = next((i for i, node in enumerate(x) if float(order.priority) == float(node[0]) and order.order_id == node[1].order_id), 0)
    
    # Search for the order in T1 and T2
    nodeT1 = T1.AVLTree_1(T1.root, x[j][0], x[j][1].order_id)
    nodeA2 = T2.AVLTree_2(T2.root, x[j][1].ETA)

    # Update the delivery time and ETA of the order
    oldtime1 = nodeT1.order.time
    nodeT1.order.time = newtime
    nodeT1.order.ETA = nodeT1.order.ETA - oldtime1 + newtime
    nodeA2.k = nodeT1.order.ETA

    # Create a list to store the updated ETAs
    ls = [f"{nodeT1.order.order_id}:{nodeT1.order.ETA}"]

    j += 1


    # Update the ETAs of the remaining OrderManagementSystem
    while j < len(x):
        t1 = T1.AVLTree_1(T1.root, x[j][0], x[j][1].order_id)
        t2 = T2.AVLTree_2(T2.root, x[j][1].ETA)
        x[j][1].ETA = x[j-1][1].ETA + x[j-1][1].time + x[j][1].time
        
        # Delete the order from T1 and T2
        T1.delNode(T1.root, t1.k, t1.order.order_id)
        T2.delNode(T2.root, t2.k, t2.order.order_id)

        # Insert the order with updated ETA into T1 and T2
        T1.keyval(float(x[j][1].priority), x[j][1])
        T2.keyval(x[j][1].ETA, x[j][1])

        # Append the updated ETA to the list
        ls.append(f"{x[j][1].order_id}:{x[j][1].ETA}")
        j += 1
        
    # Append the updated ETAs to the global output ip
    op.append(f"Updated ETAs: [{','.join(ls)}]")

def main(filename):
    # Create output file name
    output = filename.split('.')[0] + "_output_file.txt"

    # Open input file for reading and output file for writing
    with open(filename, 'r') as file, open(output, "w") as file2:
        # Read each line from the input file
        ip = file.readlines()
        for line in ip:
            line = line.strip()
            command_type = line.split("(")[0]

            # Check if the command is Quit()
            if line == "Quit()":
                Del(0)
                break

            # Check if the command is createOrder
            if command_type == "createOrder": 
                params = line.split("(")[1].split(")")[0].split(",")
                order_id, current_system_time, orderValue, time = map(int, params)
                createOrder(order_id, current_system_time, orderValue, time)

            # Check if the command is cancelOrder
            elif command_type == "cancelOrder":
                params = line[len("cancelOrder("):-1].split(", ")
                order_id, current_system_time = map(int, params)
                cancelOrder(order_id, current_system_time)
                Del(2)

            # Check if the command is print
            elif command_type == "print": 
                cc = line[len("print("):-1]
                if "," in cc:
                    t1, t2 = map(int, cc.replace(" ", "").split(","))
                    printOrdersT(t1, t2)

            # Check if the command is getRankOfOrder
            elif command_type == "getRankOfOrder": 
                order_id = int(line[len("getRankOfOrder("):-1])
                getRankOfOrder(order_id)

            # Check if the command is updateTime
            elif command_type == "updateTime": 
                params = line[len("updateTime("):-1].split(", ")
                order_id, current_system_time, newtime = map(int, params)
                updateTime(order_id, current_system_time, newtime)
                Del(2)

        # Write the global output ip to the output file
        for line in op:
            file2.write(line + "\n")
        file2.close()

class AVLTree:
    def __init__(self):
        """
        Initializes an instance of the AVLTree class.
        The root node of the AVL tree.
        """
        self.root = None
    
    def ht(self, node):
        """
        Calculates the height of a node.
        The node for which to calculate the height.
        """
        if node is None:
            return 0
        return node.ht
    
    def bf(self, node):
        #Calculates the bal factor of a node.
        if node is None:
            return 0
        return self.ht(node.left) - self.ht(node.right)

    def Uht(self, node):
        """
        Updates the ht of a node.
        node: The node for which to update the ht.
        """
        node.ht = 1 + max(self.ht(node.left), self.ht(node.right))

    def rT(self, b):
        #Performs a right rotation on a node.
        a = b.left
        A2 = a.right
        a.right = b
        b.left = A2

        self.Uht(b)
        self.Uht(a)
        return a

    def lT(self, a):
        #Performs a left rotation on a node.
        b = a.right
        A2 = b.left
        b.left = a
        a.right = A2
        self.Uht(a)
        self.Uht(b)
        return b

    def bal(self, node):
        #Balances the AVL tree.
        self.Uht(node)

        bal = self.bf(node)

        if bal > 1 and self.bf(node.left) >= 0:
            return self.rT(node)

        if bal < -1 and self.bf(node.left) <= 0:
            return self.lT(node)

        if bal > 1 and self.bf(node.left) < 0:
            node.left = self.lT(node.left)
            return self.rT(node)

        if bal < -1 and self.bf(node.right) > 0:
            node.right = self.rT(node.right)
            return self.lT(node)

        return node

    def insert(self, root, k, orderValue):
        """
        Inserts a new node into the AVL tree.
        """
        if not root:
            return Node(k, orderValue)
        elif k < root.k:
            root.left = self.insert(root.left, k, orderValue)
        else:
            root.right = self.insert(root.right, k, orderValue)
    
        root = self.bal(root)

        return root
    
   
    def keyval(self, k, orderValue):
        """
        Inserts a new node into the AVL tree using k-orderValue pair.
        """
        self.root = self.insert(self.root, k, orderValue)
    
    
    def delNode(self, root, k, order_id):
        #Deletes a node from the AVL tree.
        self.root = self.delete(root, k, order_id)


    def delete(self, root, k, order_id):
        #Deletes a node from the AVL tree.
        if not root:
            return root
        elif k < root.k:
            root.left = self.delete(root.left, k, order_id)
        elif k > root.k:
            root.right = self.delete(root.right, k, order_id)
        else:
            if root.order.order_id != order_id:
                root.right = self.delete(root.right, k, order_id)
            else:
                if root.left is None:
                    flag = root.right
                    root = None
                    return flag
                elif root.right is None:
                    flag = root.left
                    root = None
                    return flag
                flag = self.getMin(root.right)
                root.k = flag.k
                root.order = flag.order
                root.right = self.delete(root.right, flag.k, flag.order.order_id)

        if root is None:
            return root

        root = self.bal(root)
        return root
    

    def getMin(self, root):
        """
        Returns the node with the minimum orderValue in the AVL tree.
        """
        if root is None or root.left is None:
            return root
        return self.getMin(root.left)


    def getMax(self, root):
        """
        Returns the node with the maximum orderValue in the AVL tree.
        """
        if root is None or root.right is None:
            return root
        return self.getMax(root.right)

    def traversal(self, node):
        """
        Performs an ino traversal of the AVL tree and returns the nodes in a list.
        """
        ans = []
        if node:
            ans.extend(self.traversal(node.left))
            ans.append((node.k, node.order))
            ans.extend(self.traversal(node.right))
        return ans

    
    def AVLTree_1(self, root, k, order_id):
        """
        Searches for a node with the given k and order_id in the AVL tree.
        Returns the node if found, otherwise returns None.
        """
        if not root:
            return None
        elif k < root.k:
            return self.AVLTree_1(root.left, k, order_id)
        elif k > root.k:
            return self.AVLTree_1(root.right, k, order_id)
        else:
            if(root.order.order_id == order_id):
                return root
            return self.AVLTree_1(root.right, k, order_id)
    
   
    def AVLTree_2(self, root, k):
        """
        Searches for a node with the given k in the AVL tree.
        Returns the node if found, otherwise returns None.
        """
        if not root:
            return None
        elif k < root.k:
            return self.AVLTree_2(root.left, k)
        elif k > root.k:
            return self.AVLTree_2(root.right, k)
        else:
            return root

# Create AVL trees for OrderManagementSystem
T1, T2 = AVLTree(), AVLTree()

if __name__ == "__main__":
    main(sys.argv[1])