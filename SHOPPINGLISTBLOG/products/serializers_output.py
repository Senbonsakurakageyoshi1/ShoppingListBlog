CustomerReportSerializer():
    id = IntegerField(label='ID', read_only=True)
    time_raised = DateTimeField(read_only=True)
    reference = CharField(
      max_length=20, 
      validators=[<UniqueValidator(queryset=CustomerReportRecord.objects.all())>]
    )
    description = CharField(style={'type': 'textarea'})