from flask import Flask, render_template

app = Flask(__name__)

INFO = {
    "name": "Codreanu Rareș",
    "role": "Graphic Designer & Illustrator",
    "tagline": "Design cu impact, construit cu intenție.",
    "description": (
        "Sunt un artist pasionat de ilustrație și graphic design. "
        "Lucrez cu Adobe Photoshop, Illustrator, Lightroom, Clip Studio și Procreate. "
        "Îmi place să creez afișe, cover art, ilustrații și design digital cu impact vizual."
    ),
    "email": "justash814@gmail.com",
    "phone": "+40 762 212 113",
    "instagram": "@ash_4_art",
    "location": "Sfântu Gheorghe, România",
    "linkedin": "https://www.linkedin.com/in/codreanu-rares-52ba4a314/"
}

TOOLS = [
    {"name": "Photoshop",   "image": "photoshop.png"},
    {"name": "Illustrator", "image": "illustrator.png"},
    {"name": "Lightroom",   "image": "lightroom.png"},
    {"name": "Premiere",    "image": "premiere.png"},
    {"name": "Clip Studio", "image": "clipstudio.png"},
    {"name": "Procreate",   "image": "procreate.png"},
    {"name": "Canva",       "image": "canva.png"},
]

EDUCATION = [
    {"years": "2015 – 2019", "place": "Plugor Sándor Art School"},
    {"years": "2021 – 2024", "place": "Transilvania University – Communication & PR"},
]

EXPERIENCE = [
    {
        "role": "Operator Date – Smile Center",
        "period": "2025 – 2026",
        "details": "Proiectare lucrări dentare digitale în Exocad și Blender."
    },
    {
        "role": "Content Moderator – Teleperformance",
        "period": "2025",
        "details": "Moderare conținut online, analiză vizuală și respectarea ghidurilor."
    },
    {
        "role": "Ofițer Suport Clienți – Raiffeisen Bank",
        "period": "2022 – 2024",
        "details": "Relații clienți, comunicare și gestionare solicitări."
    },
]

ARTWORKS = [
    {"title": "Artwork 1", "image": "proiect1.jpeg"},
    {"title": "Artwork 2", "image": "proiect2.jpeg"},
    {"title": "Artwork 3", "image": "proiect3.jpeg"},
    {"title": "Artwork 4", "image": "proiect4.jpeg"},
    {"title": "Artwork 5", "image": "proiect5.jpeg"},
    {"title": "Artwork 6", "image": "proiect6.jpeg"},
    {"title": "Artwork 7", "image": "proiect7.jpeg"},
]

@app.route("/")
def home():
    return render_template(
        "home.html",
        info=INFO,
        tools=TOOLS,
        education=EDUCATION,
        experience=EXPERIENCE,
        artworks=ARTWORKS
    )

@app.route("/about")
def about():
    return render_template("about.html", info=INFO)

@app.route("/contact")
def contact():
    return render_template("contact.html", info=INFO)

@app.route("/projects")
def projects():
    return render_template("projects.html", artworks=ARTWORKS)

if __name__ == "__main__":
    app.run(debug=True)
