import uuid
def get_products():
    fake_response = [{
        "sku": uuid.uuid4(),
        "title": "Chocolate icecream",
        "long_descripcion" : " blalalslalslasllaslalsllaslalsllalslalslalslalslalslalslalslallslalsllalslalslalslalslalslalslalsldlasdalskdakfkfadsnvnJNDVJNSDJVNsdvnSJNDkksmKDSLKNVLAMKSDLKNVALSNDVLÑASNKD ÑVLsnd ñvlkn´LKADNVÑLksndñvsjljndñvLSNDÑVLKns´dvkln´SÑDLKVN,solkdnv´SKNDV",
        "price_euro" : 1.5 }]
    return fake_response

def create_product(sku,title,long_descripcion,price_euro):
    ''' esto iria en una base de datos'''
    print(f"crear sku={sku} y title={title}")
