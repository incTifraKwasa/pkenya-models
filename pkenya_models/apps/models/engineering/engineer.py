from tortoise import fields, models


class Engineer(models.Model):
    """
    Engineer registry model for EBK data.
    """

    id = fields.UUIDField(pk=True)

    # Core details
    registration_number = fields.CharField(max_length=100, unique=True, db_index=True)
    full_name = fields.CharField(max_length=255, db_index=True, null=True)
    gender = fields.CharField(max_length=1, null=True)
    postal_address = fields.CharField(max_length=255, null=True)
    category = fields.CharField(max_length=50, db_index=True)
    
    location = fields.CharField(max_length=100, db_index=True, null=True)
    postal_code = fields.CharField(max_length=100, db_index=True, null=True)

    # Extra fields for extensibility
    email = fields.CharField(max_length=255, null=True)
    phone = fields.CharField(max_length=50, null=True)
    county = fields.CharField(max_length=100, null=True)
    qualifications = fields.TextField(null=True)
    employer = fields.CharField(max_length=255, null=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "engineers"
        ordering = ["registration_number"]

    def __str__(self):
        return f"{self.registration_number} - {self.full_name} ({self.category})"

