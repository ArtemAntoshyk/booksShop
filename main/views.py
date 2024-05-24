from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        'title': 'Home - MAIN',
        'content': "Books store LIFE-BOOK",
        'text_on_page': """
        
        
        """
    }

    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'About us',
        'content': "About us",
        'text_on_page': """
Welcome to Life Book, your ultimate destination for all things literary! Our online bookstore is a haven for book lovers, offering an extensive selection of books across a multitude of genres and formats. Whether you're seeking the latest bestseller, a classic novel, or a niche title, we have something to ignite your passion for reading.

At Life Book, we believe in the power of stories to inspire, educate, and transform. Our carefully curated collection features books for all ages and interests, from fiction and non-fiction to children's books, academic texts, and beyond. We are committed to providing our customers with a seamless and enjoyable shopping experience, ensuring that you find the perfect book every time.

Why choose Life Book?

Diverse Selection: Our catalog spans a wide range of genres and subjects, catering to readers with varied tastes and preferences. From mystery and romance to science fiction and biographies, there's a book for everyone.

Quality Service: We pride ourselves on our customer service. Our knowledgeable and friendly team is always ready to assist you with recommendations, queries, or any concerns you might have.

Competitive Prices: We strive to make reading accessible to all by offering competitive prices and regular discounts. Our goal is to bring the joy of reading to everyone, without breaking the bank.

Convenience: Shop from the comfort of your home and enjoy fast, reliable shipping. Our user-friendly website makes it easy to browse, search, and purchase books with just a few clicks.

Community: We are more than just a bookstore; we are a community of book enthusiasts. Join us for author events, book clubs, and discussions, both online and offline, and connect with fellow readers from around the world.

At Life Book, we are passionate about books and dedicated to fostering a love for reading. Thank you for choosing us as your go-to online bookstore. Happy reading!
"""
    }

    return render(request, 'main/about.html', context)
