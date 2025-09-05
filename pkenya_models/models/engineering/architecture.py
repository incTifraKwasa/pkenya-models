from tortoise import fields
from tortoise.models import Model


class _Base(Model):
    id = fields.UUIDField(pk=True, db_index=True)
    registration_number = fields.CharField(max_length=50, unique=True, db_index=True)
    full_name = fields.CharField(max_length=255)
    postal_address = fields.CharField(max_length=255, null=True)
    town = fields.CharField(max_length=100, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        abstract = True


class Architect(_Base):
    # Any additional fields specific to architects can go here
    class Meta:
        db_table = "architects"
        verbose_name = "Architect"
        verbose_name_plural = "Architects"


class QuantitySurveyor(_Base):
    # Any additional fields specific to quantity surveyors can go here
    class Meta:
        db_table = "quantity_surveyors"
        verbose_name = "Quantity Surveyor"
        verbose_name_plural = "Quantity Surveyors"
