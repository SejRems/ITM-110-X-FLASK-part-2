session['username'] = 'joben@example.com'

# new shopping cart example
cart = []
cart.append({"code":100,"qty":1})
cart.append({"code":200,"qty":2})
session["cart"] = cart

username = session['username']

# sample action on the username
greetings = "Hello,"+username

#...

# add to shopping cart
item = {"code":300,"qty":1}
session["cart"].append(item)

session.pop("username", None)
