from api.models import Shoe, Person
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_user_shoes(request):
    uid = request.GET.get('userid', 0)
    person = Person.objects.get(id=uid)
    shoes = list(Shoe.objects.filter(user_id=uid).values("id", "size", "color"))
    ret = dict(username=person.name, shoes=shoes)
    return Response(ret)


@api_view(['POST'])
def update_user_shoes(request):
    req = request.data
    username = req.get('name', '')
    phone = req.get('phone', '')
    shoes = req.get('shoes', {})
    uid = Person.objects.create(name=username, phone=phone).id
    shoe_list = []
    for shoe in shoes:
        color = shoe.get('color', '')
        size = shoe.get('size', 0)
        shoe_list.append(Shoe.objects.create(id=None, color=color, user_id=uid, size=size).id)
    return Response({"success": True, "message": "ok", 'result': {"userId": uid, "shoesId": shoe_list}})

