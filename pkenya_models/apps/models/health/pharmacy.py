from tortoise import fields, models


class BaseProfession(models.Model):
    """
    Base model for professional regulatory bodies.
    Contains common fields for professions like Pharmacy, PharmTech, etc.
    """

    id = fields.UUIDField(pk=True, db_index=True)
    name = fields.CharField(max_length=255)
    registration_number = fields.CharField(max_length=100, unique=True, db_index=True)
    license_number = fields.CharField(max_length=100, unique=True, db_index=True)
    status = fields.CharField(max_length=50)
    valid_till = fields.DateField(null=True)
    timestamp = fields.DatetimeField(auto_now_add=True)
    is_active = fields.BooleanField(default=False)
    photo = fields.TextField(null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.name} ({self.registration_number})"

    def save(self, *args, **kwargs):
        self.is_active = self.status.lower() == "active"
        return super().save(*args, **kwargs)


class Pharmacy(BaseProfession):
    class Meta:
        table = "pharmacies"


class PharmTech(BaseProfession):
    class Meta:
        table = "pharmtechs"
