# Database Optimization Strategies

## Introduction  
This document outlines the strategies and techniques used to optimize the PostgreSQL database for the project. The optimizations aim to ensure efficient data storage, fast query execution, and scalability.  

---

## 1. **Normalization and Schema Design**  

### Normalized Schema  
- The database schema follows **3rd Normal Form (3NF)** to eliminate redundancy and ensure data integrity.  
- Entities such as `users`, `categories`, `products`, `orders`, `order_items`, `shopping_carts`, and others are normalized to have primary and foreign keys that minimize duplication.  

### Primary and Foreign Keys  
- **Primary Keys**: Uniquely identify each record in tables (e.g., `id` in `users`, `categories`).  
- **Foreign Keys**: Establish relationships between tables (e.g., `category_id` in `products` references `categories`).  

---

## 2. **Indexing**  

### Primary and Unique Indexes  
- Automatically created for primary keys and unique constraints.  

### Additional Indexing  
1. **Foreign Keys**  
   - Indexed foreign keys (e.g., `category_id` in `products`, `user_id` in `orders`) to speed up JOIN operations.  

2. **Frequently Queried Columns**  
   - Created indexes for fields often used in search or filtering:
     - `name` in `products` (e.g., for product search).  
     - `email` in `users` (e.g., for user login).  
     - `created_at` in `orders` (e.g., for recent order queries).  

3. **Composite Indexes**  
   - Created composite indexes where multiple columns are frequently queried together:
     - `(user_id, product_id)` in `reviews` to optimize review lookups for specific users and products.  

---

## 3. **Query Optimization**  

### Optimized SQL Queries  
1. **Use of SELECT**  
   - Avoid `SELECT *` and only retrieve required columns to minimize data transfer and processing overhead.  

2. **JOIN Operations**  
   - Optimized JOINs by indexing related columns (e.g., `user_id`, `category_id`).  
   - Ensured proper use of INNER JOIN or LEFT JOIN based on requirements to reduce unnecessary processing.

3. **Prepared Statements**  
   - Used prepared statements for frequent queries to leverage query plan caching.  

---

## 4. **Vacuuming and Analyzing**  

- Enabled **autovacuum** to keep statistics up-to-date and prevent table bloat.  
- Scheduled periodic `VACUUM` and `ANALYZE` commands to optimize query planning and performance.  

---

## 5. **Caching**  

- Used a query caching mechanism (e.g., Redis) for frequently accessed data, such as product details or category lists.  
- Reduced database load by implementing cache expiration strategies.  

---

## 6. **Monitoring and Profiling**  

1. **Query Profiling**  
   - Used PostgreSQL's `EXPLAIN` and `EXPLAIN ANALYZE` to understand query execution plans and identify bottlenecks.  

2. **Performance Monitoring**  
   - Monitored database performance using tools such as **pg_stat_statements** and application-level logging for slow queries.  

---

## 7. **Scalability and Maintenance**  

### Partitioning  
- Used table partitioning for large tables such as `orders` and `order_items` based on `created_at` to improve query performance for time-based queries.  

### Connection Pooling  
- Configured connection pooling using tools like **PgBouncer** to manage concurrent connections efficiently.  

---

## Example Optimized Query  

Here is an example of a common query for fetching product details with its associated category:  

```python
queryset = Review.objects.select_related('product_id', 'user_id')
queryset = CartItem.objects.select_related('cart_id', 'product_id')
queryset = OrderItem.objects.select_related('order_id', 'product_id')

```