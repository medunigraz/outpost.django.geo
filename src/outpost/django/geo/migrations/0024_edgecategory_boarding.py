from django.db import migrations, models
from outpost.django.base.key_constructors import UpdatedAtKeyBit

# Routing now minimises walking time in seconds (see RoutingEdgeViewSet). The category
# values below were chosen from a simulation on the full graph (2026-10): stairs for one
# floor, lift from two floors up, and Standard edges (mostly into rooms) still avoided.
# name: (multiplicator, addition, boarding)
NEW = {
    "Durchgang": (1.0, 0, 0),
    "Standard": (2.5, 0, 0),
    "Lift": (1.0, 5, 40),
    "Stiege": (2.0, 15, 0),
    "Versperrt": (999.0, 0, 0),
}
OLD = {
    "Durchgang": (1.0, 0, 0),
    "Standard": (2.5, 3, 0),
    "Lift": (3.0, 30, 0),
    "Stiege": (8.0, 50, 0),
    "Versperrt": (999.0, 999, 0),
}


def set_values(values):
    def apply(apps, schema_editor):
        EdgeCategory = apps.get_model("geo", "EdgeCategory")
        names = set(EdgeCategory.objects.values_list("name", flat=True))
        if not names:
            return
        missing = set(values) - names
        if missing:
            raise RuntimeError(
                f"EdgeCategory rows missing: {sorted(missing)}. Set the routing values by hand."
            )
        for name, (multiplicator, addition, boarding) in values.items():
            EdgeCategory.objects.filter(name=name).update(
                multiplicator=multiplicator, addition=addition, boarding=boarding
            )
        # Updates bypass signals, so invalidate cached routes explicitly.
        UpdatedAtKeyBit.update(apps.get_model("geo", "Edge"))

    return apply


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0023_alter_room_options_edgecategory_duration_formula_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="edgecategory",
            name="boarding",
            field=models.DecimalField(
                decimal_places=1,
                default=0,
                help_text="Seconds once per ride on a chain of edges of this category, e.g. waiting for a lift. Half is charged on the edge into the chain, half on the edge out.",
                max_digits=5,
            ),
        ),
        migrations.AlterField(
            model_name="edgecategory",
            name="addition",
            field=models.DecimalField(
                decimal_places=1,
                default=0,
                help_text="Seconds per edge on top of the walking time, e.g. per floor of stairs or lift travel.",
                max_digits=5,
            ),
        ),
        migrations.AlterField(
            model_name="edgecategory",
            name="multiplicator",
            field=models.DecimalField(
                decimal_places=1,
                default=1.0,
                help_text="Routing preference: the time on an edge is multiplied by this to choose a route, the time shown is not. 1 is neutral, above 1 avoids.",
                max_digits=4,
            ),
        ),
        migrations.RunPython(set_values(NEW), set_values(OLD)),
    ]
