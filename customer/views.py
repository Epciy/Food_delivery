from django.shortcuts import render
from django.views import View

from .models import  MenuItem,Category,OrederModel
from django.core.mail import send_mail
from django.db.models import Q





class Delivery(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'customer/index.html')

class About(View):
    def get(self,request,*args,**kwargs):
        return render(request, 'customer/about.html') 

class Order(View):
    """Grab all the items for  each category than pass them into our template """
    def get(self,request,*args,**kwargs):
        appetizers=MenuItem.objects.filter(category__name__contains='Appetizer')
        desserts=MenuItem.objects.filter(category__name__contains='Dessert')
        entrees=MenuItem.objects.filter(category__name__contains='Entree')
        drinks=MenuItem.objects.filter(category__name__contains='Drink')

        context={
            'appetizers':appetizers,
            'desserts': desserts,
            'entrees':entrees ,
            'drinks':drinks,
        }

        return render(request,'customer/order.html',context)

    def post(self,request,*args,**kwargs):
        """create a dectionnary (order_items) where we can store selected item"""
        name=request.POST.get('name')
        email=request.POST.get('email')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zipe_code')

        order_items={
            'items':[]
        }
        items=request.POST.getlist('items[]')
        print(items)
        """loop through items in order to grab all the information we need from each item"""
        for item in items :
            menu_item=MenuItem.objects.get(pk__contains=int(item))
            item_data={
                'id':menu_item.pk,
                'name':menu_item.name,
                'price':menu_item.price,
            }
            order_items['items'].append(item_data)
        # total price of gthe selected item
        price=0
        item_ids=[]
        for item in order_items['items']:
            price+=item['price']
            item_ids.append(item['id'])
        order=OrederModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code
        )
        order.items.add(*item_ids)
        """send confimation email to the user """

        body=("Hi,  your food will be delivered soon!\n"
        f'Your total: {price}\n'
        'Thank you for your order!')
        send_mail(
            'Thank Your for Order!',
            body,
            'exemple@exemple.com',
            [email],
            fail_silently=False
        )
        context={
            'items':order_items['items'],
            'price':price,
            }
        return render(request,'customer/order_confirmation.html',context)


class Menu(View):
    def get(self,request,*args,**kwargs):
        menu_items=MenuItem.objects.all()
        context={
            'menu_items':menu_items
        }
        return render(request,'customer/menu.html',context)




class MenuSearch(View):
    def get(self,request,*args,**kwargs):
        query=self.request.GET.get('q')
        """we get the search query if query matches price or name or description"""
        menu_items=MenuItem.objects.filter(
            Q(name__icontains=query)|
            Q(price__icontains=query)|
            Q(description__icontains=query)
           
        )
        context={
            'menu_items':menu_items
        }
        return render(request,'customer/menu.html',context)




       


