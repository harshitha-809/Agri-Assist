# AgriAssist – Empowering Agriculture with Technology

AgriAssist is a web-based platform designed to support farmers by providing a digital marketplace for buying and selling agricultural products, accessing the latest news, discussing in forums, and getting assistance through an intelligent chatbot. It bridges the gap between farmers and modern technologies to enhance productivity and profitability in agriculture.

---

## Features

- 🛒 **Product Marketplace:** List and browse fresh produce, crops, vegetables, and fruits.
- 🗣️ **Community Forum:** A dedicated space where farmers can ask questions, share solutions, and interact with each other.
- 📢 **Agri-News Feed:** Stay updated with the latest agricultural trends and policies.
- 💬 **Farming Chatbot:** Integrated chatbot using Voc.ai to resolve farmers' queries.

---

## 🛠️ Tech Stack
_____________________________________________________
| Layer       | Technology Used                     |
|-------------|-------------------------------------|
| Frontend    | HTML, CSS, JavaScript               |
| Styling     | Tailwind CSS                        |
| Backend     | Django (Python Framework)           |
| Database    | PostgreSQL                          |
| Chatbot     | Voc.ai Chatbot Integration          |
_____________________________________________________

---

## 📷 Screenshots

### 🏠 Homepage
![Screenshot 2024-12-01 193224](https://github.com/user-attachments/assets/23b75e54-53b3-483c-8aeb-049658e62ba6)

### 🤖 ChatBot
![Screenshot 2025-07-01 131353](https://github.com/user-attachments/assets/381a21f9-82b2-4112-b979-b9c102e65565)

### 🛒 Products Page
![screencapture-127-0-0-1-8120-shop-2025-07-01-11_49_40](https://github.com/user-attachments/assets/087a8ec1-f649-485f-a044-bab88f6c81c3)

### ➕ Add Product
![Screenshot 2024-12-01 194746](https://github.com/user-attachments/assets/72c02c24-b7fb-438b-b2b9-b3f52016585e)

### 💬 Community Forum

![screencapture-127-0-0-1-8120-forum-2025-07-01-11_54_18](https://github.com/user-attachments/assets/37d9b72a-42f6-4e6b-b165-b9bf7073cfea)

### Market News, Updates & Blogs

![screencapture-127-0-0-1-8120-forum-blog-2025-07-01-11_55_47](https://github.com/user-attachments/assets/4b43c6a6-0590-4369-8712-2705fe70c340)

![screencapture-127-0-0-1-8120-forum-article-pest-prevention-2025-07-01-11_56_10](https://github.com/user-attachments/assets/8b4c420e-baca-4c4d-afe4-6e94875318ef)

## 📁 Project Structure

```
AgriAssist/
│
├── agriassist/          # Django project settings and configuration
├── shop/                # Product listing, browsing, and management
├── forum/               # Community discussions and threads
├── login/               # User registration and authentication
├── mediaroot/           # Chatbot integration (Voc.ai)
├── templates/           # Shared HTML templates
├── requirements.txt     # Python dependencies
└── manage.py            # Django management script
```
### Requirements
- python 3.11
- postgres server


### Steps to deployment
1. Create a virtual environment in AgriAssist directory\
   `python3 -m venv venv`
2. Install required dependencies (make sure venv is activated)\
   `pip install -r requirements.txt`
3. Install PostGres Server\
   [Link to Installer](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
4. Migrate Django models\
   `python manage.py migrate`
5. Run Django server\
   `python manage.py runserver`
- Create django super user to access/modify models data\
  `python manage.py createsuperuser`
6. Acess Application : Open your browser and go to http://127.0.0.1:8000


## ❌ No payment or transaction modules


## 🤝 Contributions
### We welcome contributions! Here's how you can help:

- Fork the repository

- Create your branch (git checkout -b feature-name)

- Commit your changes (git commit -m 'Add feature')

- Push to the branch (git push origin feature-name)

- Create a pull request


## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).


