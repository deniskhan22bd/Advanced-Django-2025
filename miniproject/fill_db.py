import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miniproject.settings')
django.setup()
from users.models import User
from products.models import Category, Tag, Product

def create_superuser():
    if not User.objects.filter(username='denis').exists():
        User.objects.create_superuser('denis', 'denis@example.com', 'denis')
        print("Superuser created.")
    else:
        print("Superuser already exists.")
        
def create_categories_and_tags():
    categories_data = [
        {'name': 'Electronics', 'description': 'Devices, gadgets, and tech products.'},
        {'name': 'Books', 'description': 'Fiction, non-fiction, and educational literature.'},
    ]
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            print(f"Category '{category.name}' created.")
        else:
            print(f"Category '{category.name}' already exists.")
    tags_data = [
        {'name': 'Sale', 'description': 'Products currently on sale.'},
        {'name': 'New Arrival', 'description': 'Recently added products.'},
    ]
    for tag_data in tags_data:
        tag, created = Tag.objects.get_or_create(
            name=tag_data['name'],
            defaults={'description': tag_data['description']}
        )
        if created:
            print(f"Tag '{tag.name}' created.")
        else:
            print(f"Tag '{tag.name}' already exists.")



def create_products():
    seller = User.objects.filter(is_superuser=True).first()
    if not seller:
        print("No superuser found. Please create one first or assign a seller manually.")
        return
    products_data = [
        {"name": "Product 1", "description": "Description for product 1", "price": 10.99, "stock": 100},
        {"name": "Product 2", "description": "Description for product 2", "price": 20.99, "stock": 50},
        {"name": "Product 3", "description": "Description for product 3", "price": 30.99, "stock": 75},
        {"name": "Product 4", "description": "Description for product 4", "price": 40.99, "stock": 25},
        {"name": "Product 5", "description": "Description for product 5", "price": 50.99, "stock": 10},
    ]

    for data in products_data:
        product, created = Product.objects.get_or_create(
            name=data["name"],
            defaults={
                "description": data["description"],
                "price": data["price"],
                "stock": data["stock"],
                "seller": seller,
            }
        )
        if created:
            print(f"Created product: {product.name}")
        else:
            print(f"Product '{product.name}' already exists.")
if __name__ == '__main__':
    create_superuser()
    create_categories_and_tags()
    create_products