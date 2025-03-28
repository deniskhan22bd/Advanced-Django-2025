import django_filters 

 

class ExpenseFilter(django_filters.FilterSet): 

    date = django_filters.DateFromToRangeFilter() 

    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all()) 

 

    class Meta: 

        model = Expense 

        fields = ['date', 'category'] 