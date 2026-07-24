from architecture.building import Building


def create_plan(building):

    plan = {

        "نوع": "پلان شماتیک",

        "عرض ساختمان":
        building.width,

        "طول ساختمان":
        building.length,

        "طبقات":
        building.floors,

        "زیربنا":
        building.total_area

    }

    return plan