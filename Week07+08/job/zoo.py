#!/usr/bin/python3
# -*- coding: utf-8 -*-

# ==================================================================
# v1.0 04BF9101 maqiang <maqiang626@qq.com> [2020-11-22 18:00 +0800]
# Verified: Windows 10 20H2 &&& Python v3.7.9
#
# 1. 定义“动物”、“猫”、“狗”、“动物园”四个类，动物类不允许被实例化
# 2. 动物类要求定义“类型”、“体型”、“性格”、“是否属于凶猛动物”四个属性，是否属于凶猛动物的判断标准是：“体型 >= 中等”并且是“食肉类型”同时“性格凶猛”
# 3. 猫类要求有“叫声”、“是否适合作为宠物”以及“名字”三个属性，其中“叫声”作为类属性，除凶猛动物外都适合作为宠物，猫类继承自动物类。狗类属性与猫类相同，继承自动物类
# 4. 动物园类要求有“名字”属性和“添加动物”的方法，“添加动物”方法要实现同一只动物（同一个动物实例）不能被重复添加的功能
#
# ==================================================================
#


from abc import ABCMeta, abstractmethod


class Zoo(object):
    """动物园类

    1. 属性: 
        name 名字
        animals 已添加的动物
    2. 方法: add_animal => 同一只动物（同一个动物实例）不能被重复添加

    """

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal(self, animal):
        animal_id = id(animal)
        if animal_id not in self.animals.keys():
            self.animals[animal_id] = animal
            setattr(self, animal.__class__.__name__, True)
        else:
            print(f'[warning]id: {animal_id} 同一只动物（同一个动物实例）不能被重复添加')


class Animal(metaclass=ABCMeta):
    """动物类

    1. 不允许被实例化
    2. 属性: 
        kind 类型 => ('食肉', '食草')
        somatotype 体型 => ('大', '中', '小')
        disposition 性格 => ('温顺', '凶猛')
        _is_ferocious 是否属于凶猛动物 => “体型 >= 中等”并且是“食肉类型”同时“性格凶猛” ('True', 'False')

    """

    @abstractmethod
    def __init__(self,  kind, somatotype, disposition):
        self.kind = kind
        self.somatotype = somatotype
        self.disposition = disposition

    @property
    def _is_ferocious(self):
        return self.somatotype in ('大', '中') and self.kind == '食肉' and self.disposition == '凶猛'


class Cat(Animal):
    """猫类

    1. 继承自动物类
    2. 属性: 
        shout 叫声 => 类属性
        name 名字
        is_pet 是否适合作为宠物 => 除凶猛动物外 ('True', 'False')

    """

    shout = 'miao...miao...miao...'

    def __init__(self, name, kind, somatotype, disposition):
        super().__init__(kind, somatotype, disposition)
        self.name = name
        self.is_pet = not self._is_ferocious


class Dog(Animal):
    """狗类

    1. 继承自动物类
    2. 属性: 
        shout 叫声 => 类属性
        name 名字
        is_pet 是否适合作为宠物 => 除凶猛动物外

    """

    shout = 'wang...wang...wang...'

    def __init__(self, name, kind, somatotype, disposition):
        super().__init__(kind, somatotype, disposition)
        self.name = name
        self.is_pet = not self._is_ferocious


if __name__ == '__main__':
    # 实例化动物园
    z = Zoo('时间动物园')

    # 实例化一只猫，属性包括名字、类型、体型、性格
    cat1 = Cat('大花猫 1', '食肉', '小', '温顺')
    cat2 = Cat('苏格兰折耳猫', '食肉', '中', '温顺')
    cat3 = Cat('波斯猫', '食肉', '大', '温顺')
    cat4 = Cat('帕拉斯猫', '食肉', '大', '凶猛')
    print(f'[cat1] 是否适合作为宠物: {cat1.is_pet}')
    print(f'[cat4] 是否适合作为宠物: {cat4.is_pet}')

    # 增加一只猫到动物园
    z.add_animal(cat1)
    print(f'z.animals {z.animals}')
    z.add_animal(cat2)
    print(f'z.animals {z.animals}')
    z.add_animal(cat1)
    print(f'z.animals {z.animals}')

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(f'[have_cat] {have_cat}')

    # 动物园是否有狗这种动物
    have_dog = hasattr(z, 'Dog')
    print(f'[have_dog] {have_dog}')

    print('==================================================================')

    # 实例化一只狗，属性包括名字、类型、体型、性格
    dog1 = Dog('哈士奇', '食肉', '中', '温顺')
    dog2 = Dog('藏獒', '食肉', '大', '凶猛')
    print(f'[dog1] 是否适合作为宠物: {dog1.is_pet}')
    print(f'[dog2] 是否适合作为宠物: {dog2.is_pet}')

    # 增加一只狗到动物园
    z.add_animal(dog1)
    print(f'z.animals {z.animals}')
    z.add_animal(dog2)
    print(f'z.animals {z.animals}')
    z.add_animal(dog1)
    print(f'z.animals {z.animals}')

    # 动物园是否有猫这种动物
    have_cat = hasattr(z, 'Cat')
    print(f'[have_cat] {have_cat}')

    # 动物园是否有狗这种动物
    have_dog = hasattr(z, 'Dog')
    print(f'[have_dog] {have_dog}')
