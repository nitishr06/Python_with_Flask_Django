import iso6346

class ShippingContainer:
    next_serial = 1337
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0
    FRIDGE_VOLUME = 100.0


    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial+= 1
        return result

    @classmethod
    def create_empty(cls, owner_code, lenght_ft, **kwargs):
        return cls(owner_code, lenght_ft, content=[])

    @classmethod
    def create_with_items(cls ,owner_code, lenght_ft ,items, **kwargs):
        return cls(owner_code, lenght_ft, content = list(items), **kwargs)

    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(owner_code=owner_code, serial = str(serial).zfill(6))


    def __init__(self,owner_code, lenght_ft, content):
        self.owner_code = owner_code
        self.lenght_ft = lenght_ft
        self.content = content
        self.bic = self._make_bic_code(owner_code = owner_code, 
        serial = ShippingContainer._generate_serial())

    @property
    def volume(self):
        return self._calc_volume()

    def _calc_volume(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.lenght_ft


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0

    def __init__(self,owner_code, lenght_ft, content,*,celsius,**kwargs):
        super().__init__(owner_code, lenght_ft, content,**kwargs)
        self.celsius = celsius

    @staticmethod
    def c_to_f(celsius):
        return celsius * 9/5 + 32

    @staticmethod
    def f_to_c(farenhite):
        return (farenhite - 32) * 5/9

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)
    
    def _set_celsius(self,value):
        if(value > RefrigeratedShippingContainer.MAX_CELSIUS):
            raise ValueError("Temprature Too High!!")
        self._celsius = value

    @property
    def farenhite(self):
        return RefrigeratedShippingContainer.c_to_f(self.celsius)

    @farenhite.setter
    def farenhite(self,value):
        self.celsius = RefrigeratedShippingContainer.f_to_c(value)

    @property
    def volume(self):
        return (super()._calc_volume - RefrigeratedShippingContainer.FRIDGE_VOLUME)
    
    
    @staticmethod
    def _make_bic_code(owner_code,serial):
        return iso6346.create(owner_code=owner_code, serial = str(serial).zfill(6),category = 'R')


class HeatedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    
    def _set_celsius(self,value):
        if value < HeatedShippingContainer.MIN_CELSIUS:
            raise ValueError("Temprature too cold!!")
        super()._set_celsius(value)

    


    
    