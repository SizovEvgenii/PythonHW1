from Address import Address
from Mailing import Mailing

from_address = Address('32523', 'Москва', 'Тверская', '1', '101')
to_address = Address('64532', 'Санкт-Петербург', 'Невский', '10', '202')

mail = Mailing(to_address=to_address,from_address=from_address,cost=500, track="TRACK123")

print(mail)