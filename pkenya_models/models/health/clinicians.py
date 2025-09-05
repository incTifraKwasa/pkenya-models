from tortoise import fields
from tortoise.models import Model


class Clinician(Model):
    id = fields.UUIDField(pk=True)

    full_name = fields.CharField(max_length=255)
    practice_license_number = fields.CharField(max_length=50, null=True, db_index=True)
    status = fields.CharField(max_length=50, null=True)
    valid_till = fields.DateField(null=True)
    image_url = fields.CharField(max_length=500, null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)
    qualifications: fields.ReverseRelation["Qualification"]

    class Meta:
        db_table = "clinicians"
        verbose_name = "Clinician"
        verbose_name_plural = "Clinicians"


class Qualification(Model):
    id = fields.IntField(pk=True)

    clinician: fields.ForeignKeyRelation[Clinician] = fields.ForeignKeyField(
        "scrapy_models.Clinician",
        related_name="qualifications",
        on_delete=fields.CASCADE,
    )

    institution = fields.CharField(max_length=255, db_index=True)
    year = fields.IntField(null=True)

    registration_number = fields.CharField(max_length=50, null=True, db_index=True)
    registration_date = fields.DateField(null=True)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        db_table = "qualifications"
        verbose_name = "Qualification"
        verbose_name_plural = "Qualifications"
