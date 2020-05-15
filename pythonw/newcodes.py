'''---------------------------------------------------------------------------------
نحوه ایجاد یک ListView در جانگو

در views در زیر کلاس مربوطه
model = MyModel
template_name='temp.html'
[context_object_name='somname']
در فایل temp.html
{% for myModel in (somname or context_object_name) %}
  do smth
{% endfor %}
----------------------------------------------------------------------------------
نحوه ایجاد یک DetailView در جانگو

در views در کلاس مربوطه
model = MyModel
template_name = 'temp.html'
در temp.html
در urls.py
path('appname/<int:pk>/', BlogDetailView.as_view(), name='temp'),
در temp.html
do sth with myModel
----------------------------------------------------------------------------------
در جانگو نحوه ایجاد یک CreateView

در views در کلاس مربوطه
model = MyModel
template_name = 'temp.html'
fields = [لیست فیلدهای لازم برای ایجاد یک ردیف در جدول]
در temp.html
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save" />
</form>
----------------------------------------------------------------------------------
در جانگو نحوه ایجاد یک UpdateView

در views در کلاس مربوطه
model = MyModel
template_name = 'temp.html'
fields = [لیست فیلدهای لازم برای به روز رسانی یک ردیف در جدول]
در temp.html
<form action="" method="post">{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Update" />
</form>
در urls.py
path('appname/<int:pk>/edit/', BlogUpdateView.as_view(), name='temp'),
----------------------------------------------------------------------------------
برای ساخت یک DeleteView در جنگو

در views در کلاس مربوطه
model = MyModel
template_name = 'temp.html'
success_url = reverse_lazy('revers name in urls.py')
در temp.html
<form action="" method="post">{% csrf_token %}
    <p>Are you sure you want to delete "{{ myModel.title }}"?</p>
    <input type="submit" value="Confirm" />
</form>
در urls.py
path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
----------------------------------------------------------------------------------
git در pycharm برای پوش کردن در

ctrl+shift+k
----------------------------------------------------------------------------------
تنظیمات در pycharm
crtl+alt+s
----------------------------------------------------------------------------------
تبدیل حروف کوچک به بزرگ و بالعکس در پایچارم
ctrl+shift+U
----------------------------------------------------------------------------------
باز و بسته کردن بلاک در پایچارم
ctrl+ +/-
----------------------------------------------------------------------------------
برای commit کردن در پایچارم
ctrl+k
----------------------------------------------------------------------------------

----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
----------------------------------------------------------------------------------
'''