SOPPING CART

Project Description
This is a simple online store model implemented on Swift, where there are three main types of data:
Product — product description
CartItem — basket element (product + quantity)
ShoppingCart is the shopping cart itself, which manages adding and counting items.
The project shows how to use structs and classes,as well as how value types and referenc types work in Swift.

Why is ShoppingCart a class?
I chose the class for ShoppingCart because the shopping cart should be one common object that can be modified from different places in the program.
If the user adds an item to the cart through one screen, the changes should be immediately displayed on the other.
In Swift, classes are reference types, meaning that when passing a bucket variable, not a copy is created, but a reference to the same object.
This makes the behavior more realistic: one bucket means one state for the entire user.

I chose struct for Product and Order because they describe data, not behavior.
They don't need to have an “identity” — all that matters is their meaning.
A product is just a product description (name, price, category, etc.)
An Order is a “snapshot” of the shopping cart at the time of ordering. After creation, the order must be unchanged.
In Swift, structures are value types, so when copying, a new independent copy is created.
This helps to avoid accidental data changes.
