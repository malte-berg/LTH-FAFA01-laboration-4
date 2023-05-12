import matplotlib.pyplot as plt

# Open the file and read the data
with open("txt/5slit.txt") as f:
    lines = f.readlines()[1:] # Skip the header

# Parse the data into separate lists
x = []
total_diffraction = []
diffraction_pattern = []
interference_pattern = []
from_camera = []
for line in lines:
    values = line.strip().split()
    if len(values) == 5: # Check that the line has 5 values
        x.append(float(values[0].replace(",", ".")))
        total_diffraction.append(float(values[1].replace(",", ".")))
        diffraction_pattern.append(float(values[2].replace(",", ".")))
        interference_pattern.append(float(values[3].replace(",", ".")))
        from_camera.append(float(values[4].replace(",", ".")))
#from_camera = from_camera[-32:] + from_camera[:-32]
#from_camera = from_camera[8:] + from_camera[:8]
#from_camera = from_camera[-1:] + from_camera[:-1]
from_camera = from_camera[-8:] + from_camera[:-8]

# Create the plot
fig, ax = plt.subplots()
ax.set_title('5 spalter')
ax.set_ylabel('Relativ intensitet')
ax.set_xlabel('Avstånd på skärmen (m)')
ax.plot(x, total_diffraction, label='Förväntad diffraktion')
ax.plot(x, from_camera, label='Från kamera')
ax.set_xlim(-0.01, 0.01)
ax.legend()
plt.show()
