from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Ticket
from .serializers import TicketSerializer

class TicketViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def get_queryset(self):
        if self.request.user.is_staff:
            return Ticket.objects.all()
        return Ticket.objects.filter(created_by=self.request.user)
    
    

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        ticket = self.get_object()
        if not self.request.user.is_staff and ticket.status != 'open':
            raise PermissionError("You can only update tickets with status 'open'")
        serializer.save()
    
    def perform_destroy(self, instance):
        if not self.request.user.is_staff:   # Only admin can delete
            raise PermissionDenied("Only admin can delete tickets") # pyright: ignore[reportUndefinedVariable]
        instance.delete()

    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAdminUser])
    def status(self, request, pk=None):
        ticket = self.get_object()
        new_status = request.data.get('status')
        if new_status not in ['open', 'in_progress', 'closed']:
            return Response({'error': 'Invalid status'}, status=400)
        ticket.status = new_status
        ticket.save()
        return Response(TicketSerializer(ticket).data)
