from google.colab import files
print("Upload content image:")
uploaded = files.upload()
content_image_path = list(uploaded.keys())[0] 
print("Upload style image:")
uploaded = files.upload()
style_image_path = list(uploaded.keys())[0]
content_image = load_image(content_image_path)
style_image = load_image(style_image_path)
content_image.shape
plt.imshow(np.squeeze(style_image))
plt.show()
stylized_image = model(tf.constant(content_image), tf.constant(style_image))[0]
plt.imshow(np.squeeze(stylized_image))
plt.show()
