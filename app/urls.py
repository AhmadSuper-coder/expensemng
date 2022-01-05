from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('',views.Login,name="login"),
    path('signup/',views.Signup, name='signup'),
    path('dashboard/',views.Dashboard,name="dashboard"),
    path('profile/',views.Profile,name="profile"),
    path('expense/',views.Expenses,name="expense"),
    path('task/',views.Task, name="task"),
    path('changepassword/',views.ChangePassword,name="changepassword"),
    path('logout/',views.Logout, name='logout'),
    path('delete/<int:id>/',views.DeleteItem,name="deleteitem"),
    path('edit/<int:id>/',views.EditItem,name='edit'),
    path('edittask/<int:id>/',views.EditTask,name='edittask'),
    path('deletetask/<int:id>/',views.DeleteTask,name='deletetask'),
    path('editpro/<int:id>/',views.EditProfileUser,name="editkalua"),
    path('makeprofile/',views.MakeProfile,name='makeprofile'),
    path('viewexpense/',views.ViewExpense,name="viewexpense"),
    path('viewtotal/',views.ViewTotal,name="viewtotal")

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)