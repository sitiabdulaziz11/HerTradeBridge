# HerTradeBridge
💫 HerCommerce — Empowering Women Entrepreneurs Through Digital Access

🌸 A digital marketplace platform designed to help women entrepreneurs grow their customer base, showcase products, and build trust through technology.

✨ Overview

HerCommerce is a web platform that helps women with home-based or small-scale businesses (like butter or food sellers) reach more customers beyond word-of-mouth.
It allows sellers to showcase their products online and lets buyers easily discover, order, and review them — helping build visibility and trust.

🌟 Key Features
👩‍🍳 For Sellers

🧾 Create a seller account with contact and location details.

📸 Upload products with images, videos, prices, and descriptions.

📍 Add your exact city and village for nearby discovery.

🧮 View your orders, reviews, and customer feedback.

💰 Manage product availability and update status.

🛍️ For Buyers

🔍 Search for products by name, city, or village.

👀 View detailed product pages with seller information.

📦 Place orders for pickup or home delivery.

⭐ Leave reviews and star ratings.

🎁 Earn loyalty discounts through repeated purchases.

⚙️ For the System

🔐 Authentication for both buyers and sellers.

📊 Order and purchase tracking.

💎 Trust-building through buyer purchase history.

🖥️ Admin dashboard for data management.

🧱 Data Models Overview
🧩 Model	💬 Description
Person	Represents both buyers and sellers with role flags.
Address	Stores location details (county, city, village).
Product	Contains images, videos, price, description, and seller info.
Order	Tracks buyer orders, delivery method, and schedule.
Review	Holds buyer feedback and star ratings.
PurchaseHistory	Records total purchases and loyalty discounts.
🛠️ Tech Stack
Layer	Technology
Backend	Django (Python)
Database	SQLite / PostgreSQL / MySQL
Frontend	Django Templates / React (optional)
Media	Django Media storage for product images and videos
Authentication	Django built-in User model (extended as Person)
⚙️ Installation Guide
🧩 1️⃣ Clone the Repository
git clone https://github.com/yourusername/hercommerce.git
cd hercommerce

🌐 2️⃣ Create & Activate Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

📦 3️⃣ Install Dependencies
pip install -r requirements.txt

🧱 4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate

🔑 5️⃣ Create Superuser (Admin)
python manage.py createsuperuser

🚀 6️⃣ Run the Server
python manage.py runserver

🌍 Search and Discovery Strategy

✅ Add relevant keywords to product names and descriptions.
✅ Register the site on Google Search Console (free) for indexing.
✅ Add a Google My Business profile for local visibility.
✅ Allow product sharing via WhatsApp, Telegram, and Facebook.
✅ Enable city and village filters like:

“Butter in Bole” or “Honey in Bahir Dar”.