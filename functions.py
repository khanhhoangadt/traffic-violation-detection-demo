import cv2
def scaleFrame(frame,factor=0.25):
    height,width, layers = frame.shape
    # print(width, height,layers)
    return cv2.resize(frame, (int(width*factor),int(height*factor)))
def helloworld():
   print("hello")
def hist():
    plt.hist(mag.ravel())
    fig.canvas.draw()
    data = np.fromstring(fig.canvas.tostring_rgb(), dtype=np.uint8, sep='')
    data = data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    bgr1 = cv2.cvtColor(data,cv2.COLOR_HSV2BGR)
    fig.clf()
