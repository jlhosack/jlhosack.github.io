import os
from jinja2 import Environment, FileSystemLoader


def main():
    files = ("index.html", "about.html", "contact.html", "form.html",
             "photos.html", "resume.html", "press.html", "audiovideo.html")
    env = Environment(
        loader=FileSystemLoader(os.path.join(os.getcwd(), "templates")))

    for fname in files:
        with open(fname, "w") as f:
            for line in env.get_template(fname).generate(
                    active=fname.replace(".html", "")):
                f.write(line)

if __name__ == "__main__":
    main()
