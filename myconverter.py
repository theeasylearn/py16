#foot, meter, kilometer, mile 
def get_foot(inch):
    foot = inch / 12
    return foot 

def get_meter(inch):
    meter = get_foot(inch) / 3.281
    return meter 

def get_kilometer(inch):
    kilometer = get_meter(inch) / 1000
    return kilometer

def get_mile(inch):
    mile = get_kilometer(inch) / 1.6
    return mile 
