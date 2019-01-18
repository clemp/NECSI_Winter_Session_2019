import matplotlib.pyplot as plt # data visualization
import numpy as np

test_icsd1 = [(0, 30623), (1, 4781), (2, 2058), (3, 1357), (4, 1010), (5, 795), (6, 659), (7, 565), (8, 497), (9, 450), (10, 409), (11, 382), (12, 362), (13, 336), (14, 316), (15, 307), (16, 285), (17, 271), (18, 264), (19, 257), (20, 242), (21, 234), (22, 223), (23, 213), (24, 202), (25, 200), (26, 187), (27, 181), (28, 175), (29, 169), (30, 164), (31, 160), (32, 154), (33, 149), (34, 140), (35, 138), (36, 132), (37, 131), (38, 128), (39, 127), (40, 123), (41, 121), (43, 120), (44, 119), (45, 116), (47, 112), (49, 107), (50, 104), (51, 100), (52, 97), (53, 96), (54, 94), (55, 93), (56, 91), (57, 90), (58, 88), (59, 86), (60, 85), (61, 83), (62, 82), (63, 79), (64, 78), (65, 77), (66, 76), (67, 75), (69, 74), (72, 72), (73, 71), (75, 70), (77, 69), (78, 68), (79, 66), (80, 65), (81, 63), (82, 61), (83, 60), (84, 59), (90, 57), (91, 56), (92, 55), (95, 54), (96, 52), (98, 50), (100, 49), (102, 48), (104, 47), (106, 46), (107, 45), (109, 44), (110, 43), (122, 42), (123, 41), (134, 40), (135, 38), (140, 37), (143, 35), (147, 34), (149, 33), (151, 32), (155, 31), (158, 27), (161, 26), (163, 23), (171, 22), (182, 21), (192, 20), (206, 19), (259, 18), (287, 17), (301, 16), (304, 15), (328, 14), (334, 13), (380, 12), (386, 11), (394, 10), (432, 9), (437, 8), (501, 7), (515, 6), (693, 5), (764, 3), (916, 2), (2196, 1)]


test_icsd2 = [(0, 339092), (1, 63281), (2, 25134), (3, 15648), (4, 11506), (5, 9116), (6, 7599), (7, 6530), (8, 5717), (9, 5108), (10, 4645), (11, 4244), (12, 3910), (13, 3632), (14, 3377), (15, 3194), (16, 3020), (17, 2863), (18, 2713), (19, 2587), (20, 2459), (21, 2351), (22, 2258), (23, 2165), (24, 2086), (25, 2004), (26, 1915), (27, 1849), (28, 1791), (29, 1736), (30, 1669), (31, 1624), (32, 1554), (33, 1509), (34, 1466), (35, 1420), (36, 1370), (37, 1325), (38, 1291), (39, 1271), (40, 1239), (41, 1208), (42, 1184), (43, 1152), (44, 1125), (45, 1096), (46, 1069), (47, 1048), (48, 1018), (49, 998), (50, 971), (51, 943), (52, 924), (53, 903), (54, 884), (55, 870), (56, 854), (57, 847), (58, 833), (59, 810), (60, 800), (61, 780), (62, 764), (63, 746), (64, 740), (65, 728), (66, 715), (67, 706), (68, 694), (69, 686), (70, 675), (71, 662), (72, 653), (73, 644), (74, 634), (75, 622), (76, 615), (77, 610), (78, 604), (79, 589), (80, 580), (81, 566), (82, 560), (83, 551), (84, 546), (85, 531), (86, 523), (87, 513), (88, 506), (89, 496), (90, 491), (91, 489), (92, 484), (93, 477), (94, 470), (95, 468), (96, 462), (97, 456), (98, 450), (99, 441), (100, 435), (101, 432), (102, 428), (103, 422), (104, 416), (105, 412), (106, 407), (107, 400), (108, 395), (109, 390), (110, 386), (111, 380), (112, 376), (113, 375), (114, 369), (115, 365), (116, 360), (117, 359), (118, 354), (120, 353), (121, 349), (122, 343), (123, 339), (124, 334), (125, 331), (126, 329), (127, 325), (128, 322), (129, 320), (131, 318), (132, 316), (133, 315), (134, 311), (135, 307), (136, 301), (137, 297), (139, 292), (140, 290), (141, 284), (142, 282), (143, 278), (144, 277), (145, 274), (146, 271), (147, 269), (149, 263), (151, 262), (152, 258), (153, 256), (154, 252), (155, 248), (156, 240), (157, 238), (158, 236), (159, 235), (160, 233), (161, 231), (162, 227), (163, 224), (164, 221), (165, 220), (167, 217), (168, 214), (170, 213), (171, 212), (172, 210), (174, 206), (175, 205), (178, 203), (180, 202), (182, 200), (183, 197), (184, 196), (185, 193), (186, 191), (187, 189), (188, 185), (189, 184), (191, 182), (192, 180), (193, 178), (195, 177), (196, 176), (197, 174), (198, 173), (199, 172), (200, 170), (201, 169), (202, 168), (203, 167), (204, 166), (205, 163), (206, 161), (207, 159), (208, 157), (209, 152), (210, 150), (213, 148), (214, 147), (221, 145), (222, 142), (227, 141), (228, 138), (229, 137), (235, 135), (239, 134), (241, 133), (242, 132), (244, 131), (246, 130), (247, 129), (248, 128), (249, 127), (253, 124), (254, 123), (255, 122), (257, 119), (258, 117), (259, 115), (260, 114), (262, 113), (266, 112), (267, 111), (268, 110), (273, 109), (274, 108), (275, 107), (276, 106), (277, 104), (279, 103), (280, 102), (284, 100), (285, 99), (287, 97), (289, 96), (291, 94), (295, 93), (298, 92), (299, 90), (300, 89), (301, 88), (302, 87), (304, 86), (307, 85), (313, 84), (314, 83), (322, 82), (324, 81), (328, 80), (329, 79), (334, 78), (339, 77), (348, 76), (360, 75), (361, 74), (366, 73), (369, 72), (371, 71), (375, 70), (377, 69), (380, 68), (381, 65), (385, 64), (386, 63), (388, 62), (390, 61), (393, 60), (394, 59), (406, 58), (412, 57), (418, 56), (432, 55), (434, 54), (436, 53), (437, 52), (453, 51), (461, 49), (466, 48), (469, 47), (472, 46), (488, 45), (501, 44), (507, 43), (514, 42), (515, 41), (529, 40), (543, 39), (557, 38), (559, 37), (573, 36), (590, 35), (613, 34), (614, 33), (622, 32), (625, 31), (643, 30), (648, 29), (652, 28), (662, 27), (693, 26), (703, 24), (764, 23), (776, 22), (811, 21), (867, 20), (891, 19), (916, 18), (923, 17), (925, 16), (1046, 15), (1063, 14), (1097, 13), (1142, 12), (1162, 11), (1229, 10), (1306, 9), (1500, 8), (1579, 7), (1648, 6), (1768, 5), (2157, 4), (2196, 3), (3060, 2), (3973, 1)]

x1 = [d[0] for d in test_icsd1[1:]]
y1 = [d[1] for d in test_icsd1[1:]]

x2 = [d[0] for d in test_icsd2[1:]]
y2 = [d[1] for d in test_icsd2[1:]]

fit1 = np.polyfit(np.log10(x1), np.log10(y1), 1)
fit2 = np.polyfit(np.log10(x2), np.log10(y2), 1)

print("fit1: ", fit1)
print("fit2: ", fit2)

y11 = np.polyval(fit1, np.log10(x1)) # fit line of x1, y1; plot 10**y11

y22 = np.polyval(fit2, np.log10(x2)) # fit line of x2, y2; plot 10**y22

# Plot properties
a = 0.6

# ax = plt.gca()
plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "black",
    "axes.facecolor": "black",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "lightgray",
    "legend.facecolor": "white",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})
# Configure plot figure
plt.figure(figsize=(13, 8)) # adjust figure size
# plt.style.use('dark_background')
# plt.plot(x, y, 'g-', label='model') # plot with green line

plt.scatter(x1, y1, s=6, alpha = a, label='# RTs <= 35k')
plt.scatter(x2, y2, s=6, alpha = a, label='# RTs 350k+ fit')

# Plot fit lines
plt.plot(x1, 10**y11, label='# RTs <= 35k fit', alpha=0.5)
plt.plot(x2, 10**y22, label='# RTs 350k+ fit', alpha=0.5)


plt.ylabel('inverse cumulative sum of Kin', size = 18, color='w') # add LaTeX label on y-axis, increase size
plt.xlabel('Kin', size = 18, color='w') # add label on x-axis, increase size

# Create x,y axis log scale
plt.xscale("log")
plt.yscale("log")

plt.setp(plt.legend().get_texts(), color='w')
plt.legend(loc='best') # add legend for labels
plt.tight_layout() # fit chart to output figure
plt.show()
