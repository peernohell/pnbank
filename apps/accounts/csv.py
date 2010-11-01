# -*- coding: utf-8 -*-

def transform_transaction(request, data):
    from pnbank.apps.accounts.models import Account, Tag
    data['account'] = Account.objects.get_or_create(name=data['account'])[0]
    data['amount'] = data['amount']
    data['checked'] = data['checked']
    data['date'] = data['date']
    data['description']  = data['description']
    data['name']      = data['name']

    taglist = []
    for tag in data['tags']:
        taglist.append(Tag.objects.get_or_create(name = tag)[0])
    data['tags'] = Tag.objects.filter(pk__in = [tag.pk for tag in taglist])

    return data


