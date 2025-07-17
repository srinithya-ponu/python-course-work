#Tata Neu App

product_id = 301
product_name = "Tata 1mg Full Body Checkup Package"
price = 1299.00
categories = ["Health", "Diagnostics", "Wellness"]
stock_details = (500, 1200)
discount_percentage = 20.0
product_features = {"Free Home Sample Pickup", "Digital Report", "Certified Labs", "Doctor Consultation"}
supplier_details = {
    "Name": "Tata 1mg Labs",
    "Contact": "+91-9205920205",
    "Location": "Hyderabad"
}

final_price = price - (price * discount_percentage / 100)

categories_text = ", ".join(categories)
features_text = ", ".join(product_features)
available, sold = stock_details
supplier_name = supplier_details["Name"]
supplier_contact = supplier_details["Contact"]
supplier_location = supplier_details["Location"]

# 1. Comma-Separated Display
print("\n*** Comma-Separated Display ***")
print("Product ID:", product_id)
print("Product Name:", product_name)
print("Price:", price)
print("Categories:", categories)
print("Stock Details:", stock_details)
print("Discount:", discount_percentage)
print("Features:", product_features)
print("Supplier:", supplier_details)

# 2. Percentage (%) Formatting
print("\n*** Using % Formatting ***")
print("Product ID: %d" % product_id)
print("Product Name: %s" % product_name)
print("Price: ₹%.2f" % price)
print("Discount: %.1f%%" % discount_percentage)
print("Supplier: %s, Contact: %s, Location: %s" %
      (supplier_name, supplier_contact, supplier_location))

# 3. F-Strings
print("\n*** Using f-strings ***")
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price after discount: ₹{final_price:.2f}")
print(f"Categories: {categories_text}")
print(f"Stock - Available: {available}, Sold: {sold}")
print(f"Features: {features_text}")
print(f"Supplier: {supplier_name} ({supplier_contact}) at {supplier_location}")

# 4. .format() Method
print("\n*** Using .format() Method ***")
print("Product: {} | ID: {}".format(product_name, product_id))
print("Original Price: ₹{:.2f} | Discount: {}%".format(price, discount_percentage))
print("Final Price: ₹{:.2f}".format(final_price))
print("Categories: {}".format(categories_text))
print("Stock Details: Available - {}, Sold - {}".format(available, sold))
print("Features: {}".format(features_text))
print("Supplier: {Name} | Contact: {Contact} | Location: {Location}".format(**supplier_details))





