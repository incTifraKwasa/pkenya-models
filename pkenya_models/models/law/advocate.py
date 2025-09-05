from tortoise import models, fields


class Advocate(models.Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=300, null=True, db_index=True)
    profile_image = fields.TextField(null=True)
    advocate_number = fields.CharField(max_length=300, unique=True, db_index=True)
    postal_address = fields.TextField(null=True)
    email = fields.TextField(null=True)
    phone = fields.TextField(null=True)
    law_firm = fields.TextField(null=True)
    detail_page = fields.TextField(null=True)

    cpd_compliance = fields.JSONField(null=True)
    practice_distribution = fields.JSONField(null=True)
    meta = fields.JSONField(null=True)

    timestamp = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "advocates"
        ordering = ["-timestamp"]

    def __str__(self):
        return f"{self.name or ''} ({self.advocate_number})"
