from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class HomeworkMockCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        # Проверяем права доступа
        if not request.user.has_perm(
            "users.can_add_homework"
        ):  # Предположим, что для модели User есть разрешение "can_add_homework" (например, для группы "Учитель")
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Создаем фиктивное домашнее задание
        homework = {"id": 1, "title": "Домашнее задание по теме: Таблица умножения"}
        return Response(homework, status=status.HTTP_201_CREATED)


class HomeworkMockUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, homework_id):

        # Проверяем права доступа
        if not request.user.has_perm(
            "users.can_update_homework"
        ):  # Предположим, что для модели User есть разрешение "can_update_homework" (например, для группы "Учитель")
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Получаем обновленное домашнее задание
        updated_homework = {
            "id": homework_id,
            "title": request.data.get(
                "title", "Домашнее задание по теме: Таблица умножения"
            ),  # Задаем дефолтное значения для ситуации, когда это поле отсутствует в запросе
        }
        return Response(updated_homework, status=status.HTTP_200_OK)


class HomeworkMockRetrieveAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, homework_id):

        # Проверяем права доступа
        if not request.user.has_perm("users.can_view_homework"):
            # Предположим, что для User есть разрешение "can_view_homework" (например, для групп "Учитель" и "Ученик")
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Получаем конкретное домашнее задание
        homework = {
            "id": homework_id,
            "title": "Домашнее задание по теме: Таблица умножения",
        }
        return Response(homework, status=status.HTTP_200_OK)


class HomeworkMockDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, homework_id):

        # Проверяем права доступа
        if not request.user.has_perm(
            "users.can_delete_homework"
        ):  # Предположим, что для модели User есть разрешение "can_delete_homework" (например, для групп "Учитель")
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
