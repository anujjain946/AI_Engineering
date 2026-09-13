from .models import MenuItem
from rbac.models import user_has_permission

def dynamic_menu(request):
    if not request.user.is_authenticated:
        return {"dynamic_menu_items": []}

    items = list(MenuItem.objects.filter(is_active=True, parent__isnull=True))
    visible = []
    for item in items:
        if item.required_permission and not user_has_permission(
            request.user, item.required_permission
        ):
            continue
        children = []
        for child in item.children.filter(is_active=True):
            if child.required_permission and not user_has_permission(
                request.user, child.required_permission
            ):
                continue
            children.append(child)
        visible.append((item, children))
    return {"dynamic_menu_items": visible}
