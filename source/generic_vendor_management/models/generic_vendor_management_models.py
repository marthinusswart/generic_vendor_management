from generic_vendor_management import db


class Vendor(db.Model):
    __tablename__ = 'generic_vendor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    external_ref = db.Column(db.String(150))
    tenant_key = db.Column(db.String(150))

    def as_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'external_ref': self.external_ref,
            'tenant_key': self.tenant_key
        }
