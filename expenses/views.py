from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Sum
from django.db.models import Q

@login_required
def dashboard_view(request):
    # TODO: Add stats and charts here later
    return render(request, 'dashboard.html')

@login_required
def group_list_view(request):
    groups = Group.objects.all().order_by('name')
    return render(request, 'group_list.html', {'groups': groups})

@login_required
def label_list_view(request):
    labels = Label.objects.select_related('group').all().order_by('name')
    return render(request, 'label_list.html', {'labels': labels})

@login_required
def expense_list_view(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    paginator = Paginator(expenses, 10)  # 10 per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "expense_list.html", {"expenses": expenses})

@login_required
def income_list_view(request):
    # incomes = Income.objects.filter(user=request.user).order_by('-date')
    incomes = Income.objects.all()
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0  # Sum BEFORE pagination
    # paginator = Paginator(incomes, 10)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    search_query = request.GET.get('search', '')
    sort_option = request.GET.get('sort', 'date')  # default sort by date

    # Search filter
    if search_query:
        incomes = incomes.filter(
            Q(source__icontains=search_query) |
            Q(amount__icontains=search_query)
        )

    # Sorting options
    if sort_option in ['date', '-date', 'amount', '-amount']:
        incomes = incomes.order_by(sort_option)

    # Pagination
    paginator = Paginator(incomes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'income_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'sort_option': sort_option,
        "total_income": total_income,
    })

@login_required
def group_create_view(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_list')  # redirect to group list page (we will create next)
    else:
        form = GroupForm()
    return render(request, 'group_create.html', {'form': form})

@login_required
def label_create_view(request):
    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('label_list')
    else:
        form = LabelForm()
    return render(request, 'label_create.html', {'form': form})

@login_required
def expense_create_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, "Expense added successfully.")
            return redirect('expense_list')
    else:
        form = ExpenseForm(initial={'date': timezone.localdate()})
    return render(request, 'expense_create.html', {'form': form})

@login_required
def income_create_view(request):
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            messages.success(request, "Income added successfully.")
            return redirect("income_list")
    else:
        form = IncomeForm(initial={'date': timezone.localdate()})
    return render(request, "income_create.html", {"form": form})


def income_edit_view(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('income_list')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'income_form.html', {'form': form})

def income_delete_view(request, pk):
    income = get_object_or_404(Income, pk=pk)
    if request.method == 'POST':
        income.delete()
        return redirect('income_list')
    return render(request, 'income_confirm_delete.html', {'income': income})

