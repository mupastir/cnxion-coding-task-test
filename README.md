# cnxion coding task test
CNXION Coding Task
___
For setting data scheme it is used python dictionary in settings of the project.
It should have following style:
`{"name": {"type": "string", "nullable": True}}`

After starting project it will be created form with fields set in settings,
django contains its validation of default form fields, that's why it
just converted data to json and storing in GenericModel, which contains
one field `_data`: JSONField.
