GENDERS = [
    {
        'name': 'мужской'
    },
    {
        'name': 'женский'
    },
    {
        'name': 'универсал'
    },
]

CATEGORIES = [
    {
        'image': 'images/categories/изображение_2024-02-06_201048238.png',
        'name': 'Худи'
    },
    {
        'image': 'images/categories/670-image.jpg',
        'name': 'Штаны'
    },
    {
        'image': 'images/categories/1680419263_phonoteka-org-p-drein-futbolka-art-krasivo-2.jpg',
        'name': 'Футболки'
    },
]

ITEMS = [
    {
        'name': "Kitty",
        'price': 10000,
        'image': "images/categories/изображение_2024-02-06_201048238.png",
        'is_sale': True,
        'discount': 10,
        'category_id': 1,
        'gender_id': 3,
        'description': "norm"
    },
]


INITIAL_OBJECTS = [
    {
        "app": "main",
        "model": "ItemGender",
        "kwargs": GENDERS
    },
    {
        "app": "main",
        "model": "Category",
        "kwargs": CATEGORIES
    },
    {
        "app": "main",
        "model": "Item",
        "kwargs": ITEMS
    }
]
