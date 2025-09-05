from tortoise import fields
from tortoise.models import Model


class Doctor(Model):
    id = fields.UUIDField(pk=True)

    # Core scraped fields
    full_names = fields.CharField(max_length=255, null=True)
    name = fields.CharField(
        max_length=255, null=True
    )  # sometimes redundant with full_names
    registration_number = fields.CharField(max_length=100, null=True)
    license_no = fields.CharField(max_length=100, unique=True, db_index=True)
    license_type = fields.CharField(max_length=100, null=True, db_index=True)
    practice_type = fields.CharField(max_length=150, null=True, db_index=True)
    qualifications = fields.TextField(null=True)

    # Address & contact
    address = fields.TextField(null=True)
    postal_address = fields.TextField(null=True)
    email = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=50, null=True)

    # Extra metadata
    facility = fields.CharField(max_length=255, null=True)  # hospital/clinic
    specialization = fields.CharField(max_length=150, null=True)
    country = fields.CharField(max_length=100, null=True, default="Kenya")
    meta = fields.JSONField(null=True)

    # Timestamps
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "doctors"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_names} ({self.license_no})"
