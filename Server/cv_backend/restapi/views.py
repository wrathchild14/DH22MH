from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

import PyPDF2 as pdf
import slate3k as slate
import os


@api_view(['GET', 'POST', ])
def test(request):
    if request.method == 'GET':
        print("Test")

        d = {"test": 5}

        response = json.dumps(d)
        return Response(response)


@api_view(['POST'])
def pdf_recieve(request):
    if request.method == 'POST':
        print("SUCCESS!")

        f = request.data['file'].file
        f.seek(0)
        pdf = f.read()
        #print(pdf)

        with open("pdfs/my_file.pdf", "wb") as binary_file:
            # Write bytes to file
            binary_file.write(pdf)

        cvs = []
        directory = "pdfs/"

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

        print(cvs[0])

        # extracted_text = slate.PDF(pdf)
        # t = extracted_text[0]
        # print(t)
        # with open(f, 'rb') as fopen:
        #     q = fopen.read()
        #     print(q.decode())

        # with open(f.read().decode(), 'rb') as f:
            
        #     extracted_text = slate.PDF(f)
        #     print(extracted_text)
        # extracted_text = slate.PDF(f)
        # t = extracted_text[0]
        # t2 = t.replace("\n", " ")
        # t2 = t2.replace("–", "-")
        # print(extracted_text)

        d = {"test": 5}

        response = json.dumps(d)
        return Response(response, status=status.HTTP_200_OK)
