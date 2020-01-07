import csv
import cv2 as cv
import os
import img2pdf
from PIL import Image
from contextlib import suppress

class Certificate_Generator:
    def __init__(self, template_filepath, contestants_filepath):
        '''
        :param phrase_pos: [[(phraseA, (X, Y)), (phraseB, (X, Y)), (phraseC, (X, Y))], ...]
        :param template_path: path of the template certificate
        '''
        self.contestants_filepath = contestants_filepath
        self.template_filepath = template_filepath
        self.certificates = []
        self.phrase_position = []

    def set_data_positions(self, positions):
        contestants_file = open(self.contestants_filepath, "r")
        contestant_records = list(csv.reader(contestants_file))
        contestants_file.close()
        for record in contestant_records:
            phrase_position = [(attribute, self.center_align_attribute_poistion(attribute, position)) for attribute, position in zip(record, positions)]
            self.phrase_position.append(phrase_position)

    def center_align_attribute_poistion(self, word, position):
        uppercase_pixels = 22
        lowercase_pixels = 19
        space_pixels = 16
        half_word = word[0:len(word)//2]

        uppercase_count = sum(map(str.isupper, half_word))
        space_count = sum(map(str.isspace, half_word))
        lowercase_count = sum(map(str.islower, half_word))

        offset = uppercase_count * uppercase_pixels + lowercase_count * lowercase_pixels + space_count * space_pixels

        new_position = (position[0] - offset, position[1])
        return new_position

    def capitalize(self, phrase):
        name = phrase.split()
        name = [part.capitalize() for part in name]
        return ' '.join(name)

    def make_certificates(self):
        for participant_data in self.phrase_position:
            certificate = cv.imread(self.template_filepath, cv.IMREAD_COLOR)
            first_column = True
            for phrase, position in participant_data:
                size = 2 if len(phrase) <= 16 else 1
                if first_column:
                    capital_phrase = self.capitalize(phrase)
                    first_column = False
                else:
                    capital_phrase = phrase
                    size = 1
                cv.putText(certificate, capital_phrase, position, cv.FONT_HERSHEY_COMPLEX, size, (0, 0, 0), 1, cv.LINE_AA)
            certificate_filename = participant_data[0][0]
            self.certificates.append([certificate_filename, certificate])

    def save_all(self, target_dir):
        os.chdir(target_dir)
        with suppress(FileExistsError):
            os.mkdir('temp')
        os.chdir(os.path.join(target_dir, "temp"))

        for certificate_filename, certificate in self.certificates:
            cv.imwrite(certificate_filename + ".png", certificate)

        certificates = [certificate_filename for certificate_filename, certificate_img in self.certificates]

        os.chdir(target_dir)
        for filename in certificates:
            certificate_img = Image.open(os.path.join(target_dir, os.path.join("temp", filename + ".png")))
            pdf_bytes = img2pdf.convert(certificate_img.filename)
            certificate_pdf = open(os.path.join(target_dir, filename + ".pdf"), "wb")
            certificate_pdf.write(pdf_bytes)
            certificate_pdf.close()

        temp_dir = os.path.join(target_dir, "temp")
        os.chdir(temp_dir)
        for file in certificates:
            os.remove(file + ".png")
        os.rmdir(temp_dir)


