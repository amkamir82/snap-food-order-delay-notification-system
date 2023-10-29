from rest_framework.response import Response
from rest_framework.views import APIView

from shop.exceptions import DelayReportException, AgentAssignException
from shop.serializers import DelayReportSerializer, AgentAssignSerializer
from shop.services import DelayReportService, AgentAssignService, DelaySummaryService


class DelayReportView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = DelayReportSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        service = DelayReportService()
        try:
            result = service.process(**validated_data)
        except DelayReportException as e:
            return Response(str(e), status=400)
        return Response(status=201, data=result)


class AgentAssignView(APIView):

    def get(self, request, *args, **kwargs):
        data = request.GET
        serializer = AgentAssignSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        service = AgentAssignService()
        try:
            result = service.process(**validated_data)
        except AgentAssignException as e:
            return Response(str(e), status=400)
        return Response(status=200, data=result)


class DelaySummaryView(APIView):

    def get(self, request, *args, **kwargs):
        service = DelaySummaryService()
        result = service.process()
        return Response(status=200, data=result)
