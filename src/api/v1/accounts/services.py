def upload_avatar_path(instance, image):
    return f'users/{instance.username}/{image}'


def upload_resume_path(instance, resume):
    return f'users/{instance.username}/{resume}'


def upload_tariff_path(instance, logo):
    return f'tariff/{instance.name}/{logo}'

def upload_product_path(instance, image):
    return f'products/{instance.author.username}/{instance.title}/{image}'

def upload_category_path(instance, image):
    return f"categories/{instance.name}/{image}"
