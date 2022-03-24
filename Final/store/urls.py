from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_all, name='product_all'),
    path('<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('payment/', views.UserPayment, name='payment'),
    

    path('adminstore/', views.AdminStore,name="adminstore"),
    
    path('adminstore/admincategories/',views.CategoryListView,name="categoryList"), 
    path('adminstore/admincategories/create',views.CategoryView.as_view(),name="categoryCreate"),  
    path('adminstore/admincategorie/<int:idp>/delete', views.CategoryDeleteView.as_view(),name="categoryDelete"),
    path('adminstore/admincategorie/<int:idp>/update/',views.CategoryUpdateView.as_view(),name="categoryUpdate"),
    
    path('adminstore/adminproducts/',views.ProductListView,name="productList"),
    path('adminstore/adminproducts/create',views.ProductView.as_view(),name="productCreate"), 
    path('adminstore/adminproducts/<int:idp>/delete', views.ProductDeleteView.as_view(),name="productDelete"),
    path('adminstore/adminproducts/<int:idp>/update/',views.ProductUpdateView.as_view(),name="productUpdate"), 
    path('adminstore/adminproducts/<int:idp>/details', views.ProductDetailsView.as_view(),name="productDetails"),
]

