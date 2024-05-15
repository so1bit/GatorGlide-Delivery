
---

# GatorGlide-Delivery

## Introduction

GatorGlide-Delivery is an Order Management System built in Python, leveraging AVL trees for efficient order prioritization and delivery time estimation. This system aims to streamline order handling processes while demonstrating proficiency in data structures, algorithm design, and software development methodologies.

## System Overview

The Order Management System comprises several key functionalities designed to enhance order management and optimize delivery processes. These functionalities include:

- Creation and management of individual orders
- Prioritization of orders based on various factors including order value and current system time
- Efficient storage and organization of orders using AVL trees
- Calculation of Estimated Time of Arrival (ETA) for each order
- Delivery of orders based on their priority and current system time

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/so1bit/GatorGlide-Delivery.git
    ```

2. Navigate to the project directory:

    ```bash
    cd GatorGlide-Delivery
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Import the Order Management System module:

    ```python
    import order_management_system
    ```

2. Initialize the Order Management System:

    ```python
    order_system = order_management_system.OrderManagementSystem()
    ```

3. Utilize the provided functionalities such as creating orders, delivering orders, canceling orders, and updating order details.

## Classes and Functions

### Order Management System Class

Represents an individual order in the system with attributes like order ID, order value, delivery time, ETA, and priority.

### Node Class

Represents a node in the AVL tree used for order management.

### AVL Tree Class

Implements the AVL tree data structure for efficient order management, including insertion, deletion, balancing, searching, and traversal operations.

### Functions

- `create_order(order_details)`: Creates a new order with the given parameters and calculates its ETA.
- `deliver_single_order()`: Delivers the order with the highest priority.
- `deliver_all_OrderManagementSystem()`: Delivers all orders in the system.
- `deliver_overdue_OrderManagementSystem()`: Delivers overdue orders.
- `printOrdersID(order_id)`: Prints the details of a specific order.
- `printOrdersTIME(time1, time2)`: Prints orders within a given time range.
- `cancelOrder(order_id, current_system_time)`: Cancels an order.
- `getRankOfOrder(order_id)`: Gets the rank of an order in the delivery sequence.
- `Update Time(order_id, current_system_time, newtime)`: Updates the delivery time of an order.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
