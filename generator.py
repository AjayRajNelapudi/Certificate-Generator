import csv
import cv2 as cv

def make_certificates(certificate, names, class_sec):
    '''
    make_certificate(certificate, names, class_sec)
    :param certificate: certificate template
    :param names: list of names of students
    :param class_sec: class and section of the students repectively
    :return: None

    This function generates certifcates for all students names and class_sec based on the certifcate template
    '''
    for student in zip(names, class_sec):
        img = cv.imread(certificate, cv.IMREAD_COLOR)
        size = 2 if len(student[0]) < 16 else 1
        cv.putText(img, student[0], (508, 395), cv.FONT_HERSHEY_PLAIN, size, (0, 0, 0), 1, cv.LINE_AA)
        cv.putText(img, student[1], (265, 425), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1, cv.LINE_AA)
        cv.imwrite(student[0] + '.jpg', img)

def get_names_list(names_file):
    '''
    get_name_list(names_file):
    :param names_file: a csv file with the names in 2nd column and class_sec in 3rd column
    :return: names, class_sec

    This function retreives the names and class_sec from each of the record
    '''
    with open(names_file) as names:
        records = list(csv.reader(names))
        names = [record[1].capitalize() for record in records]
        class_sec = [record[2].upper() for record in records]
        return names, class_sec

def generate_certificates(certificate, names_file):
    '''
    generate_certficates(certificate, names_file)
    :param certificate: the certificate template
    :param names_file: csv files with names
    :return: None

    This is the exposed API which can be called to generate certificates
    '''
    names, class_sec = get_names_list(names_file)
    make_certificates(certificate, names,class_sec)