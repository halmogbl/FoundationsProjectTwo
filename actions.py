# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Almogbl's Site"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print (store.name)

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store.name == store_name:
            return store
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!
    print_stores()
    store_picked = input('Pick a store by typing its name. Or type "checkout" to pay your bills and say your goodbyes.')
    if store_picked == "checkout":
        return "checkout"
    
    elif get_store(store_picked):
        return get_store(store_picked)
    else:
        print("Invalid Store")
    

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()
    print("Write the name of the product or back")
    flag=False
    while True:
        user_input= input()
        if user_input == "back":
            break
        else:
            for product in picked_store.products:
                if product.name == user_input:
                    cart.add_to_cart(product)
                    print("item has ben added to  cart")
                    flag= True
            if flag== False:
                print("this item doesnt exist")


def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    store=pick_store()
    while True:
        if store=="checkout":
            break
        elif store:
            pick_products(cart,store) 
        store=pick_store()

    cart.checkout()
    # your code goes here!

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
