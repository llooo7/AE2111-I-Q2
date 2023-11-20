import matplotlib.pyplot as plt
import numpy as np

x1, x2, y1, y2 = [], [], [], []

data1 = [
 0.000000 , 0.000000,
 0.002000 , 0.010800,
 0.005000 , 0.016600,
 0.010000 , 0.022500,
 0.020000 , 0.029900,
 0.030000 , 0.035000,
 0.040000 , 0.038900,
 0.050000 , 0.042100,
 0.060000 , 0.044800,
 0.070000 , 0.047100,
 0.080000 , 0.049100,
 0.090000 , 0.051000,
 0.100000 , 0.052700,
 0.110000 , 0.054200,
 0.120000 , 0.055600,
 0.130000 , 0.056900,
 0.140000 , 0.058100,
 0.150000 , 0.059200,
 0.160000 , 0.060200,
 0.170000 , 0.061200,
 0.180000 , 0.062100,
 0.190000 , 0.062900,
 0.200000 , 0.063700,
 0.210000 , 0.064400,
 0.220000 , 0.065100,
 0.230000 , 0.065700,
 0.240000 , 0.066300,
 0.250000 , 0.066800,
 0.260000 , 0.067300,
 0.270000 , 0.067700,
 0.280000 , 0.068100,
 0.290000 , 0.068500,
 0.300000 , 0.068800,
 0.310000 , 0.069100,
 0.320000 , 0.069300,
 0.330000 , 0.069500,
 0.340000 , 0.069700,
 0.350000 , 0.069900,
 0.360000 , 0.070000,
 0.370000 , 0.070100,
 0.380000 , 0.070200,
 0.390000 , 0.070200,
 0.400000 , 0.070200,
 0.410000 , 0.070200,
 0.420000 , 0.070100,
 0.430000 , 0.070000,
 0.440000 , 0.069900,
 0.450000 , 0.069700,
 0.460000 , 0.069500,
 0.470000 , 0.069300,
 0.480000 , 0.069000,
 0.490000 , 0.068700,
 0.500000 , 0.068400,
 0.510000 , 0.068000,
 0.520000 , 0.067600,
 0.530000 , 0.067200,
 0.540000 , 0.066700,
 0.550000 , 0.066200,
 0.560000 , 0.065600,
 0.570000 , 0.065000,
 0.580000 , 0.064300,
 0.590000 , 0.063600,
 0.600000 , 0.062800,
 0.610000 , 0.062000,
 0.620000 , 0.061100,
 0.630000 , 0.060200,
 0.640000 , 0.059300,
 0.650000 , 0.058300,
 0.660000 , 0.057300,
 0.670000 , 0.056200,
 0.680000 , 0.055100,
 0.690000 , 0.054000,
 0.700000 , 0.052800,
 0.710000 , 0.051600,
 0.720000 , 0.050300,
 0.730000 , 0.049000,
 0.740000 , 0.047700,
 0.750000 , 0.046400,
 0.760000 , 0.045000,
 0.770000 , 0.043600,
 0.780000 , 0.042200,
 0.790000 , 0.040700,
 0.800000 , 0.039200,
 0.810000 , 0.037700,
 0.820000 , 0.036200,
 0.830000 , 0.034600,
 0.840000 , 0.033000,
 0.850000 , 0.031400,
 0.860000 , 0.029800,
 0.870000 , 0.028100,
 0.880000 , 0.026400,
 0.890000 , 0.024700,
 0.900000 , 0.022900,
 0.910000 , 0.021100,
 0.920000 , 0.019300,
 0.930000 , 0.017500,
 0.940000 , 0.015600,
 0.950000 , 0.013700,
 0.960000 , 0.011700,
 0.970000 , 0.009700,
 0.980000 , 0.007600,
 0.990000 , 0.005500,
 1.000000 , 0.003300]
data2 = [
 0.000000,  0.000000,
 0.002000, -0.010800,
 0.005000, -0.016600,
 0.010000, -0.022500,
 0.020000, -0.029900,
 0.030000, -0.035000,
 0.040000, -0.038900,
 0.050000, -0.042100,
 0.060000, -0.044800,
 0.070000, -0.047200,
 0.080000, -0.049300,
 0.090000, -0.051200,
 0.100000, -0.052900,
 0.110000, -0.054500,
 0.120000, -0.056000,
 0.130000, -0.057300,
 0.140000, -0.058500,
 0.150000, -0.059700,
 0.160000, -0.060800,
 0.170000, -0.061800,
 0.180000, -0.062700,
 0.190000, -0.063600,
 0.200000, -0.064400,
 0.210000, -0.065100,
 0.220000, -0.065800,
 0.230000, -0.066400,
 0.240000, -0.067000,
 0.250000, -0.067500,
 0.260000, -0.068000,
 0.270000, -0.068400,
 0.280000, -0.068800,
 0.290000, -0.069100,
 0.300000, -0.069400,
 0.310000, -0.069600,
 0.320000, -0.069800,
 0.330000, -0.069900,
 0.340000, -0.070000,
 0.350000, -0.070000,
 0.360000, -0.070000,
 0.370000, -0.069900,
 0.380000, -0.069800,
 0.390000, -0.069700,
 0.400000, -0.069500,
 0.410000, -0.069300,
 0.420000, -0.069000,
 0.430000, -0.068600,
 0.440000, -0.068200,
 0.450000, -0.067700,
 0.460000, -0.067200,
 0.470000, -0.066600,
 0.480000, -0.065900,
 0.490000, -0.065100,
 0.500000, -0.064200,
 0.510000, -0.063300,
 0.520000, -0.062300,
 0.530000, -0.061200,
 0.540000, -0.060000,
 0.550000, -0.058700,
 0.560000, -0.057300,
 0.570000, -0.055800,
 0.580000, -0.054300,
 0.590000, -0.052700,
 0.600000, -0.051000,
 0.610000, -0.049200,
 0.620000, -0.047400,
 0.630000, -0.045500,
 0.640000, -0.043500,
 0.650000, -0.041500,
 0.660000, -0.039400,
 0.670000, -0.037300,
 0.680000, -0.035200,
 0.690000, -0.033000,
 0.700000, -0.030800,
 0.710000, -0.028600,
 0.720000, -0.026400,
 0.730000, -0.024200,
 0.740000, -0.022000,
 0.750000, -0.019800,
 0.760000, -0.017700,
 0.770000, -0.015600,
 0.780000, -0.013600,
 0.790000, -0.011600,
 0.800000, -0.009700,
 0.810000, -0.007800,
 0.820000, -0.006000,
 0.830000, -0.004300,
 0.840000, -0.002700,
 0.850000, -0.001200,
 0.860000,  0.000100,
 0.870000,  0.001300,
 0.880000,  0.002300,
 0.890000,  0.003200,
 0.900000,  0.003900,
 0.910000,  0.004400,
 0.920000,  0.004600,
 0.930000,  0.004600,
 0.940000,  0.004300,
 0.950000 , 0.003800,
 0.960000 , 0.003100,
 0.970000 , 0.002100,
 0.980000 , 0.000800,
 0.990000 ,-0.000800,
 1.000000 ,-0.002700,
 1.000000,  0.003300]

wingbox = [
0.1, -0.052900,
0.1, 0.052700,
0.71, 0.051600,
0.71, -0.028600,
]

wingboxX=[0.1, 0.1, 0.71, 0.71, 0.1]
wingboxY=[-0.0529, 0.0527, 0.0516, -0.0286, -0.05290]

j = 0
for i in data1:
    if j%2==0:
        x1.append(i)
    else:
        y1.append(i)
    j += 1
for i in data2:
    if j%2==0:
        x2.append(i)
    else:
        y2.append(i)
    j += 1

fig, ax = plt.subplots()
ax.plot(x1, y1, color="black")
ax.plot(x2, y2, color="black")
ax.plot(wingboxX, wingboxY, color="blue")
plt.ylim(-0.2, 0.2)
plt.title("SC 20414")

plt.show()