from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializer import CookiesLocationSerializer
from .permissions import IsOwnerOrReadOnly
from locations.models import DailyCookies


class CookiesLocationListView(ListCreateAPIView):
    serializer_class = CookiesLocationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return DailyCookies.objects.filter(user=user)


class CookiesLocationDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # queryset = DailyCookies.objects.all()
    serializer_class = CookiesLocationSerializer

    def get_queryset(self):
        user = self.request.user
        return DailyCookies.objects.filter(user=user)