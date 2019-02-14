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

    def extract_contestants_data(self, positions):
        contestants_file = open(self.contestants_filepath, "r")
        contestant_records = list(csv.reader(contestants_file))
        contestants_file.close()
        for record in contestant_records:
            phrase_position = []
            for attribute, position in zip(record, positions):
                phrase_position.append((attribute, position))
            self.phrase_position.append(phrase_position)

    def make_certificates(self):
        for participant_data in self.phrase_position:
            certificate = cv.imread(self.template_filepath, cv.IMREAD_COLOR)
            for phrase, position in participant_data:
                size = 2 #if len(phrase) < 16 else 1
                cv.putText(certificate, phrase, position, cv.FONT_HERSHEY_SCRIPT_SIMPLEX, size, (0, 0, 0), 1, cv.LINE_AA)
            certificate_filename = participant_data[0][0]
            self.certificates.append([certificate_filename, certificate])

    def save_all(self, target_dir):
        os.chdir(target_dir)
        with suppress(FileExistsError):
            os.mkdir('temp')
        os.chdir(target_dir + "/temp")

        for certificate_filename, certificate in self.certificates:
            cv.imwrite(certificate_filename + ".png", certificate)

        certificates = [certificate_filename for certificate_filename, certificate_img in self.certificates]

        os.chdir(target_dir)
        for filename in certificates:
            certificate_img = Image.open(target_dir + "/temp/" + filename + ".png")
            pdf_bytes = img2pdf.convert(certificate_img.filename)
            certificate_pdf = open(target_dir + "/" + filename + ".pdf", "wb")
            certificate_pdf.write(pdf_bytes)
            certificate_pdf.close()

        os.chdir(target_dir + "/temp")
        for file in certificates:
            os.remove(file + ".png")
        os.rmdir(target_dir + "/temp")


