from django.shortcuts import render, redirect
from django.contrib import messages
 
# import todo form and models
 
from .forms import TodoForm
from .models import Todo
 
###############################################
 
 
def index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
 
    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)
 
 
### function to remove item, it receive todo item_id from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('/')

### function to update item,  it receive todo item_id from url ##
def update(request, pk):
	item = Todo.objects.get(id=pk)
	form = TodoForm(instance=item)

	if request.method == 'POST':
		form = TodoForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('/')

	context =  {'taskEditForm':form}
	return render(request, 'todo/updateTask.html', context)