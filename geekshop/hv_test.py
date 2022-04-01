from locust import HttpUser, TaskSet, task


def login(l):
    l.client.post("/auth/login/", {"username":"admin", "password":"123456"})


def logout(l):
    l.client.post("/auth/logout/", {"username":"admin", "password":"123456"})


def index(l):
    l.client.get("/")

# def profile(l):
#     l.client.get("auth/edit/")


def products(l):
    l.client.get("/products/")

def contacts(l):
    l.client.get("/contacts/")

def products_cat2(l):
    l.client.get("/products/category/32/")

def products_cat3(l):
    l.client.get("/products/category/33/")

def products_pro1(l):
    l.client.get("/products/product/2/")

def products_pro2(l):
    l.client.get("/products/product/10/")

def products_pro3(l):
    l.client.get("/products/product/3/")

def products_pro4(l):
    l.client.get("/products/product/4/")


@task
class UserBehavior(TaskSet):
    tasks = {index: 2,
             products: 2,
             products_cat3: 2,
             products_cat2: 2,
             products_pro1: 2,
             products_pro2: 2,
             products_pro3: 2,
             products_pro4: 2,
             }

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)
@task
class WebsiteUser(HttpUser):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000


# locust -f hv_test.py -H IP_MY_SERVER