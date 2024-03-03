import rhinoscriptsyntax as rs

def boolean_difference():
    # Select the objects
    objs = rs.GetObjects("Select two objects for boolean difference", 2)
    if not objs:
        return

    # Check if two objects are selected
    if len(objs) != 2:
        print("Please select exactly two objects.")
        return

    # Get the bounding boxes of the objects
    bbox1 = rs.BoundingBox(objs[0])
    bbox2 = rs.BoundingBox(objs[1])

    # Get the tallest object
    if bbox1[1][2] > bbox2[1][2]:
        tall_obj = objs[0]
        short_obj = objs[1]
    else:
        tall_obj = objs[1]
        short_obj = objs[0]

    # Perform boolean difference
    result = rs.BooleanDifference(tall_obj, [short_obj])
    if result:
        print("Boolean difference successful.")
    else:
        print("Boolean difference failed.")

if __name__ == "__main__":
    boolean_difference()