import os
from jinja2 import Environment, FileSystemLoader


def main():
    files = ("index.html", "about.html", "contact.html", "form.html",
             "photos.html", "resume.html", "press.html", "audiovideo.html")
    loader = FileSystemLoader(os.path.join(os.getcwd(), "templates"))
    env = Environment(loader=loader)

    for fname in files:
        with open(fname, "w") as f:
            if fname == "index.html":
                g = env.get_template(fname).generate(indexactive=True)
            elif fname == "about.html":
                g = env.get_template(fname).generate(aboutactive=True)
            elif fname == "contact.html":
                g = env.get_template(fname).generate(contactactive=True)
            elif fname == "photos.html":
                g = env.get_template(fname).generate(photosactive=True)
            elif fname == "resume.html":
                g = env.get_template(fname).generate(resumeactive=True)
            elif fname == "press.html":
                g = env.get_template(fname).generate(pressactive=True)
            elif fname == "audiovideo.html":
                g = env.get_template(fname).generate(avactive=True)

            for line in g:
                f.write(line)

if __name__ == "__main__":
    main()
