import rhinoscriptsyntax as rs

def find_unique_objects():
    # Get all the objects in the document
    all_objects = rs.AllObjects()

    # Dictionary to store objects by their heights
    objects_by_height = {}

    # Iterate through all objects
    for obj in all_objects:
        # Get the bounding box of the object
        bbox = rs.BoundingBox(obj)
        if bbox is None:
            continue

        # Round the height to some decimal places to avoid floating point precision issues
        height = round(bbox[1][2], 3)

        # Get the objects at the same height
        objects_at_height = objects_by_height.get(height, [])
        objects_at_height.append(obj)
        objects_by_height[height] = objects_at_height

    # List to store unique objects
    unique_objects = []

    # Iterate through the dictionary
    for height, objects in objects_by_height.items():
        # If there's only one object at the height, it's unique
        if len(objects) == 1:
            unique_objects.append(objects[0])

    return unique_objects

def main():
    unique_objects = find_unique_objects()

    if unique_objects:
        print("Unique objects found:")
        for obj in unique_objects:
            print("Object GUID:", obj)
    else:
        print("No unique objects found.")

if __name__ == "__main__":
    main()
