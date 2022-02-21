import CellPhoneClass as c

def main():
    my_phone = c.CellPhone('Samsung', 'Galaxy', 899)

    print('\nManufacturer:', my_phone.get_manufacturer())
    print('Model:', my_phone.get_model())
    print('Retail Price:', my_phone.get_retail_price())
    
    my_phone.set_manufacturer('Apple')
    my_phone.set_model('iPhone 13')
    my_phone.set_retail_price(1099)

    print('\nManufacturer:', my_phone.get_manufacturer())
    print('Model:', my_phone.get_model())
    print('Retail Price:', my_phone.get_retail_price())

main()
