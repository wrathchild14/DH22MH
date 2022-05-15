from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

import PyPDF2 as pdf
import slate3k as slate
import os
import shutil


cvs = []
directory = "pdfs/"

@api_view(['POST'])
def pdf_recieve(request):
    if request.method == 'POST':
        print("SUCCESS!")

        f = request.data['file'].file
        f.seek(0)
        pdf = f.read()

        with open("pdfs/my_file.pdf", "wb") as binary_file:
            # Write bytes to file
            binary_file.write(pdf)

        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                with open(f, 'rb') as f:
                    extracted_text = slate.PDF(f)
                    t = extracted_text[0]
                    t2 = t.replace("\n", " ")
                    t2 = t2.replace("–", "-")
                    cvs.append(t2)

        d = {"test": 5}
        response = json.dumps(d)
        return Response(response, status=status.HTTP_200_OK)

@api_view(['GET', 'POST', ])
def delete_pdfs(request):
    if request.method == 'GET':
        shutil.rmtree('pdfs')
        os.mkdir('pdfs')

        return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_seniority(request):
    if request.method == 'GET':
        rez = seniority(cvs[0])

        d = {"seniority": rez}
        response = json.dumps(d)
        return Response(response)

@api_view(['GET'])
def get_name(request):
    if request.method == 'GET':
        rez = name(cvs[0])

        d = {"name": rez}
        response = json.dumps(d)
        return Response(response)

@api_view(['GET'])
def get_email(request):
    if request.method == 'GET':
        rez = email(cvs[0])

        d = {"email": rez}
        response = json.dumps(d)
        return Response(response)

@api_view(['GET'])
def get_faculty(request):
    if request.method == 'GET':
        rez = faculty(cvs[0])

        d = {"faculty": rez}
        response = json.dumps(d)
        return Response(response)

@api_view(['GET'])
def get_address(request):
    if request.method == 'GET':
        rez = address(cvs[0])
        print(rez)

        d = {"address": rez}
        response = json.dumps(d)
        return Response(response)

@api_view(['GET'])
def get_pr_lang(request):
    if request.method == 'GET':
        rez = pr_lang(cvs[0])

        d = {"pr_lang": rez}
        response = json.dumps(d)
        return Response(response)

@api_view(['GET'])
def get_info(request):
    if request.method == 'GET':
        d = {
            'seniority': seniority(cvs[0]),
            'name': name(cvs[0]),
            'email': email(cvs[0]),
            'faculty': faculty(cvs[0]),
            'address': address(cvs[0]),
            'pr_lang': pr_lang(cvs[0])
        }

    response = json.dumps(d)
    return Response(response)


# ---------------------------------- Helping functions ---------------------------------- #
def godine_rada(date):
    date1, date2 = date.split("-")
    godina1 = date1.split("/")[1]
    godina2 = date2.split("/")[1]
    god = abs(int(godina1.strip()[-2:]) - int(godina2.strip()[-2:]))
    return god

def seniority(cv):
    first_work = cv.split("  ")[7]
    second_work = cv.split("  ")[18]
    all_years = godine_rada(first_work) + godine_rada(second_work)
    if (all_years < 3):
        return "Junior"
    elif (3 < all_years < 6):
        return "Mid"
    else:
        return "Senior"

def name(cv):
    return cv.split("  ")[0]

def email(cv):
    a, mail = cv.split("  ")[3].strip().split(" ")
    return mail

def faculty(cv):
    return cv.split("  ")[37] + " " + cv.split("  ")[38]

def address(cv):
    return cv.split("  ")[1].split(":")[1].strip()

def pr_lang(cv):
    l = cv.split("  ")[45].split(",")
    return [i.strip() for i in l]

