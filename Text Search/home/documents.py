from django_elasticsearch_dsl import Document,fields
from django_elasticsearch_dsl.registries import registry
from .models import Product

@registry.register_document
class ProdcuctDocument(Document):
    class Index:
        name = "products"
        settings = {
            'number_of_shards' : 1,
            'number_of_replicas' : 0
        }
    class Django:
        model = Product
        fields = [
            "title",
            "description",
            "category",
            "price",
            "brand",
            "sku",
            "thumbnail"
        ]
