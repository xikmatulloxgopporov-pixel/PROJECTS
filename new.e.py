# class User:
#     def __init__(self,user_id,username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self,user):
#         user.followers += 1
#         self.following += 1
# user_1 = User("001","angela")
# user_2 = User("002","Jack")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)
# class Talaba:
#     def __init__(self,ism,familiya, tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
#     def get_ism(self):
#         return self.ism
#     def tanishtr(self):
#         return f'Ismim {self.ism},familiya {self.familiya},tyil {self.tyil}'
# talaba1 = Talaba("Olim","Olimov",2000)
# talaba2 = Talaba("Najim","G`ulomov",1999)
# talaba3 = Talaba("HIkmat","Toshmatov",2007)
# print(talaba1.tanishtr())
# # print(talaba2.tanishtr())
# class Avto:
#     def __init__(self, model, rang, korobka, narh, km=0):
#         self.model = model
#         self.rang = rang
#         self.korobka = korobka
#         self.narh = narh
#         self.km = km
#
#     def get_info(self):
#         return (f"Model: {self.model}, Rang: {self.rang}, "
#                 f"Korobka: {self.korobka}, Narh: {self.narh}$, "
#                 f"Yurgan km: {self.km} km")
#
#     def update_km(self, yangi_km):
#         if yangi_km >= 0:
#             self.km += yangi_km
#         else:
#             print("Km manfiy bo‘lishi mumkin emas")
# avto1 = Avto("Malibu", "Qora", "Avtomat", 25000)
#
# print(avto1.get_info())
# avto1.update_km(150)
# print(avto1.get_info())
#
#
# class Avtosalon:
#     def __init__(self, nomi, manzil):
#         self.nomi = nomi
#         self.manzil = manzil
#         self.avtolar = []
#
#     def add_avto(self, avto):
#         self.avtolar.append(avto)
#
#     def get_avtolar_info(self):
#         info = f"🏢 Avtosalon: {self.nomi}\n Manzil: {self.manzil}\n"
#         for avto in self.avtolar:
#             info += avto.get_info() + "\n"
#         return info
#
# salon = Avtosalon("GM Uzbekistan", "Toshkent")
#
# avto2 = Avto("Cobalt", "Oq", "Mexanika", 12000)
# avto3 = Avto("Tracker", "Ko‘k", "Avtomat", 22000)
#
# salon.add_avto(avto1)
# salon.add_avto(avto2)
# salon.add_avto(avto3)
#
# print(salon.get_avtolar_info())
# print(avto1.__dict__)
# print(dir(str))
# print(dir(int))



