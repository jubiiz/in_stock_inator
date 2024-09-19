# General
This is a configuration file located in `./shopping_lists/`. It specifies
a list of target products to check for availability. For each product, 
a corresponding [availability function](#creating-an-availability-function) will check if the product is in stock, pass that result to an [alerting function](#creating-an-alerting-function), which will decide how to alert the user. 

# Schema
## Groups
The shopping list is organized by **groups** of items, where each group has an **availability function** and an **alerting function**. This is done to avoid repeating the same two functions for every one of many items. 

## Items
Each item entry is currently uniquely identified by the URL of the target product.