from django.shortcuts import get_object_or_404, render, redirect
from .models import Category, Product, Cart, CartItem, Purchase, PurchaseItem
from django.contrib.auth.decorators import login_required
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm



def homePage(request):
    products = None
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.objects.filter(category=category_id)
    else:
        products = Product.objects.filter(category=1)
    context = {'products': products, 'categories': categories}
    return render(request, 'frontend/home.html', context)

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("frontend:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm
    return render (request=request, template_name="frontend/signup.html", context={"register_form":form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("frontend:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="frontend/login.html", context={"login_form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("frontend:home")


def add_to_cart(request, product_id):
    # Get the product
    product = get_object_or_404(Product, id=product_id)
    
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get or create a cart for the authenticated user
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For guests, use session to store cart ID
        cart_id = request.session.get("cart_id")
        
        if cart_id:
            # Retrieve existing cart by session ID
            cart = get_object_or_404(Cart, id=cart_id, user=None)
        else:
            # Create a new cart for guest and store cart ID in session
            cart = Cart.objects.create(user=None)
            request.session["cart_id"] = cart.id

    # Get or create a CartItem for this product in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    # If the CartItem already exists, increment the quantity
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Redirect to the cart page or another page
    return redirect('frontend:home')

def delete_from_cart(request, product_id):
    # Determine the cart for the authenticated user or guest session
    if request.user.is_authenticated:
        cart = get_object_or_404(Cart, user=request.user)
    else:
        cart_id = request.session.get("cart_id")
        cart = get_object_or_404(Cart, id=cart_id, user=None) if cart_id else None

    # Ensure the cart and item exist before attempting deletion
    if cart:
        cart_item = CartItem.objects.filter(cart=cart, product_id=product_id).first()
        if cart_item:
            cart_item.delete()

    # Redirect back to the cart page
    return redirect('frontend:cart')

def cart_view(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Get or create a cart for the authenticated user
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        # For guests, use session to store cart ID
        cart_id = request.session.get("cart_id")
        if cart_id:
            # Retrieve existing cart by session ID
            cart = get_object_or_404(Cart, id=cart_id, user=None)
        else:
            # Create a new cart for guest and store cart ID in session
            cart = Cart.objects.create(user=None)
            request.session["cart_id"] = cart.id
    
    # Pass the cart to the template context
    context = {'cart': cart}
    return render(request, 'frontend/cart.html', context)

@login_required
def purchase_view(request):
    # Get the user's cart
    cart = get_object_or_404(Cart, user=request.user)
    
    # Calculate the total price
    total_price = cart.total_price
    
    # Create a new purchase record
    purchase = Purchase.objects.create(user=request.user, total_price=total_price)
    
    # Create purchase items from cart items
    for item in cart.items.all():
        PurchaseItem.objects.create(
            purchase=purchase,
            product=item.product,
            quantity=item.quantity
        )
    
    # Clear the cart (optional)
    cart.items.all().delete()
    
    # Redirect to a confirmation page
    return render(request, 'frontend/purchase_confirmation.html', {'purchase': purchase})