from fastai.vision.all import ImageDataLoaders, get_image_files, resnet50, ResNet50_Weights, Resize, cnn_learner, error_rate, PILImage
from pathlib import Path

def is_cat(x):
    return x[0].isupper()

path = Path("./ch1/images/")

file_list = get_image_files(path=path).items

dls = ImageDataLoaders.from_name_func(
path, file_list, valid_pct=0.2, seed=42,
label_func=is_cat, item_tfms=Resize(224))

learn = cnn_learner(dls, resnet50, metrics=error_rate)

learn.fit(10)

is_puppy, _, prob = learn.predict(PILImage.create('./ch1/predict/canvas.png'))

print(f"is puppy {is_puppy}")
print(f"probability {prob}")

learn.show_results()
