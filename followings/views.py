from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import FollowingSerializer
from .models import Following
from rest_framework.generics import CreateAPIView
from django.core.mail import send_mail
from django.conf import settings
from books.models import Book


class FollowingView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Following.objects.all()
    serializer_class = FollowingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        id = serializer.data["book"]
        book = get_object_or_404(Book, id=id)
        name_user = self.request.user.first_name
        title = book.title
        copies = book.copies_quantity

        msg_not_available = (
            f"Olá, {name_user}! \n"
            f"No momento não temos cópias do livro {title} disponível\n"
            "Manteremos informado quando houver disponibilidade da cópia."
        )

        msg_available = (
            f"Olá, {name_user}! \n"
            f"Notamos seu interesse no livro {title}. Que tal fazer uma reserva?\n"
            f"Temos {copies} {'cópia' if copies > 0 and  copies == 1 else 'cópias'} do livro."
        )

        send_mail(
            subject="BiblioteKA",
            message=f"{msg_available if copies > 0 else msg_not_available}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.request.user.email],
            fail_silently=False,
        )
