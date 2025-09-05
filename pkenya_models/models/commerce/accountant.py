from tortoise import models, fields


class Accountant(models.Model):
    id = fields.UUIDField(pk=True, db_index=True)
    name = fields.CharField(max_length=500, blank=True, null=True)
    member_no = fields.CharField(max_length=200, db_index=True, unique=True)
    status = fields.CharField(max_length=20)
    standing = fields.CharField(max_length=200)

    class Meta:
        db_table = "accountant"
        verbose_name = "Accountant"
        verbose_name_plural = "Accountants"

    def __str__(self):
        return f"({self.name}) ({self.member_no})"
