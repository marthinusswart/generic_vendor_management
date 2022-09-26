from flask import request, jsonify
from flask_restful import Resource


class Vendors(Resource):
    def get(self, tenant_key):
        from .models.generic_vendor_management_models import Vendor
        vendors = Vendor.query.filter_by(tenant_key=tenant_key)
        result = [a.as_json() for a in vendors]
        print(tenant_key)
        return jsonify(result)

    def post(self, tenant_key):
        from . import db
        from .models.generic_vendor_management_models import Vendor

        new_vendor_json = request.get_json()

        vendor = Vendor.query.filter_by(
            external_ref=new_vendor_json['external_ref'], tenant_key=tenant_key).first()
        if vendor:
            return {'result': 'Vendor already exists', 'JSON received': new_vendor_json}, 409
        else:
            new_vendor = Vendor()
            new_vendor.external_ref = new_vendor_json['external_ref']
            new_vendor.name = new_vendor_json['name']
            new_vendor.tenant_key = tenant_key
            db.session.add(new_vendor)
            db.session.commit()
            return {'result': 'Vendor created', 'JSON received': new_vendor_json}


class VendorManagement(Resource):
    def get(self, tenant_key, vendor_id):
        from .models.generic_vendor_management_models import Vendor
        vendor = Vendor.query.filter_by(
            tenant_key=tenant_key, id=vendor_id).first()

        if not vendor:
            return {'result': 'No vendor by that id', 'Id received': vendor_id}, 404

        return jsonify(vendor.as_json())

    def put(self, tenant_key, vendor_id):
        from . import db
        from .models.generic_vendor_management_models import Vendor
        vendor = Vendor.query.filter_by(
            tenant_key=tenant_key, id=vendor_id).first()

        if not vendor:
            return {'result': 'No vendor by that id', 'Id received': vendor_id}, 404

        account_json = request.get_json()
        vendor.name = account_json['name']

        db.session.commit()
        return {'result': 'Vendor', 'JSON received': account_json}

    def delete(self, tenant_key, vendor_id):
        from . import db
        from .models.generic_vendor_management_models import Vendor
        vendor = Vendor.query.filter_by(
            tenant_key=tenant_key, id=vendor_id).first()

        if not vendor:
            return {'result': 'No vendor by that id', 'Id received': vendor_id}, 404

        db.session.delete(vendor)
        db.session.commit()
        return {'result': 'Vendor deleted', 'Id received': vendor_id}
