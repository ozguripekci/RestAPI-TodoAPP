from django.urls import path
#! Function based urls
# from .views import home, hello_world, todoList, todoCreate, todoListCreate, todoUpdate, todoDelete
#! Class based urls
from .views import home, TodoList, TodoDetail

urlpatterns = [
    path('', home),

    #! Function based views
    #path('hello/', hello_world),
    #path('todoList/', todoList),
    #path('todoCreate/', todoCreate),
    #path('todoListCreate/', todoListCreate),
    #path('todoUpdate/<int:pk>/', todoUpdate),
    #path('todoDelete/<int:pk>/', todoDelete),

    #! Class based views
    path('list/', TodoList.as_view()),
    path('detail/<int:id>/', TodoDetail.as_view()),
]
