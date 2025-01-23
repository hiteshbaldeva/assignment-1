### Consider a 3-D co-ordinate space. Input 10 3-D points. Find the nearest neighbour for each 
###  of the points in your 3-D space and store them in a list. The final output is a list with each 
### consisting of a point and its nearest neighbour. [Hint: Use distance between two points 
list_x=[]
list_y=[]
list_z=[]
for i in range(1,11):
    x=int(input(f"enter the x{i} coordinate :"))
    list_x.append(x)
    y=int(input(f"enter the y{i} coordinate :"))
    list_y.append(y)
    z=int(input(f"enter the z{i} coordinate :"))
    list_z.append(z)

print(list_x)
print(list_y)
print(list_z)

nearest_neighbors = []

for i in range(10):
    min_distance = float('inf')
    nearest_neighbor = None
    
    for j in range(10):
        if i != j:
            distance = ((list_x[j] - list_x[i])**2 + (list_y[j] - list_y[i])**2 + (list_z[j] - list_z[i])**2)**0.5
            
            if distance < min_distance:
                min_distance = distance
                nearest_neighbor = (list_x[j], list_y[j], list_z[j])
    
    nearest_neighbors.append(((list_x[i], list_y[i], list_z[i]), nearest_neighbor))

# Print the list of each point and its nearest neighbor
for point, neighbor in nearest_neighbors:
    print(f"Point {point} has nearest neighbor {neighbor}")

           