
def main():
    with open('inmap0.dat', 'r') as f:
        lines = f.readlines()

    first_line = lines[0].strip().split()
    #num_locations = int(first_line[0])
    scale = float(first_line[1])

    map_distances = []
    for i in range(1, len(lines)):
        if lines[i].strip():
            map_distances.append(float(lines[i].strip()))

    mileage_distances = [round(dist * scale, 1) for dist in map_distances]
    total_distance = round(sum(mileage_distances), 1)

    print("Анна")
    print()
    print("Simple Map Distance Computations")
    print()
    print(f"Map Scale Factor:        {scale:.2f} miles per inch")
    print()
    print("Map Measure    Mileage Distance")

    for i, (map_dist, mileage_dist) in enumerate(zip(map_distances, mileage_distances), 1):
        print(f"# {i:<5} {map_dist:<8.1f} {mileage_dist:<8.1f}")

    print()
    print(f"Total Distance:    {total_distance} miles")


if __name__ == "__main__":
    main()
