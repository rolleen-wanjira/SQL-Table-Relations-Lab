# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# CodeGrade step1
# Replace None with your code
df_boston = pd.read_sql(""" 
        SELECT
        e.firstName, 
        e.lastName,
        e.jobTitle
        FROM employees e
        JOIN offices o ON e.officeCode = o.officeCode
        WHERE o.city = 'Boston'    
        """, conn)
print(df_boston)

# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql("""
        SELECT 
            o.officeCode,
            o.city,
            COUNT(e.employeeNumber)
        FROM offices o
        LEFT JOIN employees e ON o.officeCode = e.officeCode
        GROUP BY o.officeCode
        HAVING COUNT(e.employeeNumber) = 0                  
""", conn)
print(df_zero_emp)

# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql(""" 
            SELECT 
            e.firstName, 
            e.lastName, 
            o.city, 
            o.state
            FROM employees e
            LEFT JOIN offices o ON e.officeCode = o.officeCode
            ORDER BY e.firstName, e.lastName   
                """, conn)
print(df_employee)

# CodeGrade step4
# Replace None with your code
df_contacts = pd.read_sql(""" 
            SELECT 
            c.contactFirstName, 
            c.contactLastName,
            c.phone, 
            c.salesRepEmployeeNumber
            FROM customers c
            LEFT JOIN orders o ON c.customerNumber = o.customerNumber
            WHERE o.orderNumber IS NULL
            ORDER BY c.contactLastName              
                          """, conn)
print(df_contacts)

# CodeGrade step5
# Replace None with your code
df_payment = pd.read_sql(""" 
            SELECT 
            c.contactFirstName, 
            c.contactLastName,
            p.amount, 
            p.paymentDate
            FROM customers c
            JOIN payments p ON c.customerNumber = p.customerNumber
            ORDER BY CAST(p.amount AS REAL) DESC             
                         """, conn)
print(df_payment)

# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql(""" 
        SELECT 
        e.employeeNumber, 
        e.firstName, 
        e.lastName,
            COUNT(c.customerNumber)
        FROM employees e
        JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
        GROUP BY e.employeeNumber
        HAVING AVG(CAST(c.creditLimit AS REAL)) > 90000
        ORDER BY COUNT(c.customerNumber) DESC    
""", conn)
print(df_credit)

# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql(""" 
                SELECT 
                p.productName,
                    COUNT(od.orderNumber) AS numorders,
                    SUM(od.quantityOrdered) AS totalunits
                FROM products p
                JOIN orderdetails od ON p.productCode = od.productCode
                GROUP BY p.productCode
                ORDER BY totalunits DESC              
                              """, conn)
print(df_product_sold)

# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql(""" 
                 SELECT 
                 p.productName, 
                 p.productCode,
                    COUNT(DISTINCT o.customerNumber) AS numpurchasers
                FROM products p
                JOIN orderdetails od ON p.productCode = od.productCode
                JOIN orders o ON od.orderNumber = o.orderNumber
                GROUP BY p.productCode
                ORDER BY numpurchasers DESC   
                    """, conn)
print(df_total_customers)

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql(""" 
            SELECT 
            of.officeCode, 
            of.city,
                COUNT(c.customerNumber) AS n_customers
            FROM offices of
            JOIN employees e ON of.officeCode = e.officeCode
            JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
            GROUP BY of.officeCode
            ORDER BY n_customers DESC               
                           """, conn)
print(df_customers)

# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql(""" 
            WITH low_reach_products AS (
                SELECT p.productCode
                FROM products p
                JOIN orderdetails od ON p.productCode = od.productCode
                JOIN orders o ON od.orderNumber = o.orderNumber
                GROUP BY p.productCode
                HAVING COUNT(DISTINCT o.customerNumber) < 20
)
                SELECT DISTINCT e.employeeNumber, e.firstName,
                    e.lastName, of.city, of.officeCode
                FROM employees e
                JOIN offices of ON e.officeCode = of.officeCode
                JOIN customers c ON e.employeeNumber = c.salesRepEmployeeNumber
                JOIN orders o ON c.customerNumber = o.customerNumber
                JOIN orderdetails od ON o.orderNumber = od.orderNumber
                WHERE od.productCode IN
                    (SELECT productCode FROM low_reach_products)              
                          """, conn)
print(df_under_20)

# Run this cell without changes

conn.close()