<<<<<<< HEAD
# HTMLのフォーム部品生成
# フォーム送信データを格納・データのチェック
# 送信データをテーブルに挿入 save()
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        # Modelクラスの指定
        model = User
        # フォーム画面に表示する入力部品
=======
# HTMLのフォーム部品生成
# フォーム送信データを格納・データのチェック
# 送信データをテーブルに挿入 save()
from django import forms
from .models import User

class UserForm(forms.ModelForm):
    
    class Meta:
        # Modelクラスの指定
        model = User
        # フォーム画面に表示する入力部品
>>>>>>> 02eda6b (2025_1115_mypage_custom)
        fields = ['username', 'email']