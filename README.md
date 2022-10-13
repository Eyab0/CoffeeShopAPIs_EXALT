
# Coffee Shop APIs Project - EXALT Traning

Backend service for a coffee shop that manages  the employees and customers and  allows them to take customer orders.


## Features

- Authentication and Authorization via a role-based control design pattern
- Ability to perform CRUD shop on orders, employees, customers, items, and bills.


## ER Diagram

![CoffeeShopProjectERD](https://user-images.githubusercontent.com/61092637/195473532-dc6e429f-78a7-473b-b017-67699e0329e5.jpg)


## API Reference

### Register a new employee

```http
  POST /manager/employee
```

`Request Body`:
```yaml
{
  "name": "Ahmad Ahmad",
  "phone_number": 0596581120,
  "role": "cashier",
  "username": "ahmad99",
  "password": "123"
}
```

`Response`:
```yaml
{
  "message": "Created new Employee."
  "Employee":
    {
      "name": "Ahmad Ahmad",
      "phone_number": 0596581120,
      "join_date":'2022-09-01',
      "role": "cashier",
      "username": "ahmad99",
      "status": "Active"
    }
  
}

```

### Login as an Employee

```http
  POST /auth/login
```

`Request Body`:
```yaml
{
  "username": "ahmad99",
  "password": "123"
}
```

`Response`:
```yaml
{
  "access_token": "secret"
}
```

### Get all employees

```http
  GET /manager/employees
```

| Parameter | Type     | Description                                 |
|:----------| :------- |:--------------------------------------------|
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |

`Response`:
```yaml
[
  {
    "phone_number": 555,
    "id": 1,
    "role": "cashier"
    "name": "Ahmad Ahmad"
  },
  {
    "phone_number": 444,
    "id": 2,
    "role": "manager"
    "name": "David"
  }
]
```


### Get employee

```http
  GET /manager/employees/${employee_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `employee_id`| `integer` | **Required**. Id of employee to fetch |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
{
  "phone_number": 555,
  "id": 1,
  "role": "cashier"
  "name": "Ahmad Ahmad",
  "status": "Active"
}
```
### Update employee

```http
  PUT /manager/employees/${employee_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `employee_id`| `integer` | **Required**. Id of employee to update |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Request Body`:
```yaml
{
  "phone_number": 111,
  "name": "Ahmad Ahmad",
  "status": "Deactivated"
}
``` 

`Response`:
```yaml
{
  "phone_number": 111,
  "id": 1,
  "name": "Ahmad Ahmad"
}
```


### Get all items

```http
  GET /shop/items
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
[
  {
    "id": 1,
    "name": "Curry Chicken with Onion",
    "price": "$7.00"
  },
  {
    "id": 2,
    "name": "Chicken with Black Beans",
    "price": "$7.00"
  }
]
```

### Create item

```http
  POST /shop/items
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Request Body`:
```yaml
{
  "name": "Curry Chicken with Onion",
  "price": "$7.00"
}
```

`Response`:
```yaml
{
  "id": 1,
  "name": "Curry Chicken with Onion",
  "price": "$7.00"
}
```

### Delete item

```http
  DELETE /shop/items/${item_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id`| `integer` | **Required**. Id of item to delete |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
{
  "id": 1,
  "name": "Curry Chicken with Onion",
  "price": "$7.00"
}
```
### Get item

```http 
  GET /shop/items/${item_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id`| `integer` | **Required**. Id of item to fetch |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
{
  "id": 1,
  "name": "Curry Chicken with Onion",
  "price": "$7.00"
}
```

### Update item

```http
  PUT /shop/employees/${item_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id`| `integer` | **Required**. Id of item to update |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Request Body`:
```yaml
{
  "name": "Curry Chicken with Onion",
  "price": "$10.00"
}
```

`Response`:
```yaml
{
  "id": 1,
  "name": "Curry Chicken with Onion",
  "price": "$10.00"
}
```

### Get all customers

```http
  GET /shop/customers
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |

`Response`:
```yaml
[
  {
    "phone_number": 1,
    "id": 1,
    "name": "one"
  },
  {
    "phone_number": 2,
    "id": 2,
    "name": "two"
  }
]
```

### Create customer

```http
  POST /shop/customers
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |

`Request Body`:
```yaml
{
  "phone_number": 3,
  "name": "Osama"
}
```


`Response`:
```yaml
{
  "id": 3,
  "phone_number": 3,
  "name": "Osama"
}
```

### Delete customer

```http
  DELETE /shop/customers/${customer_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer_id`| `integer` | **Required**. Id of customer to delete |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
{
  "id": 3,
  "phone_number": 3,
  "name": "Osama"
}
```
### Get customer

```http
  GET /shop/customers/${employee_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer_id`| `integer` | **Required**. Id of customer to fetch |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
{
  "id": 3,
  "phone_number": 3,
  "name": "Osama" 
}
```

### Update customer

```http 
  PUT /shop/customers/${customer_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `customer_id`| `integer` | **Required**. Id of customer to update |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Request Body`:
```yaml
{ 
  "phone_number": 4,
  "name": "David"
}
```

`Response`:
```yaml
{
  "id": 4,
  "phone_number": 4,
  "name": "David"
}
```

### Get all orders

```http
  GET /shop/orders
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |

`Response`:
```yaml
[
 {
  "customer_id": 2,
  "employee_id": 5,
  "id": 7,
  "items_ordered": [
    {
      "description": "no salt",
      "item_id": 1,
      "quantity": 1
    }
  ],
  "order_time": "2022-07-25T07:20:08.023003",
  "status": "in Progress"
},
{
  "customer_id": 1,
  "employee_id": 2,
  "id": 12,
  "items_ordered": [
    {
      "description": "A LOT OF SALT",
      "item_id": 5,
      "quantity": 2
    },
    {
      "description": "NO SUGAR",
      "item_id": 4,
      "quantity": 2
    }
  ],
  "order_time": "2022-07-25T07:20:08.023003",
  "status": "in Progress"
]
```

### Create order

```http
  POST /shop/orders
```


| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |

`Request Body`:
```yaml
{
  "customer_id": 2,
  "employee_id": 3,
  "items_ordered": [
    {
      "description": "extra salt",
      "item_id": 3,
      "quantity": 2
    }
  ],
  "status": "in Progress"
}
```


`Response`:
```yaml
{
  "customer_id": 2,
  "employee_id": 1,
  "id": 19,
  "items_ordered": [
    {
      "description": "extra salt",
      "item_id": 3,
      "quantity": 2
    }
  ],
  "order_time": "2022-07-25T10:12:40.397597",
  "status": "in Progress"
}
```

### Delete order

```http
  DELETE /shop/orders/${order_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_id`| `integer` | **Required**. Id of order to delete |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:

```yaml
{
  "customer_id": 2,
  "employee_id": 1,
  "id": 19,
  "items_ordered": [
    {
      "description": "extra salt",
      "item_id": 3,
      "quantity": 2
    }
  ],
  "order_time": "2022-07-25T10:12:40.397597",
  "status": "Canceled"
}
```
### Get order

```http
  GET /shop/orders/${order_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_id`| `integer` | **Required**. Id of order to fetch |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
{
  "customer_id": 1,
  "employee_id": 2,
  "id": 12,
  "items_ordered": [
    {
      "description": "A LOT OF SALT",
      "item_id": 5,
      "quantity": 2
    },
    {
      "description": "NO SUGAR",
      "item_id": 4,
      "quantity": 2
    }
  ],
  "order_time": "2022-07-25T07:44:11.668169",
  "status": "in Progress"
}
```
### Update order

```http
  PUT /shop/orders/${order_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `order_id`| `integer` | **Required**. Id of order to update |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Request Body`:
```yaml
{
  "customer_id": 1,
  "employee_id": 2,
  "items_ordered": [
    {
      "description": "chicken tika masala",
      "item_id": 1,
      "quantity": 2
    }
  ],  
  "status": "Done"
}
```


`Response`:
```yaml
{
  "customer_id": 1,
  "employee_id": 2,
  "id": 12,
  "items_ordered": [
    {
      "description": "chicken tika masala",
      "item_id": 1,
      "quantity": 2
    }
  ],
  "order_time": "2022-07-25T07:44:11.668169",
  "status": "Done"
}
```

### Read all bills

```http
  GET /shop/bill
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |


`Response`:
```yaml
[
    {
        "customer_id": 1,
        "employee_id": 1,
        "order_id": 1,
        "price": "12"
    },
    {
        "customer_id": 1,
        "employee_id": 2,
        "order_id": 2,
        "price": "13"
    },
]
```

### Get receipt

```http
  GET /operation/bill/${order_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee |

`Response`:
```yaml
{
    "customer_id": 1,
    "employee_id": 1,
    "order_id": 1,
    "price": "12"
}
```

### Create receipt

```http
  POST /shop/bill/${order_id}
```

| Parameter | Type     | Description                                      |
| :-------- | :------- |:-------------------------------------------------|
| `order_id`| `integer` | **Required**. Id of order to find the receipt of |
| `Token`   | `Bearer Token` | **Required**. JWT of an authorized employee      |


```yaml
{
    "customer_id": 1,
    "employee_id": 1,
    "order_id": 1,
    "price": "$67.50"
}
```

## Authors

- [@Eyab Ghifari](https://www.github.com/Eyab0)
