from model import UserData, SupportData

users_data = {1: UserData(id=1, email="george.bluth@reqres.in", first_name="Janet", last_name="George",
                          avatar="https://reqres.in/img/faces/1-image.jpg", job=''),
              2: UserData(id=2, email="janet.weaver@reqres.in", first_name="Janet", last_name="Weaver",
                          avatar="https://reqres.in/img/faces/2-image.jpg", job=''),
              3: UserData(id=3, email="emma.wong@reqres.in", first_name="Emma", last_name="Wong",
                          avatar="https://reqres.in/img/faces/3-image.jpg", job=''),
              4: UserData(id=4, email="eve.holt@reqres.in", first_name="Eve", last_name="Holt",
                          avatar="https://reqres.in/img/faces/4-image.jpg", job=''),
              5: UserData(id=5, email="charles.morris@reqres.in", first_name="Charles", last_name="Morris",
                          avatar="https://reqres.in/img/faces/5-image.jpg", job='')
              }

support_data = SupportData(url="https://reqres.in/#support-heading",
                           text="To keep ReqRes free, contributions towards server costs are appreciated!")
