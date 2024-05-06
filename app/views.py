import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book, FileSave
import io
import os
import time


class ExportBookData(APIView):
    def post(self, request):
        try:
            books = Book.objects.all()
            df = pd.DataFrame.from_records(books.values())

            excel_buffer = io.BytesIO()
            df.to_excel(excel_buffer, index=False)

            excel_buffer.seek(0)

            export_folder = os.path.join(os.getcwd(), "Exports")
            if not os.path.exists(export_folder):
                os.makedirs(export_folder)
            timestamp = str(int(time.time()))
            file_name = f'BookExport_{timestamp}.xlsx'
            file_path = os.path.join(export_folder, file_name)

            with open(file_path, 'wb') as f:
                f.write(excel_buffer.getvalue())

            file_model_instance = FileSave.objects.create(file=file_path)
            excel_buffer.close()

            return Response({
                'status': True,
                'message': 'Export Successfully'
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'status': False,
                'message': 'Export Fail: {}'.format(str(e))
            }, status=status.HTTP_400_BAD_REQUEST)
