
#### Star Tracking Algorithm for telescope guiding system ####

Author: Jervis Ong Zhe Ao

To run the algorithm, open main.py and first utilize the function track_movement. You will need to input the location of your local folder which contains the images. Example images are provided in the subfolder 'Images'. A txt is then generated which contains the coordinates of the star. This function can be modified to suit your purposes. For example, it can be modified to provided the coordinates of two stars respectively. This results in a txt file with 5 columns (x1, x2, y1, y2 and t) instead of three. 

Once we have the txt file with the coordinates, the results can be analysed with the function plot_movement. An example output txt file for 2 stars is provided as WideFieldRun.txt. This can be input into the function to obtain results.jpg.
