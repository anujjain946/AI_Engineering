from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from menus.models import MenuItem
from rbac.models import user_has_permission

class MeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "is_staff": request.user.is_staff,
            "is_admin_user": request.user.is_admin_user,
        })

class MenuAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = []
        for item in MenuItem.objects.filter(is_active=True, parent__isnull=True):
            if item.required_permission and not user_has_permission(request.user, item.required_permission):
                continue
            children = []
            for child in item.children.filter(is_active=True):
                if child.required_permission and not user_has_permission(request.user, child.required_permission):
                    continue
                children.append({
                    "name": child.name,
                    "code": child.code,
                    "url": child.url_name,
                    "icon": child.icon,
                })
            data.append({
                "name": item.name,
                "code": item.code,
                "url": item.url_name,
                "icon": item.icon,
                "children": children,
            })
        return Response(data)
