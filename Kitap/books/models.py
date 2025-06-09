from datetime import datetime
from reg_users.models import Profile
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

#4. валидация года
current_year = datetime.now().year

# 5. валидация возрастногг ограничения
age_validator = RegexValidator(
    regex=r'^-?\d{1,2}\+$|^-?\d{1,2}$',
    message='Мисалы: "18+", "0+", "-6", "16" ж.б.')


class Book(models.Model):
    genre = models.ManyToManyField("Genre")
    author = models.ManyToManyField("Author")
    language = models.ManyToManyField("Language")

    title = models.CharField(max_length=150, help_text="Китептин аталышы")
    year = models.IntegerField(default=True,  validators=[MinValueValidator(500), MaxValueValidator(current_year, message=f"Год не может быть больше {current_year}.")], help_text="Чыгарылган жылы")
    age_restriction = models.CharField(max_length=4, validators= [age_validator], help_text="Китеп сунушталат")
    content = models.CharField(max_length=7000, help_text="Кыскача мазмуну")
    price = models.IntegerField(validators=[MaxValueValidator(9999,  message="Баасы 9999 ойдо боло албайт")], help_text="Баасы", null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to="book/")
    file_book = models.FileField(upload_to="book/")

    # 1.валидация жанра, можно выбирать только 5 жанров

    def clean(self):
        super().clean()
        if self.pk:
            if self.genre.count() > 5:
                raise ValidationError("5тен коп жанр тандоого уруксат эмес")

    # 2. валидация добавление автора книги
    def clean(self):
        super().clean()
        if self.pk:
            if self.author.count() > 2:
                raise ValidationError("Китеп учун 2 гана автор тандоого болот")

    # 3. валидация названия книги
    def save(self, *args, **kwargs):
        self.title = self.title.capitalize()
        super().save(*args, **kwargs)

    #6. валидация фото
    def validate_img_size(photo):
        max_size = 77 * 1024 * 1024
        if photo.size > max_size:
            raise ValidationError("Сурот 77 мегабайттан ойдо боло албайт")


    #7. валидация файла
    def validate_file(file_book):
        maxsize = 1024 * 1024 * 1024
        if file_book.size > maxsize:
            raise ValidationError("Жуктоло турган файл 1 ГБ ашпаш керек")


    #8 валидация языка
    def clean(self):
        super().clean()
        if self.pk:
            if self.language.count() > 1:
                raise ValidationError("1 гана тил тандоого болот!")

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ('title', 'content')


class Genre(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=55, db_index=True)
    surname = models.CharField(max_length=60, db_index=True)

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.surname = self.surname.capitalize()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}, {self.surname}"

class Language(models.Model):
    lan = models.CharField(max_length=100)


    def __str__(self):
        return self.lan


class Review(models.Model):
    RATING_CHOICES = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=7000)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)  # от 1 до 5
    created_at = models.DateTimeField(auto_now_add=True)