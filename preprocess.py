import os
parser = argparse.ArgumentParser(description='Neural style transfer with Keras.')
parser.add_argument('base_image_path', metavar='base', type=str,
                    help='Path to the image to transform.')
parser.add_argument('directory', metavar='base', type=str,
                    help='directory to the image to transform')
parser.add_argument('style_reference_image_path', metavar='ref', type=str,
                    help='Path to the style reference image.')
parser.add_argument('result_prefix', metavar='res_prefix', type=str,
                    help='Prefix for the saved results.')

args = parser.parse_args()
base_image_path = args.base_image_path
directory = args.directory
style_reference_image_path = args.style_reference_image_path
result_prefix = args.result_prefix
weights_path = 'vgg16_weights.h5'

# these are the weights of the different loss components
total_variation_weight = 1.
style_weight = 1.
content_weight = 0.025

cmd1= 'cd sourcevideo'
cmd2="ffmpeg -i " + base_image_path + " -r 12 -f image2 "+directory+"/image-%5d.jpg"
cmd3="ffmpeg -i " + base_image_path +" "+directory+"/rawaudio.wav"
os.system(cmd1)
os.system(cmd2)
os.system(cmd3)

for file in os.listdir(directory):
    #fullfilename = directory+file
    if file.endswith('.jpg'):
        #img=preprocess_image(directory+'/'+file)
        img=imresize(imread(directory+'/'+file),(img_width, img_height))
        fname = directory+'/'+file + '.png'
        imsave(fname, img)