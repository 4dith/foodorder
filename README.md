# Online Food Ordering System

## 👥 Team Members
* **Adithya Venkatesh** (423102)
* **R Neti** (423173)
* **Aaryan Shyam Pillai** (423102)

## 📖 About the Project
This project is a scalable, multi-sided marketplace designed to connect Customers, Restaurant Partners, and Delivery Riders. The system facilitates menu browsing, secure order placement, payment processing, and real-time delivery tracking.

## 🚀 Tech Stack
* **Frontend:** React.js
* **Backend:** Python (Django)
* **Database:** MongoDB (Menus/Catalogs) & PostgreSQL (Orders/Payments/Users)
* **Caching & Real-Time:** Redis & WebSockets

## ✨ Core Features

### 🔐 User Management & Authentication
* Role-based access for Customers, Partners, and Riders.
* Secure login via email/password.

### 🍔 Catalog & Search
* Location-based restaurant discovery and proximity filtering.
* Advanced search filters (cuisine type, ratings, dietary preferences).
* Real-time CRUD operations for restaurant partners to manage menus and item availability.

### 🛒 Order Processing
* Dynamic shopping cart with real-time calculation of totals, taxes, and delivery fees.
* Unique Order ID generation.
* Operational dashboard for partners to accept/reject pending orders.

### 💳 Payments
* Secure third-party payment gateway integration for credit cards and UPI.
* Escrow fund holding with automated weekly disbursements.

### 📍 Real-Time Logistics
* Automated broadcast of "Ready for Delivery" orders to nearby riders.
* Live GPS tracking of riders streamed via WebSockets to the customer interface.
* Automated order status updates (e.g., "Delivered" upon rider confirmation).

