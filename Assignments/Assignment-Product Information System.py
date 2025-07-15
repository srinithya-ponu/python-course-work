#DSLR Camera product details

product_id = 1908
product_name = "Nikon D850 DSLR Camera"
price = 289999.00
categories = ["Photography", "Videography", "Content Creation"]
stock_available = 40
stock_sold = 15
stock_details = (stock_available, stock_sold)
discount_percentage = 7.5
product_features = {"4K Video", "WiFi Transfer", "Time-Lapse Mode"}
supplier_details = {
    "Name": "LensWorld Distributors",
    "Contact": "+91-9345612309",
    "Location": "Hyderabad"
}
print("\n***Product Details***")


# Supplier details
supplier_name = supplier_details["Name"]
supplier_contact = supplier_details["Contact"]
supplier_location = supplier_details["Location"]

#1. Using comma separation
print("Product ID:", product_id)
print("Product Name:", product_name)
print("Price:", price)
print("Categories:", categories)
print("Stock Details:", stock_details)
print("Discount Percentage:", discount_percentage)
print("Product Features:", product_features)
print("Supplier Details:", supplier_details)

#2. Using percentage formatting
print("\n*** Using % formatting ***")
print("Product ID: %d" % product_id)
print("Product Name: %s" % product_name)
print("Price: ₹%.2f" % price)
print("Discount: %.1f%%" % discount_percentage)
print("Supplier: %s" % supplier_name)
print("Contact: %s" % supplier_contact)
print("Location: %s" % supplier_location)

#3. Using f-strings
# Calculate price after discount
final_price = price - (price * discount_percentage / 100)
#categories as text
categories_text = ", ".join(categories)
#stock details
available = stock_details[0]
sold = stock_details[1]
#stock details
available = stock_details[0]
sold = stock_details[1]
#features as text
features_text = ", ".join(product_features)
print("\n*** Using f-strings ***")
print(f"Product ID: {product_id}")
print(f"Product Name: {product_name}")
print(f"Price after discount: ₹{final_price:.2f}")
print(f"Categories: {categories_text}")
print(f"Stock - Available: {available}, Sold: {sold}")
print(f"Features: {features_text}")
print(f"Supplier: {supplier_name} ({supplier_contact}) at {supplier_location}")


#4. Using .format() method
print("\n*** Using .format() method ***")
print("Original Price: ₹{:.2f}".format(price))
print("Discount: {}%".format(discount_percentage))
print("Final Price after discount: ₹{:.2f}".format(final_price))
print("Categories: {}".format(categories_text))
print("Stock Available: {}".format(stock_details[0]))
print("Stock Sold: {}".format(stock_details[1]))
print("Features: {}".format(features_text))
print("Supplier Name: {}".format(supplier_name))
print("Supplier Contact: {}".format(supplier_contact))
print("Supplier Location: {}".format(supplier_location))






#OUTPUT:

#***Product Details***
#Product ID: 1908
#Product Name: Nikon D850 DSLR Camera
#Price: 289999.0
#Categories: ['Photography', 'Videography', 'Content Creation']
#Stock Details: (40, 15)
#Discount Percentage: 7.5
##Product Features: {'WiFi Transfer', '4K Video', 'Time-Lapse Mode'}
#Supplier Details: {'Name': 'LensWorld Distributors', 'Contact': '+91-9345612309', 'Location': 'Hyderabad'}

#*** Using % formatting ***
#Product ID: 1908
#Product Name: Nikon D850 DSLR Camera
#Price: ₹289999.00
#Discount: 7.5%
#Supplier: LensWorld Distributors
#Contact: +91-9345612309
#Location: Hyderabad

#*** Using f-strings ***
#Product ID: 1908
#Product Name: Nikon D850 DSLR Camera
#Price after discount: ₹268249.08
#Categories: Photography, Videography, Content Creation
#Stock - Available: 40, Sold: 15
#Features: WiFi Transfer, 4K Video, Time-Lapse Mode
#Supplier: LensWorld Distributors (+91-9345612309) at Hyderabad

#*** Using .format() method ***
#Original Price: ₹289999.00
#Discount: 7.5%
#Final Price after discount: ₹268249.08
#Categories: Photography, Videography, Content Creation
#Stock Available: 40
#Stock Sold: 15
#Features: WiFi Transfer, 4K Video, Time-Lapse Mode
#Supplier Name: LensWorld Distributors
#Supplier Contact: +91-9345612309
#Supplier Location: Hyderabad

