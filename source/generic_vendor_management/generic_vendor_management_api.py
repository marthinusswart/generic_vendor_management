from flask_restful import Api
from generic_vendor_management.api_management import ApiManagement
from generic_vendor_management.vendor_management import Vendors, VendorManagement


def create_api(app):
    api = Api(app)
    api.add_resource(ApiManagement, '/api/v1')
    api.add_resource(Vendors, '/api/v1/<tenant_key>/vendors')
    api.add_resource(VendorManagement,
                     '/api/v1/<tenant_key>/vendors/<int:vendor_id>')
    return api
