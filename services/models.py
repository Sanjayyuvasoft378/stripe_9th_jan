from django.db import models
from django.core import validators

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=70,
        verbose_name='Product Name'
    )

    description = models.TextField(
        max_length=800,
        verbose_name='Description'
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[
            validators.MinValueValidator(50),
            validators.MaxValueValidator(100000)
        ]
    )
    
    
class OrderDetail(models.Model):
    
    id = models.BigAutoField(
        primary_key=True
    )

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    product = models.ForeignKey(
        to=Product,
        verbose_name='Product',
        on_delete=models.PROTECT
    )

    amount = models.IntegerField(
        verbose_name='Amount'
    )

    stripe_payment_intent = models.CharField(
        max_length=200
    )

    # This field can be changed as status
    has_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )




# Create your models here.

# class Course(models.Model):
#     course_name = models.CharField(max_length=20)
#     course_description = RichTextField()
#     is_premium = models.BooleanField(default=False)
#     course_image = models.ImageField(upload_to='course/')
#     slug=models.SlugField(blank=True)
    
#     def save(self,*args, **kwargs):
#         self.slug = slugify(self.course_name)
#         super(Course,self).save(*args,**kwargs)
    
#     def __str__(self):
#         return self.course_name


# class CourseModule(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     course_module_name = models.CharField(max_length=100)
#     course_description = RichTextField()
#     video_url = models.URLField(max_length=300)
#     can_view = models.BooleanField(default=False)
    

    
