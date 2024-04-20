from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Users

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = Users.objects.create(username=username, password=password)
        return JsonResponse({'message': 'User created successfully'})
    return JsonResponse({'error': 'Invalid request method'})

def update_user(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    if request.method == 'PUT':
        user.username = request.POST.get('username', user.username)
        user.password = request.POST.get('password', user.password)
        user.save()
        return JsonResponse({'message': 'User updated successfully'})
    return JsonResponse({'error': 'Invalid request method'})

def delete_user(request, user_id):
    user = get_object_or_404(Users, pk=user_id)
    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    return JsonResponse({'error': 'Invalid request method'})
