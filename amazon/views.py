from django.shortcuts import render


def home(request):
    sidebar_sect = [
        {
            "title": "Trending",
            "items": ["Bestsellers", "New Releases"],
        },
        {
            "title": "Digital Content & Devices",
            "items": [
                "Echo & Alexa",
                "Fire TV",
                "Kindle E-Readers & eBooks",
                "Audible Audiobooks",
                "Amazon Prime Video",
                "Amazon Music",
            ],
        },
        {
            "title": "Shop by Category",
            "items": [
                "Mobiles, Computers",
                "TV, Appliances, Electronics",
                "Men's Fashion",
                "Women's Fashion",
            ],
        },
        {
            "title": "Programs & Features",
            "items": [
                "Gift Cards & Mobile Recharges",
                "Amazon Launchpad",
                "Amazon Business",
                "Handloom and Handicrafts",
            ],
        },
        {
            "title": "Help & Settings",
            "items": ["Customer Service", "Your Account", "Sign Out"],
        },
    ]
    return render(request, "index.html", {"sidebar_sect": sidebar_sect})