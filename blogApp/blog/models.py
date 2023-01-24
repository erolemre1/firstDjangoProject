from asyncio import sleep
import pywhatkit as kit
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
import time
import qrcode
import pyautogui
import datetime
import webbrowser

# now = datetime.datetime.now()
# now
# datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
# print(now)

# kit.sendwhatmsg_to_group("+905318105767", "One hour to the deadline", 18, 33, 20, True, 10)

# img = qrcode.make('https://www.google.com')
# type(img)
# img.save("qr.png")

# def asdsd(phone):
#     print(phone)
#     kit.sendwhatmsg('+905318105767', "One hour to the deadline", 19, 54, 20, True, 10)


# n = 0
# while n < 99000000000:
#     n += 1
#     time.sleep(10)
#     asdsd(905318105767)


# for i in range(999999):
#     print(i)
# if i == 999998: kit.sendwhatmsg_to_group("CF3hryvYMSv28lankHtpNv", "One hour to the deadline", 18, 33, 20, True, 10)

# for i in range(20,99,2):
#     print(i)

# time.sleep(10)
# def message():
#     pyautogui.write("Emooooo")
#     pyautogui.press('enter')


# webbrowser.open('http://example.com')

# while True:
#         message()
#         time.sleep(0)

 


class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    file = models.FileField(upload_to="files", blank=True,
                            null=True, unique=True,  db_index=True, )
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True,
                            unique=True, db_index=True, editable=False)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(null=False, blank=True, unique=True,
                            db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
