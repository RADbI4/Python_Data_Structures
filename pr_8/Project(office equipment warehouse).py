departments_of_company = [45, 65, 78, 115, 78, 92, 346, 75, 81, 11, 8, 35, 42, 43]
"""
45 - is Werehouse department
"""


class Warehouse:  # There and next "w" in code will be mean "warehouse"

    def __init__(self,
                 w_size_A_lenght_mm: int,
                 w_size_B_width_mm: int,
                 w_size_H_height_mm: int,
                 _w_room_temperature_C: int,
                 w_room_humidity: int,
                 w_has_firefighting_system: bool,
                 w_has_door: bool,
                 w_has_windows: bool,
                 w_doors_count: int,
                 w_widows_count: int,
                 __w_office_equipment_data_base: dict,
                 ):
        self.w_size_A_lenght_mm = w_size_A_lenght_mm
        self.w_size_B_width_mm = w_size_B_width_mm
        self.w_size_H_height_mm = w_size_H_height_mm
        self._w_room_temperature_C = _w_room_temperature_C
        self.w_room_humidity = w_room_humidity
        self.w_has_firefighting_system = w_has_firefighting_system
        self.w_has_door = w_has_door
        self.w_has_windows = w_has_windows
        self.w_doors_count = w_doors_count
        self.w_widows_count = w_widows_count
        self.w_office_equipment_data_base = __w_office_equipment_data_base

    def __str__(self):
        return f"Склад размерами (длинна, ширина, высота:{self.w_size_A_lenght_mm}х" \
               f"{self.w_size_B_width_mm}х{self.w_size_H_height_mm}\n С дверью {self.w_has_door} и " \
               f"с количеством окон: {self.w_widows_count}. \n" \
               f"Склад оснащён системой пожаротушения: {self.w_has_firefighting_system}"

    def w_get_area(self):
        return self.w_size_A_lenght_mm * self.w_size_B_width_mm

    def w_get_perimetr(self):
        return self.w_size_A_lenght_mm * 2 + self.w_size_B_width_mm * 2

    def w_get_volume(self):
        return self.w_size_B_width_mm * self.w_size_B_width_mm * self.w_size_H_height_mm

    @staticmethod
    def w_open():
        return f'Склад открыт'

    @staticmethod
    def w_close():
        return f'Склад закрыт'

    def show_w_office_equipment(self, type_1, type_2, type_3):
        types_in_w = len(self.w_office_equipment_data_base.keys())
        count_of_type_1 = self.w_office_equipment_data_base.setdefault(type_1)
        count_of_type_2 = self.w_office_equipment_data_base.setdefault(type_2)
        count_of_type_3 = self.w_office_equipment_data_base.setdefault(type_3)
        return f'На складе находятся следующие типы оффисной техники: {types_in_w} в количестве: ' \
               f'{len(count_of_type_1)+len(count_of_type_2) + len(count_of_type_3)}\n' \
               f'Из них:\n' \
               f'{type_1} - {len(count_of_type_1)} шт.\n' \
               f'{type_2} - {len(count_of_type_2)} шт.\n' \
               f'{type_3} - {len(count_of_type_3)} шт.\n'

    def w_office_equipment_buy(self, type_of_equipment: str):
        self.list_of_one_type_of_equipment = []
        w_office_equipment = {type_of_equipment:  self.list_of_one_type_of_equipment}
        self.w_office_equipment_data_base.update(w_office_equipment)
        return f'Компания купила новый тип оргтехники: {type_of_equipment}!'

    def w_office_equipment_income(self, type_of_tech: str, name_of_tech: str, inventary_number_of_tech: int):
        incoming_tech = [type_of_tech, name_of_tech, inventary_number_of_tech]
        self.list_of_one_type_of_equipment.append(incoming_tech)
        return f'На склад прибыл {type_of_tech}, под инвентарным номером: {inventary_number_of_tech}'

    def w_office_equipment_outcome(self, type_of_equipment: str, inventory_number: int, department: int):
        list_of_tech_by_type = self.w_office_equipment_data_base.pop(type_of_equipment)
        list_of_tech_by_type = list_of_tech_by_type.pop(inventory_number)
        self.w_office_equipment_data_base.update({type_of_equipment: [list_of_tech_by_type]})
        return f'Со склада убыл {type_of_equipment}, под инвентарным номером: {inventory_number} ' \
               f'в отдел № {department}'


class Office_equipment_tech:  # There and next "et" in code will be mean "equipment tech"
    def __init__(self,
                 type_of_et: str,
                 name_of_et: str,
                 name_of_brand_of_et: str,
                 serial_number_of_et: str,
                 inventory_number_of_et: int,
                 size_A_of_et_mm: int,
                 size_B_of_et_mm: int,
                 size_H_of_et_mm: int,
                 has_repair_warranty: bool,
                 department: int
                 ):
        self.type_of_et = type_of_et
        self.name_of_et = name_of_et
        self.name_of_brand_of_et = name_of_brand_of_et
        self.serial_number_of_et = serial_number_of_et
        self.inventory_number_of_et = inventory_number_of_et
        self.size_A_of_et_mm = size_A_of_et_mm
        self.size_B_of_et_mm = size_B_of_et_mm
        self.size_H_of_et_mm = size_H_of_et_mm
        self.has_repair_warranty = has_repair_warranty
        self.department = department

    def __str__(self):
        return f'Оргтенхика: {self.type_of_et} ' \
               f'фирмы {self.name_of_brand_of_et}\n' \
               f'Имя: {self.name_of_et}\n' \
               f'Инвентарный №: {self.inventory_number_of_et}\n' \
               f'На гарантии: {self.has_repair_warranty}\n' \
               f'Габарит А, мм: {self.size_A_of_et_mm}\n' \
               f'Габарит B, мм: {self.size_B_of_et_mm}\n' \
               f'Габарит H, мм: {self.size_H_of_et_mm}\n'

    def equipment_tech_move_to_w(self):
        return f'Оргтехника {Office_equipment_tech} прибыла на склад из подразделения {self.department}'

    def equipment_tech_move_from_w_to(self):
        return f'Оргтехника {Office_equipment_tech} покинула склад в подразделение {self.department}'

    def get_info_where_is_equipment_tech(self):
        return f'Оргтехника находится в подразделении № {self.department}'

    def office_equipment_is_working(self):
        return f'Оргтехника работает в подразделении № {self.department}'

    def office_equipment_is_not_working(self):
        return f'Оргтехника не работает в подразделении № {self.department}'

    def online(self):
        return f'{self.name_of_et} is online'

    def offline(self):
        return f'{self.name_of_et} is not online'


class Scaner(Office_equipment_tech):
    def __init__(self,
                 type_of_et: str,
                 name_of_et: str,
                 name_of_brand_of_et: str,
                 serial_number_of_et: str,
                 inventory_number_of_et: int,
                 size_A_of_et_mm: int,
                 size_B_of_et_mm: int,
                 size_H_of_et_mm: int,
                 has_repair_warranty: bool,
                 option_to_scan: bool,
                 size_of_paper_may_scan: list,
                 department
                 ):
        super(Scaner, self).__init__(type_of_et,
                                     name_of_et,
                                     name_of_brand_of_et,
                                     serial_number_of_et,
                                     inventory_number_of_et,
                                     size_A_of_et_mm,
                                     size_B_of_et_mm,
                                     size_H_of_et_mm,
                                     has_repair_warranty,
                                     department
                                     )
        self.option_to_scan = option_to_scan
        self.size_of_paper_may_scan = size_of_paper_may_scan

    @staticmethod
    def scan():
        return f'Сканирование'


class Printer(Office_equipment_tech):
    def __init__(self,
                 type_of_et: str,
                 name_of_et: str,
                 name_of_brand_of_et: str,
                 serial_number_of_et: str,
                 inventory_number_of_et: int,
                 size_A_of_et_mm: int,
                 size_B_of_et_mm: int,
                 size_H_of_et_mm: int,
                 has_repair_warranty: bool,
                 department: int,
                 option_to_print: bool,
                 size_of_paper_may_print: list,
                 ):
        super(Printer, self).__init__(type_of_et,
                                      name_of_et,
                                      name_of_brand_of_et,
                                      serial_number_of_et,
                                      inventory_number_of_et,
                                      size_A_of_et_mm,
                                      size_B_of_et_mm,
                                      size_H_of_et_mm,
                                      has_repair_warranty,
                                      department
                                      )
        self.option_to_print = option_to_print
        self.size_of_paper_may_print = size_of_paper_may_print

    @staticmethod
    def Print():
        return f'Печать'


class Plotter(Printer):
    """Плоттер- это принтер широкого формата"""

    @staticmethod
    def Print_widhtler_format():
        return f'Печать широкого формата'


warehouse = Warehouse(8000, 10000, 3000, 23, 40, True, True, True, 1, 0, {})

printer_1 = Printer('Printer',
                    'AAA 111',
                    'Samsung',
                    'FJ 1111',
                    0,
                    700,
                    700,
                    700,
                    True,
                    departments_of_company[0],
                    True,
                    [297, 330, 'A4'])

printer_2 = Printer('Printer',
                    'NVD 2222',
                    'Sony',
                    'FJ 2222',
                    1,
                    800,
                    800,
                    800,
                    True,
                    departments_of_company[0],
                    True,
                    [594, 330, 'A4'])

scaner_1 = Scaner('Scaner',
                  'XXX 1111',
                  'Philips',
                  'FY 4444',
                  2,
                  900,
                  900,
                  900,
                  False,
                  departments_of_company[0],
                  [1189, 890],
                  45)

plotter_1 = Plotter('Plotter',
                    'NVD 2222',
                    'Sony',
                    'FJ 2222',
                    3,
                    800,
                    800,
                    800,
                    True,
                    departments_of_company[0],
                    True,
                    [1189, 890, 'A0'])


warehouse.w_office_equipment_buy(printer_1.type_of_et)
warehouse.w_office_equipment_income(printer_1.type_of_et, printer_1.name_of_et, printer_1.inventory_number_of_et)
warehouse.w_office_equipment_income(printer_2.type_of_et, printer_2.name_of_et, printer_2.inventory_number_of_et)
warehouse.w_office_equipment_buy(plotter_1.type_of_et)
warehouse.w_office_equipment_income(plotter_1.type_of_et, plotter_1.name_of_et, plotter_1.inventory_number_of_et)
warehouse.w_office_equipment_buy(scaner_1.type_of_et)
warehouse.w_office_equipment_income(scaner_1.type_of_et, scaner_1.name_of_et, scaner_1.inventory_number_of_et)
print(warehouse.w_office_equipment_data_base)
print(warehouse.show_w_office_equipment(printer_1.type_of_et, plotter_1.type_of_et, scaner_1.type_of_et))
print(warehouse.w_office_equipment_outcome(printer_1.type_of_et, printer_1.inventory_number_of_et,
                                           departments_of_company[8]))
print(warehouse.show_w_office_equipment(printer_1.type_of_et, plotter_1.type_of_et, scaner_1.type_of_et))
print(warehouse.w_office_equipment_data_base)
