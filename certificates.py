import csv
import cv2 as cv
import os
import img2pdf
from PIL import Image
from contextlib import suppress
import shutil
import logging

class CertificateGenerator:
    def __init__(self, template_filepath, contestants_filepath):
        self.contestants_filepath = contestants_filepath
        self.template_filepath = template_filepath
        self.certificates = []
        self.phrase_position = []
        self.logger = logging.getLogger("certificates")

    def set_data_positions(self, positions):
        with open(self.contestants_filepath, "r") as contestants_file:
            contestant_records = list(csv.reader(contestants_file))

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
            try:
                certificate = cv.imread(self.template_filepath, cv.IMREAD_COLOR)
                first_column = True
                for phrase, position in participant_data:
                    size = 2 if len(phrase) <= 16 else 1
                    if first_column:
                        processed_phrase = self.capitalize(phrase)
                        first_column = False
                    else:
                        processed_phrase = phrase
                        size = 1
                    cv.putText(certificate, processed_phrase, position, cv.FONT_HERSHEY_COMPLEX, size, (0, 0, 0), 1, cv.LINE_AA)
                certificate_filename = participant_data[0][0]
                self.certificates.append([certificate_filename, certificate])

                self.logger.info(certificate_filename + "'s certificate created successfullly")
            except Exception as exp:
                self.logger.info(participant_data[0][0] + "'s certificate creation failed due to " + str(exp))

    def prepare_dirs(self, target_dir):
        os.chdir(target_dir)
        with suppress(FileExistsError):
            os.mkdir('temp')
        os.chdir(os.path.join(target_dir, "temp"))

    def save_as_images(self):
        for certificate_filename, certificate in self.certificates:
            cv.imwrite(certificate_filename + ".png", certificate)

    def convert_to_pdfs(self, target_dir):
        certificates = [certificate_filename for certificate_filename, certificate_img in self.certificates]

        os.chdir(target_dir)
        for filename in certificates:
            try:
                certificate_img = Image.open(os.path.join(os.path.join("temp", filename + ".png")))
                pdf_bytes = img2pdf.convert(certificate_img.filename)
                with open(os.path.join(target_dir, filename + ".pdf"), "wb") as certificate_pdf:
                    certificate_pdf.write(pdf_bytes)

                self.logger.info(filename + ".png converted to pdf")
            except Exception as exp:
                self.logger.info(filename + ".png conversion to pdf failed due to " + str(exp))

    def clean_dir(self, target_dir):
        temp_dir = os.path.join(target_dir, "temp")
        shutil.rmtree(temp_dir)

    def save_all(self, target_dir):
        self.prepare_dirs(target_dir)
        self.save_as_images()
        self.convert_to_pdfs(target_dir)
        self.clean_dir(target_dir)


