from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render 
from models import Expense, Category, GroupExpense
from filters import ExpenseFilter
@login_required 

def expense_list(request): 

    expenses = Expense.objects.filter(user=request.user) 

    return render(request, 'expense_list.html', {'expenses': expenses}) 

@login_required 

def add_category(request): 

    if request.method == 'POST': 

        name = request.POST['name'] 

        Category.objects.create(name=name, user=request.user) 

    return redirect('category_list') 

@login_required 

def expense_list(request): 

    expenses = Expense.objects.filter(user=request.user) 

    expense_filter = ExpenseFilter(request.GET, queryset=expenses) 

    return render(request, 'expense_list.html', {'filter': expense_filter}) 


@login_required 

def add_group_expense(request): 

    if request.method == 'POST': 

        name = request.POST['name'] 

        amount = request.POST['amount'] 

        users = request.POST.getlist('users') 

        group_expense = GroupExpense.objects.create(name=name, amount=amount, date=timezone.now()) 

        group_expense.users.set(users) 

    return redirect('group_expense_list')


@login_required 

def group_expense_list(request): 

    expenses = GroupExpense.objects.all() 

    return render(request, 'group_expense_list.html', {'expenses': expenses}) 

 