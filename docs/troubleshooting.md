# Troubleshooting

One of the most common problems you might run into whilst developing a Django project is a mismatch or conflict with migrations.

If you see an error like this, it's a good indication it's a migration issue.

```
MySQLdb._exceptions.OperationalError: (1050, "Table 'mod_app_topic' already exists")
```

#### Explanation

This error will typically occur if your app has previously applied the migration relevant to the table, let's call it migration 35, and is now trying to reapply it.

This can happen if you switch branches to one where the latest migration is 34 and don't unapply migration 35. If you run the migrate on the branch with migration 34, the app will think it should be on 34 but will still have table created in 35, so when you switch to the newer branch with 35, the app will try to apply it but will find it already has the table outlined in 35.

### Steps

To get a picture of the migrations that have been applied and to help pinpoint which migration is causing the issue, run

```bash
python manage.py showmigrations
```

Assuming the contents of the migration haven't changed since they were first applied, simply fake the earliest migration that hasn't been applied

```bash
python manage.py migrate <app_name> <migration number> --fake
```

_A small note on migration numbers: they will typically have 4 digits, in our example, migration 35 would be `0035`_

Once the migration causing the issue has been faked, you should be able to apply the rest of the migrations

```bash
python manage.py migrate
```

You can check that everything is up to date and as expected by creating a new migration. This will pick up if there are other changes that are in the codebase but not reflected in the migrations. If a new file is created, investigate its contents before applying.

```bash
python manage.py makemigrations
```

---

If the contents of the migration file _have_ changed since they were first applied, you should still `--fake` the offending migration but then unapply it by migrating to the number before and then reapply the migration. This may not resolve the issue depending on what changes have been made.
