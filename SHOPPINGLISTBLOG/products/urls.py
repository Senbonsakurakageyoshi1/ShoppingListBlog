from django.urls import path
from .views import ProductsListAPIVIEW,ProduitsRetrieveAPIVIEW,ProduitsRetrieveUpdateAPIVIEW,ProduitsDestroyAPIVIEW,ProduitsCreateAPIVIEW
from django.conf.urls.static import static
from django.conf import settings
urlpatterns=[path('api/produits/',ProductsListAPIVIEW.as_view(),name="products_list"),
             path('api/produits/<int:id>/',ProduitsRetrieveAPIVIEW.as_view(),name="products_detail"),
                       path('api/produits/create/',ProduitsCreateAPIVIEW.as_view(),name="products_create"),
             path('api/produits/update/<int:id>/',ProduitsRetrieveUpdateAPIVIEW.as_view(),name="products_update"),
             path('api/produits/delete/<int:id>/',ProduitsDestroyAPIVIEW.as_view(),name="products_delete")]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)