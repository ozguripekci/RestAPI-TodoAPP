from django.urls import path, include
#! Function based urls
# from .views import home, hello_world, todoList, todoCreate, todoListCreate, todoUpdate, todoDelete
#! Class based urls
#from .views import home, TodoList, TodoDetail
#! Generic Views
#from .views import home, TodoList
#! Concrete Views
#from .views import home, TodoListCreate, TodoGetUpdateDelete, TodoMVS

#!MVSet
from .views import home, TodoMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', TodoMVS)

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
    #path('list/', TodoList.as_view()),
    #path('detail/<int:id>/', TodoDetail.as_view()),
    #! Concrete Views
    #path('list/', TodoListCreate.as_view()),
    #path('detail/<int:id>/', TodoGetUpdateDelete.as_view()),

    #!MVSet
    #path('', include(router.urls)),

]

urlpatterns += router.urls
