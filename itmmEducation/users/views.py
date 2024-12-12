from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def personal_account(request):
    # Создаём профиль, если он отсутствует
    if not hasattr(request.user, 'profile'):
        from users.models import Profile
        Profile.objects.create(user=request.user)

    return render(request, 'users/account.html', {
        'username': request.user.username,
        'tokens': request.user.token.amount,
        'avatar_url': request.user.profile.avatar_url
    })