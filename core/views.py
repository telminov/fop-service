import subprocess
import shutil
import tempfile
from django.conf import settings
from django.http import HttpResponse
from rest_framework import views
from rest_framework.response import Response

from . import serializers

class Index(views.APIView):
    def get(self, request):
        return Response({'message': 'hello!'})

index = Index.as_view()


class GeneratePdf(views.APIView):
    def post(self, request):
        serializer = serializers.GeneratePdf(data=request.data)
        serializer.is_valid(raise_exception=True)

        filename = serializer.validated_data['filename']
        fo_string = serializer.validated_data['fo_data']

        fop_path = settings.FOP_PATH
        filename = str(filename)

        tmpdir = tempfile.mkdtemp()

        tmp_fo_path = tempfile.mktemp(dir=tmpdir, prefix=filename, suffix='.fo')
        tmp_fo = open(tmp_fo_path, mode='w')
        tmp_fo.write(fo_string)
        tmp_fo.close()

        tmp_pdf_path = tempfile.mktemp(dir=tmpdir, prefix=filename, suffix='.pdf')

        cmd = 'cd %s; ./fop -c conf/userconfig.xml -fo %s -pdf %s ' % (
            fop_path,
            tmp_fo_path,
            tmp_pdf_path
        )

        status, output = subprocess.getstatusoutput(cmd)
        if status:
            raise Exception(u'Generation pdf error:\n%s\n\n%s' % (cmd, output))

        tmp_pdf = open(tmp_pdf_path, "rb")
        pdf_content = tmp_pdf.read()
        tmp_pdf.close()

        shutil.rmtree(tmpdir)

        response = HttpResponse(pdf_content, content_type="application/pdf")
        response['Content-Disposition'] = 'filename=%s.pdf' % filename.encode('utf-8')

        return response
generate_pdf = GeneratePdf.as_view()
