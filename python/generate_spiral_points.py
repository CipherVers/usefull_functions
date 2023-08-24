import numpy as np

def generate_spiral_points(city_lon, city_lat, population):
    # Define parameters for the spiral
    a = 0.0001 * np.sqrt(population)  # Adjust the scaling factor as needed
    b = 0.001
    num_points = int(7200*a)  # Number of points to generate along the spiral

    spiral_lon = []
    spiral_lat = []

    for angle in np.linspace(0, 2*np.pi*40, num_points, endpoint=False):
        # Calculate the new latitude and longitude using the spiral equation
        radius = (3*a)*(1-np.exp(-angle*b))
        new_lat = city_lat + radius * np.cos(angle)
        new_lon = city_lon + radius * np.sin(angle)

        spiral_lon.append(new_lon)
        spiral_lat.append(new_lat)

    return spiral_lon, spiral_lat

# Example usage
# 48.8667	2.3333	9904000	Paris
# 2237,Toulouse,493465,43.60426,1.44367
# 994,Lille,234475,50.63297,3.05858

city_longitude = 1.44367  # Example city's longitude 
city_latitude = 43.60426  # Example city's latitude 
city_population = 493465  # Example city's population 

spiral_lon, spiral_lat = generate_spiral_points(city_longitude, city_latitude, city_population)

print("Spiral Longitude Points:", spiral_lon)
print("Spiral Latitude Points:", spiral_lat)

dicdf = pd.DataFrame({
    "lon":spiral_lon,
    "lat":spiral_lat
})
dicdf.to_csv("spiral.csv")
