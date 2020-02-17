# Homework 3 Writeup (Jack Tonina & Steve Setteducatti)

## NOTE
Please check the product_catalogs directory for all of our code since we reused some code from HW1 and HW2. We thought that adjusting our directory structure for this made the most sense in a program organizational manner.

# PART I: 

### SQL Queries:
    - Approach 1: 
            SELECT product_name,
			   brand,
			   diameter
			   dial_color,
			   price
		FROM products
		WHERE category = ‘Watches’
            AND diameter = 44
		AND brand = ‘Tommy Hilfiger’
		AND dial_color = ‘Beige’
		AND is_available = 1
		ORDER BY price ASC
		    
    - Approach 2: 
            SELECT p.product_name,
			   w.brand,
			   w.dial_color,
			   w.diameter,
			   p.price
		FROM product p
		INNER JOIN category c
		ON p.category_id = c.category_id
		INNER JOIN watches w
		ON w.product_id = p.product_id
		WHERE c.category_name = ‘Watches’
            AND = w.diameter = 44
		AND w.brand = ‘Tommy Hilfiger’
		AND w.dial_color = ‘Beige’
		AND p.is_available = 1
		ORDER BY p.price ASC

    - Approach 3:
            SELECT p.product_name,
			   w.brand,
			   w.dial_color,
			   w.diameter,
			   p.price
		FROM product p
		INNER JOIN category c
		ON p.category_id = c.category_id
		INNER JOIN watches w
		ON w.product_id = p.product_id
		WHERE c.category_name = ‘Watches’
            AND = w.diameter = 44
		AND w.brand = ‘Tommy Hilfiger’
		AND w.dial_color = ‘Beige’
		AND p.is_available = 1
		ORDER BY p.price ASC
 
    - Approach 4:
        # This is a combination of pseudocode and python for simplicity's sake
        Ret = []
        
	    For key in (Keys *):
		If hmget(key, ‘category’) == ‘watch’ and hmget(key, ‘brand’) == ‘Tommy Hilfiger’ and hmget(key, ‘dialcolor’) == ‘beige’ and hmget(key, ‘diameter’) == 44 and hmget(key, ‘is_available’) == 1:
		    D = {}
		    D[‘product_id’] = key
                D[‘product_name’] = hmget(key, ‘product_name’)
                D[‘price’] = hmget(key, ‘price’)
                D[‘category’] = ‘watch’
                D[‘brand’] = ‘Tommy Hilfiger’
                D[‘dial_color’] = ‘beige’
                D[‘diameter’] = 44
                D['is_available'] = 1
                ret.append(D)
        Return ret
    
    - Approach 5:
        db.watches.find( {dial_color : ‘beige’, brand: ‘Tommy Hilfiger’, diameter: 44, is_available: 1})
      
### Synopsis:
    - Approach 1: This approach equires you to include many more attributes (which will for the most part be NULLs) due to the 
    fact it needs to hold data for thousands of categories in one table. Because it has to hold tens of millions of products, 
    it will take a long time to query this one table, especially given many input conditions. However, not needing to join across 
    multiple large tables is an advantage in terms of speed and efficiency. The database admin is going to have a heart attack 
    because this approach doesn’t follow any type of normal form. This orientationis ideal for machine learning approaches 
    since an analytical dataset is readily available with all fields and some simple feature generation can be done to condense 
    this dataset into a more concise model.

    - Approach 2: This approach requires joining across three tables in order to pull information for a specific query with 
    multiple conditions, which can take time especially for categories with lots of products. Is efficient in terms of 
    minimizing the amount of data held in total, as opposed to the first strategy where each row has to have data for every 
    attribute across every product category (majority NULLs), this method only requires you to fill attributes relevant to 
    the specific category. One final challenge with this strategy may be that joining to each unique category table requires 
    precise naming conventions (changing / updating category names).

    - Approach 3: With approach 3, joining to and the querying from the Property table may be inefficient as it has one row 
    for each attribute of each product, which ends up being millions and millions of rows. This would require subquerying 
    or self joins in order to execute a query searching for multiple conditions which is not overly efficient. Comparing 
    this to strategy two above, this is less efficient in the sense that querying for a category with 5 attributes requires 
    you to read through the table 5 times regardless of how many products in the category you are querying for, where as in 
    strategy two you just query through the specific table of products in that category.

    - Approach 4: Using a key-value store approach, Each key is the product id which is a unique identifier for the product. 
    This key points to a hashmap which contains all of the values for that product. The process here requires you to loop 
    through every key that we have stored in the database and check if it meets the requirements of a query by checking the 
    hashmap for its values against the required attributes for the query. There are other approaches where we could store 
    all of each category in a list where the key is category name and the value is a list of product ids but this still would 
    require pulling out each product id and checking its hashmap for whether or not the attributes meet the query expectations. 
    It is limited by the fact that there is no such thing as querying by field in key-value stores and is inherently a slow 
    process.
    
    - Approach 5: The database has a collection for each category that could be queried on. Then once the collection is 
    selected, one could leverage Mongo to query directly against the attributes we are looking for. It is incredibly simple 
    and supports the changing attribute structure of each category very well.


# Part II:

### Code:

    def run_queries(db_conn):
        with db_conn() as db:
            collection = "Watches"
            query = {
                "dial_color": "beige",
                "brand": "Tommy Hilfiger",
                "diameter": 40,
                "is_available": 1,
            }
        return db.run_query(collection, query)

### Output:

    [{'_id': ObjectId('5e457db5293feea95ae0d277'), 'product_id': 71, 'product_name': 'johnson', 'brand': 'Tommy Hilfiger', 'color': 'beige', 'price': 6870, 'diameter': 40, 'dial_color': 'beige', 'is_available': 1}]

# Contributions
MongoConnector.py - Steve
generate_products.py - Jack
insert_products.py - Steve
get_products.py - Steve and Jack
utils.py - Steve and Jack (similar to hw2)
ReadMe - Jack