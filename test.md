/*--------------------------------------------------------------------------------------------------------*/
/* Open the following link in your browser then copy and past the exercise into the online SQL compiler:
/* https://www.programiz.com/sql/online-compiler/
/*--------------------------------------------------------------------------------------------------------*/

/* Q1.
* Orders in this table were created from 2021-2022, but the OrderDate are all off by 25 years
  orders from 2021 show as 1996 and orders from 2022 show as 1997
* What functions could you use to correct the year of each order date?
* How would you go about writing a script to correct the year of all orders?
*/

SELECT  OrderId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderDate -- DATE
FROM my_database.my_schema.orders
;

/* Q2.
* Some orders from the orders table were deleted, and later recovered in a separate table.
  we are not sure if all orders from the recovered data were deleted from the orders table.
* How would you write a script that looked for OrderIds in both tables?
* How would you go about writing a script that would combine the recovered data with the
  data from the orders table without duplicating any of the Orders?
*/

SELECT  OrderId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderDate -- DATE
FROM my_database.my_schema.recovered_orders
;

SELECT  OrderId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderDate -- DATE
FROM my_database.my_schema.orders
;

/* Q3.
* When the orders from the orders table were deleted and later recovered, we also lost
  some of the order detail data for those orders.
  We were able to recover some of the order details data, but not all of it.
* How would you write a script that combines the order details data with the recovered
  orders detail data and excludes ant duplicates? (pick any solution from the previous exercise)
* How would you write a script that returns all OrderId from the orders table that have no
  OrderDetailId in the now combined order_details table?
* How would you go about removing orders from the order table that have no order details in
  the order_details table?
*/

SELECT  OrderDetailId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderId -- INTEGER (NOT NULL FOREIGN KEY REFERENCES recovered_orders.OrderID)
      , ProductId -- INTEGER (NOT NULL FOREIGN KEY REFERENCES products.ProductID)
      , Quantity -- INTEGER (NOT NULL)
FROM my_database.my_schema.recovered_order_details
;

SELECT  OrderDetailId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderId -- INTEGER (NOT NULL FOREIGN KEY REFERENCES orders.OrderID)
      , ProductId -- INTEGER (NOT NULL FOREIGN KEY REFERENCES products.ProductID)
      , Quantity -- INTEGER (NOT NULL)
FROM my_database.my_schema.order_details
;


SELECT  OrderId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderDate -- DATE
FROM my_database.my_schema.orders
;

/* Q4.
* Using the products, orders, and order_detail tables write a script that
   will return the total cost of all products *per OrderId*, name the column: CostPerOrderId
* Calculate the Average CostPerOrderId, *rounded to the nearest dollar*
   and group and sort it by the Month of the OrderDate
* Use any function to add a UniqueRowId to each row in the final result
* Create a view named: my_database.my_schema.vw_avg_cost_per_order from the script
*/

SELECT  ProductId -- INTEGER (NOT NULL PRIMARY KEY)
      , Price -- FLOAT64 (NOT NULL)
FROM my_database.my_schema.products
;

SELECT  OrderId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderDate -- DATE
FROM my_database.my_schema.orders
;

SELECT  OrderDetailId -- INTEGER (NOT NULL PRIMARY KEY)
      , OrderId -- INTEGER (NOT NULL FOREIGN KEY REFERENCES orders.OrderID)
      , ProductId -- INTEGER (NOT NULL FOREIGN KEY REFERENCES products.ProductID)
      , Quantity -- INTEGER (NOT NULL)
FROM my_database.my_schema.order_details
;

/*--------------------------------------------------------------------------------------------------------*/