# -*- coding: utf-8 -*-
"""
Created on Tue May 22 10:28:49 2018

@author: Vishnu
"""

import re
from sklearn.externals import joblib
import os
from .mappings import brand, mem, cam, size, OS, plans, yesorno, store, model, spec, low, gsm, cust, uae, card, names, no
import base64
from .models import RequestCache, UserCache
import aiml
import dill

os.chdir('C:/Users/hp/eclipse-workspace/AIStore/AIStore/')
brain_file = 'QA.brn'

def create_cache(CACHE_ID):
    try:
        req_cache = RequestCache.objects.get(cache_id=CACHE_ID)
        print 'req_cache', req_cache
    except RequestCache.DoesNotExist:
        kern_medical = aiml.Kernel()
        kern_medical.bootstrap(brainFile=brain_file)
        kernel_str = dill.dumps(kern_medical)
        kernel_str = base64.b64encode(kernel_str)
        req_cache = RequestCache.objects.create(cache_id=CACHE_ID, cache=[],
                                                user=UserCache.objects
                                                .create(aiml_kernel=kernel_str)
                                                )
    return req_cache

def get_customer(text, cache_list):
    text = text.lower()
    dict_cust = {}
    for key, value in cust.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_cust['Customer'] = key
                cache_list = remove_duplicate(cache_list, 'Customer')
                cache_list.append(dict_cust)
    return cache_list

def get_citizen(text, cache_list):
    text = text.lower()
    dict_citi = {}
    for key, value in uae.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_citi['Citizen'] = key
                cache_list = remove_duplicate(cache_list, 'Citizen')
                cache_list.append(dict_citi)
    return cache_list

def get_card(text, cache_list):
    text = text.lower()
    dict_card = {}
    for key, value in card.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_card['Card'] = key
                cache_list = remove_duplicate(cache_list, 'Card')
                cache_list.append(dict_card)
    return cache_list

def get_brand(text, cache_list):
    text = text.lower()
    dict_brand = {}
    for key, value in brand.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_brand['Brand'] = key
                cache_list = remove_duplicate(cache_list, 'Brand')
                cache_list.append(dict_brand)
    return cache_list

def get_spec(text, cache_list):
    text = text.lower()
    dict_spec = {}
    for key, value in spec.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_spec['Features'] = key
                cache_list = remove_duplicate(cache_list, 'Features')
                cache_list.append(dict_spec)
    return cache_list

# def get_top(text, cache_list):
#     text = text.lower()
#     dict_top = {}
#     for key, value in top.items():
#         for i in value:
#             match = re.compile(r"\b%s\b"%(i))
#             ent = match.findall(text)
#             if len(ent) != 0:
#                 dict_top['Top'] = key
#                 cache_list = remove_duplicate(cache_list, 'Top')
#                 cache_list.append(dict_top)
#     return cache_list

def get_low(text, cache_list):
    text = text.lower()
    dict_low = {}
    for key, value in low.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_low['Low'] = key
                cache_list = remove_duplicate(cache_list, 'Low')
                cache_list.append(dict_low)
    return cache_list

def get_model(text, cache_list):
    text = text.lower()
    dict_brand = {}
    for key, value in model.items():
        for i in value:
            i = i.lower()
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_brand['Model'] = key
                cache_list = remove_duplicate(cache_list, 'Model')
                cache_list.append(dict_brand)
    return cache_list

def get_RAM(text, cache_list):
    text = text.lower()
    dict_ram = {}
    for key, value in mem.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_ram['RAM'] = key
                cache_list = remove_duplicate(cache_list, 'RAM')
                cache_list.append(dict_ram)
    return cache_list

def get_storage(text, cache_list):
    text = text.lower()
    dict_storage = {}
    for key, value in store.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_storage['Storage'] = key
                cache_list = remove_duplicate(cache_list, 'Storage')
                cache_list.append(dict_storage)
    return cache_list

def get_frontcam(text, cache_list):
    text = text.lower()
    dict_frontcam = {}
    for key, value in cam.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_frontcam['Front Cam'] = key
                cache_list = remove_duplicate(cache_list, 'Front Cam')
                cache_list.append(dict_frontcam)
    return cache_list

def get_backcam(text, cache_list):
    text = text.lower()
    dict_backcam = {}
    for key, value in cam.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_backcam['Back Cam'] = key
                cache_list = remove_duplicate(cache_list, 'Back Cam')
                cache_list.append(dict_backcam)
    return cache_list

def get_size(text, cache_list):
    text = text.lower()
    dict_size = {}
    for key, value in size.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_size['Screen Size'] = key
                cache_list = remove_duplicate(cache_list, 'Screen Size')
                cache_list.append(dict_size)
    return cache_list

def get_os(text, cache_list):
    text = text.lower()
    dict_os = {}
    for key, value in OS.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_os['OS'] = key
                cache_list = remove_duplicate(cache_list, 'OS')
                cache_list.append(dict_os)
    return cache_list

def get_budget(text, cache_list):
    text = str(text)
    text = text.lower()
    list_budget = re.findall(r'(\d{1,9})', text)
    dict_budget = {}
    if len(list_budget) != 0:
        for i in list_budget:
            if len(str(i)) >= 2:
                dict_budget['Price'] = i
                cache_list = remove_duplicate(cache_list, 'Price')
                cache_list.append(dict_budget)
    else:
        for key, value in no.items():
            for i in value:
                match = re.compile(r"\b%s\b"%(i))
                ent = match.findall(text)
                if len(ent) != 0:
                    dict_budget['Price'] = key
                    cache_list = remove_duplicate(cache_list, 'Price')
                    cache_list.append(dict_budget)
    return cache_list

def get_quest(text, cache_list):
    text = text.lower()
    dict_quest = {}
    for key, value in yesorno.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_quest['Question'] = key
                cache_list = remove_duplicate(cache_list, 'Question')
                cache_list.append(dict_quest)
    return cache_list

def get_plantype(text, cache_list):
    text = text.lower()
    dict_plan = {}
    for key, value in gsm.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_plan['Plan_type'] = key
                cache_list = remove_duplicate(cache_list, 'Plan_type')
                cache_list.append(dict_plan)
    return cache_list
                
def get_plan(text, cache_list):
    text = text.lower()
    dict_plan = {}
    for key, value in plans.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_plan['Plan'] = key
                cache_list = remove_duplicate(cache_list, 'Plan')
                cache_list.append(dict_plan)
    return cache_list

def get_data(text, cache_list):
    text = text.lower()
    dict_data = {}
    for key, value in yesorno.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_data['Data'] = key
                cache_list = remove_duplicate(cache_list, 'Data')
                cache_list.append(dict_data)
    return cache_list

def get_voice(text, cache_list):
    text = text.lower()
    dict_voice = {}
    for key, value in yesorno.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_voice['Voice'] = key
                cache_list = remove_duplicate(cache_list, 'Voice')
                cache_list.append(dict_voice)
    return cache_list

def get_international(text, cache_list):
    text = text.lower()
    dict_int = {}
    for key, value in yesorno.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_int['International'] = key
                cache_list = remove_duplicate(cache_list, 'International')
                cache_list.append(dict_int)
    return cache_list

def get_combo(text, cache_list):
    text = text.lower()
    dict_combo = {}
    for key, value in yesorno.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_combo['Combo'] = key
                cache_list = remove_duplicate(cache_list, 'Combo')
                cache_list.append(dict_combo)
    return cache_list

def get_assistance(text, cache_list):
    text = text.lower()
    dict_assistance = {}
    for key, value in yesorno.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_assistance['Assist'] = key
                cache_list = remove_duplicate(cache_list, 'Assist')
                cache_list.append(dict_assistance)
    return cache_list

def get_name(text, cache_list):
    text = text.lower()
    dict_name = {}
    for key, value in names.items():
        for i in value:
            match = re.compile(r"\b%s\b"%(i))
            ent = match.findall(text)
            if len(ent) != 0:
                dict_name['Name'] = key
    if len(dict_name) > 0:
        cache_list = remove_duplicate(cache_list, 'Name')
        cache_list.append(dict_name)
    else:
        dict_name['Name'] = 'invalid'
        cache_list = remove_duplicate(cache_list, 'Name')
        cache_list.append(dict_name)        
    return cache_list

def intent_classifier(text):
    text_list = []
    text_list.append(str(text))
    clf = joblib.load('intent_model.pkl')
    label = clf.predict(text_list)
    return label[0]

def greeting_classifier(text):
    text_list = []
    text_list.append(str(text))
    clf = joblib.load('greeting_model.pkl')
    label = clf.predict(text_list)
    return label[0]

def remove_duplicate(lists, key_name):
    if len(lists) != 0:
        for dicts in lists:
            if key_name in dicts:
                lists.remove(dicts)
    return lists
