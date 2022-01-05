from django.contrib import admin
from app.models import Expense,TaskModel,ProfileModel,UserLogin,UserCreation,GroupName
# Register your models here.

@admin.register(GroupName)
class GroupNameAdmin(admin.ModelAdmin):
    list_display=['gname','groupname']

@admin.register(UserLogin)
class UserLoginAdmin(admin.ModelAdmin):
    list_display=['ulname','ulpassword']

@admin.register(UserCreation)
class UserCreationAdmin(admin.ModelAdmin):
    list_display=['uname','upw']

@admin.register(Expense)
class ExpenseModelAdmin(admin.ModelAdmin):
    list_display=['user_id','user','itemname','price','quantity','date']

@admin.register(TaskModel)
class TaskModelAdmin(admin.ModelAdmin):
    list_display=['user_id','user','name','start','end','note']

@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display=['user','user_id','img','desc','occupation','martial']