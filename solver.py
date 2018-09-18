import os
import time
import crayons
import wikipedia
import nltk
import pytesseract

from PIL import Image, ImageEnhance

"""
Note: I hacked this all together very quickly and I don't think it represents my best code at all
"""

SCREEN_DIR = "" # Mine was "/Users/davidhariri/Desktop"
IDENTIFIER = "Screen Shot"
CROP_AREA = (78, 208, 986, 1161) # Mine was "/Users/davidhariri/Desktop"
DEBUG = False


def process_image(img):
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(3)

    sharper = ImageEnhance.Sharpness(img)
    img = sharper.enhance(1)

    brighter = ImageEnhance.Brightness(img)
    img = brighter.enhance(1)

    img = img.convert("L")

    # Crop for question
    img = img.crop((135, 280, 880, 1040))
    
    # Check work with...
    # img.show()

    return img


stop = set(nltk.corpus.stopwords.words("english"))

while True:
    screen_shots = list(filter(
        lambda p: IDENTIFIER in p, os.listdir(SCREEN_DIR)))

    if len(screen_shots) == 0:
        print(crayons.yellow("No screen shot found"))
    else:
        # Pause while loop while processing image
        file_path = os.path.join(SCREEN_DIR, screen_shots[0])

        # Open screen shot
        screen = process_image(Image.open(file_path))
        screen.save(SCREEN_DIR + "/test.png")

        # Get tesseract result from filtered screen
        # TODO: Round font training
        result = pytesseract.image_to_string(
            screen, config="load_system_dawg=0 load_freq_dawg=0")

        # Split up newlines until we have our question and answers
        parts = result.split("\n\n")

        question = parts.pop(0).replace("\n", " ")
        q_terms = question.split(" ")
        q_terms = list(filter(lambda t: t not in stop, q_terms))
        q_terms = set(q_terms)

        parts = "\n".join(parts)
        parts = parts.split("\n")

        answers = list(filter(lambda p: len(p) > 0, parts))

        # question = "In Mexico, a saladito is always known as what?"
        # answers = ["Taco salad", "Salted plum", "Guava roll"]

        

        print("\n\n{}\n\n{}\n\n".format(
            crayons.blue(question),
            crayons.blue(", ".join(answers))
        ))

        answer_results = {}

        for answer in answers:
            records = wikipedia.search(answer)
            r = records[0] if len(records) else None

            if r is not None:
                p = wikipedia.page(r)
                answer_results[answer] = {
                    "content": p.content,
                    "words": p.content.split(" ")
                }

        for a in answer_results:
            term_count = 0

            for t in q_terms:
                term_count += answer_results[a]["words"].count(t)

            tc = term_count / len(answer_results[a]["words"])
            tcp = round(tc * 10000, 2)

            answer_results[a]["score"] = tcp

        max_a = 0
        max_a_key = None

        # Maximize
        for a in answer_results:
            if answer_results[a]["score"] > max_a:
                max_a_key = a
                max_a = max(answer_results[a]["score"], max_a)

        print(crayons.green(max_a_key))

        input("Continue?")

        if not DEBUG:
            os.rename(file_path, file_path.replace("Screen Shot", "Done"))

    time.sleep(0.1)
    os.system("clear")
