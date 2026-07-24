class Building:

    def __init__(
        self,
        length,
        width,
        floors,
        occupancy_ratio=60
    ):

        self.length = length
        self.width = width
        self.floors = floors
        self.occupancy_ratio = occupancy_ratio


    @property
    def land_area(self):

        return self.length * self.width


    @property
    def floor_area(self):

        return (
            self.land_area *
            self.occupancy_ratio / 100
        )


    @property
    def total_area(self):

        return (
            self.floor_area *
            self.floors
        )


    def info(self):

        return {

            "مساحت زمین":
            self.land_area,

            "زیربنای هر طبقه":
            self.floor_area,

            "زیربنای کل":
            self.total_area,

            "تعداد طبقات":
            self.floors
        }