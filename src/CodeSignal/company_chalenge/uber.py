def map_car_edges(luckySpot,car_dimension):
    left_up=luckySpot[0]
    left_bottom=luckySpot[1]
    right_up=luckySpot[2]
    right_bottom=luckySpot[3]
    begin_cars_position=(left_up,left_bottom)
    end_cars_position=(left_up+car_dimension[0]-1,right_up+car_dimension[1]-1)

    return (begin_cars_position,end_cars_position)


def parking_slot(carDimensions,parkingLot,luckySpot):
    pass


if __name__=="__main__":
    map_car_edges(luckySpot=[1,1,2,3],
                  car_dimension=[3,2])