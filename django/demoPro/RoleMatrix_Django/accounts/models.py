from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class Role(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    is_active=models.BooleanField(default=True)
    def __str__(self): return self.name

class Permission(models.Model):
    code=models.CharField(max_length=100, unique=True)
    name=models.CharField(max_length=150)
    def __str__(self): return self.name

class RolePermission(models.Model):
    role=models.ForeignKey(Role,on_delete=models.CASCADE,related_name="role_permissions")
    permission=models.ForeignKey(Permission,on_delete=models.CASCADE,related_name="permission_roles")
    class Meta: unique_together=("role","permission")

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,role=None,**extra):
        if not email: raise ValueError("Email is required")
        user=self.model(email=self.normalize_email(email),role=role,**extra)
        user.set_password(password); user.save(using=self._db); return user
    def create_superuser(self,email,password=None,**extra):
        user=self.create_user(email,password,**extra)
        user.is_staff=True; user.is_superuser=True; user.is_active=True
        user.save(using=self._db); return user

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(unique=True)
    name=models.CharField(max_length=150,blank=True)
    role=models.ForeignKey(Role,null=True,blank=True,on_delete=models.SET_NULL)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD="email"
    objects=UserManager()
    def __str__(self): return f"{self.email} ({self.role})"

    def has_role_permission(self, code):
        if self.is_superuser: return True
        return bool(self.role and self.role.role_permissions.filter(permission__code=code).exists())
