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
        Ret = []
	For key in (Keys *):
		If hmget(key, ‘category’) == ‘watch’ and hmget(key, ‘brand’) == ‘Tommy Hilfiger’ and hmget(key, ‘dialcolor’) == ‘beige’ and hmget(key, ‘diameter’) == 44 and hmget(key, ‘is_available’) == 1:
			D = {}
    D[‘product_id’] = key
    D[‘product_name’] = hmget(key, ‘product_name’)
    D[‘price’] = hmget(key, ‘price’)
    D[‘category’] = ‘watch’
    D[‘brand’] = ‘Tommy Hilfiger’
    D[‘dialcolor’] = ‘beige’
    D[‘diameter’] = 44
    ret.append(D)
    Return ret
    
    - Approach 5:
      db.watches.find( {dialcolor : ‘beige’, brand: ‘Tommy Hilfiger’, diameter: 44, is_available: 1})
      
### Synopsis:

# Part II:

### Code:

### Output:
